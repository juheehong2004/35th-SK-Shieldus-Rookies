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

    # get으로 가져와야 오류 안남
    name = page["properties"]["이름"]["title"][0]["plain_text"]
    age = page["properties"]["나이"]["number"]
    status = page["properties"]["상태"]["select"]["name"]

    print(f"{i}. 이름: {name}")
    print(f"   나이: {age}")
    print(f"   상태: {status}")
    print("-" * 30)


'''
견고성 문제
1. 에러 핸들링 없음 — 토큰 만료, DB 미공유(권한) 등 원인이 섞여서 나오면 진단이 어려움
2. 속성 값 접근이 취약함 — title 배열이 비어있거나(제목 미입력), 
    select가 None(값 미선택)이면 IndexError/TypeError로 스크립트 전체가 죽음. 
    실제 운영 DB는 빈 값이 섞여 있기 마련
3. 페이지네이션 누락 — 파일 상단 주석은 "모든 레코드 조회"라고 되어 있지만, 
    data_sources.query()는 기본적으로 최대 100건만 반환합니다. 100건이 넘으면 나머지는 조용히 누락됨

'''