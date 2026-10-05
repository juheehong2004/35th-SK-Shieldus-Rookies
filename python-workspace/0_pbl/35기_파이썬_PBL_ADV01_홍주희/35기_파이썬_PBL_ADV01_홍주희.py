'''
[파이썬 PBL 응용-1] 노션 API 기반 서버 자산 관리 CLI 구축
    - 정규표현식 입력 검증과 notion-client SDK를 활용한 대화형 서버 자산 CRUD 관리 자동화 구현
'''
# ======================================================================
# 1. 환경 설정 및 API 인증
# ======================================================================
import os
import re
from dotenv import load_dotenv, set_key, find_dotenv
from notion_client import Client, APIResponseError


# .env 파일을 읽어 환경변수로 등록
load_dotenv()

# 필수 환경변수
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID")

# 필수 값이 없으면 API 호출이 불가능하므로 시작 단계에서 바로 중단
if NOTION_TOKEN is None or PARENT_PAGE_ID is None:
    raise RuntimeError(
        "NOTION_TOKEN 또는 NOTION_PARENT_PAGE_ID가 설정되어 있지 않습니다."
    )

# set_key로 값을 추가할 .env 파일 경로
DOTENV_PATH = find_dotenv()

# Notion 클라이언트
notion = Client(auth=NOTION_TOKEN)

# 허용하는 태그 목록
TAG_OPTIONS = ["Web", "DB", "WAS", "Cache"]


# ======================================================================
# 2. 데이터 유효성 검증 (Regex)
# ======================================================================
# 호스트명 : srv-(web|db|was|cache)-숫자 2자리    예) srv-web-01
HOSTNAME_PATTERN = re.compile(r"^srv-(web|db|was|cache)-\d{2}$")

# IP 주소 : 1~3자리 숫자 4개를 점(.)으로 구분   예) 192.168.0.10
#           (형식만 확인하며, 0~255 범위는 validate_ip에서 확인)
IP_PATTERN = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")

# 포트 번호 : 1~5자리 숫자
#             (형식만 확인하며, 1~65535 범위는 validate_port에서 확인)
PORT_PATTERN = re.compile(r"^\d{1,5}$")

# 호스트명 검증
def validate_hostname(value: str) -> bool:
    """호스트명이 srv-{web|db|was|cache}-NN 형식이면 True"""
    return bool(HOSTNAME_PATTERN.match(value))

# IP 주소 검증
def validate_ip(value: str) -> bool:
    """IPv4 형식이면서 각 자리가 0~255 범위이면 True (예: 300.1.1.1은 False)"""
    if not IP_PATTERN.match(value):
        return False
    # 정규식은 '999' 같은 값도 통과시키므로 범위를 따로 검사
    return all(0 <= int(octet) <= 255 for octet in value.split("."))

# 포트 번호 검증
def validate_port(value: str) -> bool:
    """숫자이면서 1~65535 범위이면 True (예: 70000은 False)"""
    if not PORT_PATTERN.match(value):
        return False
    # 정규식은 '99999' 같은 값도 통과시키므로 범위를 따로 검사
    return 1 <= int(value) <= 65535


# ======================================================================
# 3. Notion 데이터베이스 스키마 설계
# ======================================================================
def create_server_database():
    """
    부모 페이지 아래에 '서버 자산 대장' 데이터베이스를 생성하고
    Data Source ID를 반환한다.
    """

    # 데이터베이스 제목
    title = [
        {
            "type": "text",
            "text": {
                "content": "서버 자산 대장"
            }
        }
    ]

    # 컬럼 정의
    properties = {

        # 제목 컬럼 (DB에는 title 속성이 반드시 하나 필요)
        "호스트명": {
            "title": {}
        },

        "IP주소": {
            "rich_text": {}
        },

        "포트": {
            "number": {
                "format": "number"
            }
        },

        # 단일 선택 : 서버 운영 상태
        "상태": {
            "select": {
                "options": [
                    {"name": "Active"},
                    {"name": "Maintenance"},
                    {"name": "Decommissioned"},
                ]
            }
        },

        # 다중 선택 : 서버 역할 (여러 개 지정 가능)
        "태그": {
            "multi_select": {
                "options": [
                    {"name": "Web"},
                    {"name": "DB"},
                    {"name": "WAS"},
                    {"name": "Cache"},
                ]
            }
        },
    }

    # DB 생성
    db = notion.databases.create(
        parent={
            "type": "page_id",
            "page_id": PARENT_PAGE_ID,
        },

        title=title,

        initial_data_source={
            "properties": properties
        },
    )

    database_id = db["id"]

    # 생성된 DB에서 Data Source ID 가져오기
    db_info = notion.databases.retrieve(database_id)
    data_source_id = db_info["data_sources"][0]["id"]

    print("새 데이터베이스 생성 완료!")

    return data_source_id


# ======================================================================
# 4. Notion API 기반 CRUD 로직(조회/생성/수정/삭제)
# ======================================================================

# 조회 : 현재 데이터베이스에 등록된 모든 서버의 호스트명, IP, 포트, 상태, 태그를 번호와 함께 출력
def show_servers(data_source_id: str):
    """
    서버 목록을 번호와 함께 출력하고 페이지 목록(list)을 반환한다.
    반환값은 수정·삭제 시 '출력한 번호 → 실제 페이지'를 연결하는 데 쓰인다.
    """

    response = notion.data_sources.query(
        data_source_id=data_source_id
    )

    pages = response["results"]

    # 등록된 서버가 없으면 빈 리스트를 반환 (호출한 쪽에서 `if not pages`로 중단)
    if not pages:
        print("\n등록된 서버가 없습니다.")
        return pages

    print("\n===== 서버 목록 =====")

    # 목록 번호는 1부터 시작
    for num, page in enumerate(pages, start=1):

        properties = page["properties"]

        # 각 속성 타입에 맞는 위치에서 값을 꺼낸다
        #   title / rich_text : 리스트의 첫 요소의 plain_text
        #   number            : 값 그대로
        #   select            : 선택된 옵션의 name
        #   multi_select      : 옵션 리스트 → 이름만 뽑아 쉼표로 연결
        hostname = properties["호스트명"]["title"][0]["plain_text"]
        ip = properties["IP주소"]["rich_text"][0]["plain_text"]
        port = properties["포트"]["number"]
        status = properties["상태"]["select"]["name"]
        tags = ", ".join([tag["name"] for tag in properties["태그"]["multi_select"]])

        print(f"{num}. {hostname} | {ip} | {port} | {status} | {tags}")

    return pages


# 번호로 서버 선택 (입력 번호가 목록 범위 안에 있는지 검증)
def select_page(pages: list, message: str):
    """
    사용자에게 번호를 입력받아 해당 페이지를 반환한다.
    숫자가 아니거나 범위를 벗어나면 경고 후 None을 반환한다.
    """

    # 숫자가 아닌 값(문자 등)이 들어오면 int()에서 ValueError 발생
    try:
        num = int(input(message))
    except ValueError:
        print("\n❌ 숫자를 입력하세요.")
        return None

    # 목록 범위(1 ~ 서버 개수) 검증
    if num < 1 or num > len(pages):
        print(f"\n❌ 1 ~ {len(pages)} 사이의 번호를 입력하세요.")
        return None

    # 화면 번호는 1부터, 리스트 인덱스는 0부터 시작하므로 -1
    return pages[num - 1]


# 생성 : 호스트명, IP 주소, 포트, 태그를 입력받아 데이터베이스에 페이지를 추가하며, 신규 등록 시 상태는 'Active'로 고정
def create_server(data_source_id: str):
    """
    서버 정보를 입력받아 정규표현식으로 검증한 뒤 DB에 새 페이지로 등록한다.
    검증에 실패하면 경고만 출력하고 API를 호출하지 않은 채 메뉴로 돌아간다.
    """

    print("\n===== 신규 서버 등록 =====")

    # 입력값 검증 : 하나라도 틀리면 경고 후 메뉴로 복귀
    hostname = input("호스트명 (예: srv-web-01): ").strip()
    if not validate_hostname(hostname):
        print("\n❌ 호스트명 형식이 올바르지 않습니다. (예: srv-web-01)")
        return

    ip = input("IP 주소 (예: 192.168.0.10): ").strip()
    if not validate_ip(ip):
        print("\n❌ IP 주소 형식이 올바르지 않습니다. (각 자리는 0~255)")
        return

    port = input("포트 번호 (1~65535): ").strip()
    if not validate_port(port):
        print("\n❌ 포트 번호는 1~65535 사이의 숫자여야 합니다.")
        return

    # 태그 : 쉼표로 구분해 리스트로 만들고, 허용 목록에 있는 값인지 확인
    tags_input = input("태그 (Web / DB / WAS / Cache, 여러 개는 쉼표로 구분): ")
    tags = [tag.strip() for tag in tags_input.split(",")]

    for tag in tags:
        if tag not in TAG_OPTIONS:
            print(f"\n❌ 허용되지 않은 태그입니다: {tag}")
            return

    # 모든 검증을 통과한 경우에만 노션에 페이지(행) 추가
    notion.pages.create(
        parent={
            "data_source_id": data_source_id
        },
        properties={
            "호스트명": {
                "title": [{"text": {"content": hostname}}]
            },
            "IP주소": {
                "rich_text": [{"text": {"content": ip}}]
            },
            "포트": {
                "number": int(port)
            },
            "상태": {
                "select": {"name": "Active"}   # 신규 등록 시 상태는 Active로 고정
            },
            "태그": {
                "multi_select": [{"name": tag} for tag in tags]
            },
        }
    )

    print(f"\n✅ 서버 등록 완료: {hostname} ({ip}:{port})")


# 수정 : 특정 서버를 번호로 선택하고 상태를 Active/Maintenance/Decommissioned 중 하나로 덮어쓰기
def update_server_status(data_source_id: str):
    """목록에서 서버를 번호로 선택하고, 상태(select)를 새 값으로 덮어쓴다."""

    # 목록을 먼저 보여주고, 서버가 없으면 바로 종료
    pages = show_servers(data_source_id)
    if not pages:
        return

    # 번호가 잘못되면 select_page가 경고를 출력하고 None 반환
    page = select_page(pages, "\n상태를 변경할 서버 번호를 입력하세요: ")
    if page is None:
        return

    print("\n변경할 상태 선택")
    print("1. Active")
    print("2. Maintenance")
    print("3. Decommissioned")

    status_num = input("번호 선택: ")

    # 입력한 번호를 상태 문자열로 변환 (1~3 이외는 거부)
    if status_num == "1":
        new_status = "Active"
    elif status_num == "2":
        new_status = "Maintenance"
    elif status_num == "3":
        new_status = "Decommissioned"
    else:
        print("\n❌ 1, 2, 3 중에서 선택하세요.")
        return

    # 선택한 페이지의 '상태' 속성만 덮어쓰기 (다른 속성은 그대로 유지)
    notion.pages.update(
        page_id=page["id"],
        properties={
            "상태": {
                "select": {
                    "name": new_status
                }
            }
        }
    )

    print(f"\n✅ 상태가 '{new_status}'(으)로 변경되었습니다.")


# 삭제 : 선택한 서버를 노션 휴지통으로 이동
def delete_server(data_source_id: str):
    """목록에서 서버를 번호로 선택해 노션 휴지통으로 이동(보관 처리)한다."""

    pages = show_servers(data_source_id)
    if not pages:
        return

    page = select_page(pages, "\n폐기할 서버 번호를 입력하세요: ")
    if page is None:
        return

    # archived=True : 해당 페이지를 삭제(휴지통으로 이동) 상태로 변경
    # (완전 삭제가 아니므로 노션 휴지통에서 복구 가능)
    notion.pages.update(
        page_id=page["id"],
        archived=True
    )

    print("\n✅ 서버가 폐기(휴지통 이동)되었습니다.")


# ======================================================================
# 메인
# ======================================================================
if __name__ == "__main__":
    # 이전 실행에서 저장해 둔 Data Source ID를 .env에서 읽어온다
    data_source_id = os.getenv("SERVER_DATA_SOURCE_ID")

    # 찾는 키값이 .env 파일에 없다면 DB 생성 후 .env에 영구 저장
    # (다음 실행부터는 DB를 새로 만들지 않고 저장된 ID를 재사용)
    if data_source_id is None:
        try:
            data_source_id = create_server_database()
        except APIResponseError as e:
            # DB 생성에 실패하면 이후 메뉴를 사용할 수 없으므로 종료
            print(f"\n❌ 데이터베이스 생성 실패: {e}")
            exit()

        set_key(DOTENV_PATH, "SERVER_DATA_SOURCE_ID", data_source_id, quote_mode="never")

    # ======================================================================
    # 5. 대화형 인터페이스 및 예외 처리
    # ======================================================================
    
    # 0을 입력할 때까지 메뉴를 반복해서 보여준다
    while True:
        print("\n===== 서버 자산 관리 메뉴 =====")
        print("1. 전체 서버 목록 조회")
        print("2. 신규 서버 등록")
        print("3. 서버 상태 변경 (Active / Maintenance / Decommissioned)")
        print("4. 서버 폐기")
        print("0. 프로그램 종료")

        choice = input("\n메뉴 번호를 입력하세요: ")

        # Notion API 호출 중 오류가 나도 프로그램이 종료되지 않도록 처리
        try:
            if choice == "1":
                show_servers(data_source_id)

            elif choice == "2":
                create_server(data_source_id)

            elif choice == "3":
                update_server_status(data_source_id)

            elif choice == "4":
                delete_server(data_source_id)

            elif choice == "0":
                print("\n프로그램을 종료합니다.")
                break

            else:
                print("\n❌ 0 ~ 4 중에서 선택하세요.")

        # 노션 서버가 돌려준 오류
        except APIResponseError as e:
            print(f"\n❌ Notion API 오류가 발생했습니다: {e}")

        # 그 외 오류 - 오류 메시지만 출력하고 메뉴로 돌아가 프로그램이 강제 종료되지 않도록 한다.
        except Exception as e:
            print(f"\n❌ 네트워크 또는 예상치 못한 오류가 발생했습니다: {e}")