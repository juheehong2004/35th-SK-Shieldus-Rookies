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



# 5. 데이터베이스 조회
result = notion.data_sources.query(
    data_source_id=data_source_id
)

pages = result["results"]

print("\n=== 학생 목록 ===")

for i, page in enumerate(pages, start=1):

    properties = page["properties"]

    name = properties["이름"]["title"][0]["plain_text"]
    age = properties["나이"]["number"]

    status_data = properties["상태"]["select"]

    if status_data:
        status = status_data["name"]
    else:
        status = "없음"

    print(f"{i}. 이름: {name}")
    print(f"   나이: {age}")
    print(f"   현재 상태: {status}")
    print("-" * 30)


# ..............................................
# 6. 수정할 학생 선택
update_num = int(input('수정할 번호를 입력하세요 ->'))

# 번호에 해당하는 페이지 선택
page_id = pages[update_num-1]["id"]

# ..............................................
# 7. 새로운 상태 선택
print("\n변경할 상태 선택")
print("1. 재학")
print("2. 졸업")

status_num = input("번호 선택: ")

if status_num == "1":
    new_status = "재학"
elif status_num == "2":
    new_status = "졸업"
else:
    print("❌ 잘못된 번호입니다.")
    exit() # 프로그램 종료


# ..............................................
# 8. 상태값만 수정
notion.pages.update(
    page_id=page_id,
    properties={
        "상태" : {
            "select" : { "name" : new_status }
        } 
    }
)

print(f"\n✅ 상태가 '{new_status}'(으)로 수정되었습니다.")

