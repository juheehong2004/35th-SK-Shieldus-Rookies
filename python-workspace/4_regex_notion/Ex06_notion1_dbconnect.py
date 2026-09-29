
import os
from dotenv import load_dotenv
from notion_client import Client

# 1. 환경변수 로드
load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# 2. Notion 연결
notion = Client(auth=NOTION_TOKEN)


# 3. Notion 데이터베이스의 정보를 조회
db_info = notion.databases.retrieve(NOTION_DATABASE_ID)

# 4. 조회한 데이터베이스 정보에서 Data Source ID를 가져옴
data_source_id = db_info["data_sources"][0]["id"]

# Data Source ID 출력
print("Data Source ID:", data_source_id)

