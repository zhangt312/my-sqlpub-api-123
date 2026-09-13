from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import os

app = FastAPI()

# 允许所有来源跨域访问（方便手机App和前端网页调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- 数据库连接配置（从 Render 环境变量读取） ----------
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "cursorclass": pymysql.cursors.DictCursor
}

# ---------- 定义多表查询集合（核心部分） ----------
# 键名：前端按钮 data-query 对应的值
# 键值：要执行的 SQL 语句（可以随意写 SELECT、JOIN、WHERE、ORDER BY 等）
QUERIES = {
    "60ksldz": "SELECT * FROM 60K缩量大涨 ",
    "trueslxg": "SELECT * FROM 真缩量新高",
    "cyflweekk":"select * from 超越放量周K",
    "zkxh":"select * from 周K吸货",
}

# ---------- API 接口 ----------
@app.get("/api/data")
def get_data(query: str = Query("orders", description="查询名称，对应 QUERIES 字典的键")):
    """
    根据 query 参数执行对应的 SQL 查询
    例如：/api/data?query=orders  -> 执行 QUERIES["orders"] 中的 SQL
    """
    sql = QUERIES.get(query)
    if sql is None:
        return {
            "error": f"未知的查询名称: '{query}'",
            "available": list(QUERIES.keys())
        }

    try:
        conn = pymysql.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
        conn.close()
        return {
            "query": query,
            "row_count": len(result),
            "data": result
        }
    except Exception as e:
        return {
            "query": query,
            "error": str(e)
        }

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "多表查询 API 已就绪",
        "available_queries": list(QUERIES.keys())
    }

# ---------- （可选）健康检查接口，方便监控 ----------
@app.get("/health")
def health():
    return {"status": "healthy"}
