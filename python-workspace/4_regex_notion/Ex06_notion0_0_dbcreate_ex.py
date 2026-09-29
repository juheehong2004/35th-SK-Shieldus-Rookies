"""
노션-파이썬 연결 이전 버전
"""

import os
import requests
from dotenv import load_dotenv


# .env 파일 로드
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")


# 1. HTTP 요청 헤더
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}", # ******* Bearer 뒤에 공백 필수
    "Notion-Version": "2026-03-11",
    "Content-Type": "application/json"
}


# 2. 데이터베이스 생성에 사용할 JSON
data = {
    "parent": {
        "type": "page_id",
        "page_id": NOTION_PARENT_PAGE_ID
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "학생 관리0"
            }
        }
    ],
    "initial_data_source": {
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
}


# 3. Notion API에 직접 HTTP POST 요청 (키 안보이게)
response = requests.post(
    "https://api.notion.com/v1/databases",
    headers=headers,
    json=data
)


# 4. 응답(결과) 확인
if response.status_code == 200:
    database = response.json()

    # Database ID
    database_id = database["id"]

    # Data Source ID
    data_source_id = database["data_sources"][0]["id"]

    print("데이터베이스 생성 완료!")
    print("Database ID:", database_id)
    print("Data Source ID:", data_source_id)

else:
    print("생성 실패")
    print("상태 코드:", response.status_code)
    print("오류:", response.text)