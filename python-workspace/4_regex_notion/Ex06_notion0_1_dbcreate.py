import os
from dotenv import load_dotenv
from notion_client import Client


# .env 파일 로드
load_dotenv()

# 1. Notion 연결
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

#----------------------------------
# 이전과 달리 연동이 한줄이면 됨
notion = Client(auth=NOTION_TOKEN)
#----------------------------------

# 2. 데이터베이스 생성
database = notion.databases.create(
    parent={
        "type": "page_id",
        "page_id": NOTION_PARENT_PAGE_ID
    },
    title=[
        {
            "type": "text",
            "text": {
                "content": "학생 관리"
            }
        }
    ],
    initial_data_source={
        "properties": {
            "이름": {
                "title": {}
            },
            "나이": {
                "number": {}
            },
            "상태": {
                "select": {
                    "options": [
                        {"name": "재학"},
                        {"name": "졸업"}
                    ]
                }
            }
        }
    }
)

# 생성된 Database ID
database_id = database["id"]

# 생성된 Data Source ID
data_source_id = database["data_sources"][0]["id"]

print("데이터베이스 생성 완료!")
print("Database ID:", database_id)
print("Data Source ID:", data_source_id)


# *******[ 확인 ]*************
# 출력 후에 NOTION_DATABASE_ID과 NOTION_DATA_SOURCE_ID 값을 .env에 저장합니다.

# 위에처럼 수동적 저장이 아니라 자동으로 저장되게 추가 작업을 하셔야 합니다.



'''
실무(인프라 자동화) 관점에서 아래 3가지는 보완이 필요합니다.

1. 환경변수 검증 누락 — .env에 값이 없으면 notion.databases.create()에서 알아듣기 힘든 에러가 남
2. 에러 핸들링 없음 — API 실패 시(APIResponseError) 원인 파악이 어려움
3. "출력 후 수동으로 .env에 저장"  
    →  자동화 스크립트인데 마지막 단계가 수작업. python-dotenv의 set_key()로 자동 반영하는 게 실무형

'''