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

print("\n=== 데이터베이스 페이지 목록 ===")

pages = result["results"]

for i, page in enumerate(pages, start=1):

    name = page["properties"]["이름"]["title"][0]["plain_text"]
    age = page["properties"]["나이"]["number"]
    status = page["properties"]["상태"]["select"]["name"]

    print(f"{i}. 이름: {name}")
    print(f"   나이: {age}")
    print(f"   상태: {status}")
    print("-" * 30)


#..............................................
# 6. 삭제할 페이지 번호 입력
delete_num = int(input('삭제할 번호를 입력하세요 ->'))
# print(delete_num)

# 번호에 해당하는 페이지 선택
page_id = pages[delete_num-1]["id"]
# print(page_id) # 3eaed442-e2ce-8122-aeb8-cd71ef2fdb15

#..............................................
# 7. 페이지 삭제
# archived=True : 해당 페이지를 삭제(휴지통으로 이동) 상태로 변경합니다.
notion.pages.update(page_id=page_id, archived=True)

print("\n✅ 페이지가 삭제되었습니다.")