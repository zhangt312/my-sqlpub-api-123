from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data():
    # 从 Render 环境变量中读取（非常安全，密码不会泄露）
    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM 60k缩量大涨 ")  # ⚠️ 改成你的表名
        result = cursor.fetchall()
    conn.close()
    return result

@app.get("/")
def root():
    return {"status": "ok"}
