import os
from dotenv import load_dotenv
from notion_client import Client

load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

notion = Client(auth=NOTION_TOKEN)

db_info = notion.databases.retrieve(NOTION_DATABASE_ID)

data_source_id = db_info["data_sources"][0]["id"]

print("Data Source ID:", data_source_id)


# ---------- 데이터베이스 조회 
result = notion.data_sources.query(
    data_source_id=data_source_id,

    # 필터 작성
    # 상태가 재학인 행 검색
    # filter = {
    #     "property" : "상태",
    #     "select" : {
    #         "equals" : "재학"
    #     }
    # }
    # 이름에 홍 이라는 글자가 있는 행 검색
    # filter = {
    #     "property" : "이름",
    #     "title" : {
    #         "contains" : "홍"
    #     }
    # }
    # 나이가 30 이상인 행 검색
    filter = {
        "property" : "나이",
        "number" : {
            "greater_than_or_equal_to" : 30
       }
    }

)
#----------------------------

print("\n=== 데이터베이스 내용 ===")

for page in result["results"]:
    
    name = page["properties"]["이름"]["title"][0]["plain_text"]
    age = page["properties"]["나이"]["number"]
    status = page["properties"]["상태"]["select"]["name"]

    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"상태: {status}")
    print("-" * 30)