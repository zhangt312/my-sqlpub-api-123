# my-sqlpub-api-123
读取sqlpub上的mysql数据库

# SQLPub 数据查询项目

## 项目简介
本项目通过 GitHub 托管后端代码，使用 Render 免费 Web Service 部署 FastAPI 接口，连接 sqlpub 的 MySQL 数据库，并在本地通过 `index.html` 网页查询和展示数据。

## 在线链接
- GitHub 仓库：https://github.com/zhangt312/my-sqlpub-api-123
- Render 后端服务：https://my-sqlpub-api-123.onrender.com
- 本地前端文件：`D:\index.html`

## 技术架构
sqlpub MySQL 数据库 → GitHub 仓库 (main.py) → Render Web Service → 本地 index.html

## 文件说明
| 文件 | 说明 |
|------|------|
| `main.py` | FastAPI 后端，定义 `QUERIES` 查询字典，连接 MySQL，提供 `/api/data` 接口 |
| `requirements.txt` | Python 依赖清单（fastapi、uvicorn、pymysql） |
| `index.html` | 本地前端页面，按钮触发查询，表格展示结果 |

## 部署流程
1. 在 GitHub 创建仓库 `my-sqlpub-api-123`。
2. 编写 `main.py` 和 `requirements.txt`，提交到仓库。
3. 在 Render 创建 Web Service，连接该 GitHub 仓库。
4. 配置环境变量：`DB_HOST`、`DB_USER`、`DB_PASS`、`DB_NAME`。
5. 设置 Build Command：`pip install -r requirements.txt`  
   Start Command：`uvicorn main:app --host 0.0.0.0 --port 10000`
6. 部署成功后，获得服务地址 `https://my-sqlpub-api-123.onrender.com`。
7. 在本地 D 盘保存 `index.html`，将 `API_BASE` 改为上述 Render 地址。

## 使用说明
- 双击打开 `D:\index.html`。
- 点击按钮查询对应表。
- 查询结果以 Tab 分隔的表格文本显示，可复制到 Excel 自动分列。
- 新增查询：在 `main.py` 的 `QUERIES` 中增加键值对，并在 `index.html` 的按钮组中增加对应 `data-query` 按钮。

## 注意事项
- Render 免费实例 15 分钟无访问会休眠，再次访问需等待约 30–50 秒。可用 UptimeRobot 定时 ping 保持唤醒。
- 表名和字段名必须与 sqlpub 数据库完全一致。
- 若表名以数字开头或包含中文，建议在 SQL 中使用反引号，例如 ``SELECT * FROM `60K缩量大涨` ``。
- 修改代码后提交到 GitHub，Render 会自动重新部署；若未触发，可在 Render 控制台点击 **Manual Deploy → Deploy latest commit**。

## 常见问题
- **提示“未知的查询名称”**：检查前端 `data-query` 与后端 `QUERIES` 的键名是否完全一致。
- **提示表不存在**：检查 SQL 中的表名是否与 sqlpub 中一致。
- **首次访问慢**：Render 免费实例冷启动导致，等待几十秒即可。

## 许可证
个人学习使用。
