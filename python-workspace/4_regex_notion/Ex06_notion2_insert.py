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


def insertRecord(name, age, status):

    # 5. Notion 데이터베이스에 데이터 추가
    notion.pages.create(
        parent={
            "type": "data_source_id",
            "data_source_id": data_source_id
        },
        properties={
            "이름": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "나이": {
                "number": age
            },
            "상태": {
                "select": {
                    "name": status
                }
            }
        }
    )


    print("\n데이터 추가 완료!")
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"상태: {status}")

if __name__ == '__main__':
    # 4. 사용자 입력 받기
    print("\n=== Notion 데이터 입력 ===")
    name = input("이름을 입력하세요: ")
    age = int(input("나이를 입력하세요: "))
    status = input("상태를 입력하세요 (예: 재학, 휴학, 졸업): ")
    insertRecord(name,age,status)
