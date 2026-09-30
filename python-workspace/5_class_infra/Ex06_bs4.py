import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_security_news():

    # 현재 보안뉴스 메인 페이지
    url = "https://www.boannews.com/"

    # 보안뉴스 사이트는 헤더 정보 필요없음(보안 약한가봄) - 정상 경로로 접속한건지 확인하는것
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        # ==================================
        # 1. 웹페이지 요청
        # ==================================
        response = requests.get(
            url,
            # headers=headers,
            timeout=10
        )

        # 200 이외 응답 감지해서 알림
        response.raise_for_status()

        print("✅ 연결 성공")
        print("상태 코드:", response.status_code)


        # ==================================
        # 2. HTML 파싱
        # ==================================
        soup = BeautifulSoup(   response.text,  "html.parser"  )

        # print(soup)
        # return

        # ==================================
        # 3. 모든 링크 확인
        # ==================================
        # 웹페이지 html 내용 받아와서 <a> 태그 찾기
        links = soup.find_all("a")

        print("\n" + "=" * 60)
        print("🛡️ 최신 보안 뉴스")
        print("=" * 60)


        count = 0
        # seen_titles = {} 라고 쓰면 빈 딕셔너리 생성됨
        seen_titles = set()

        #--------------------------------------------
        # 여기
        for a in links:
            title = a.get_text
            href = a.get('href')

            # 링크가 없을때는 제외(False + not = True)
            if not href: continue

            # 링크가 보안뉴스 외부 링크 제외
            if "boannews.com" not in href: continue

            # 보안뉴스 내 링크만 남음

            seen_titles.add(title)
            count += 1

            print(f'\n {count}. {title}')
            print(f'🔗 {href}')

            # 10문장 가져오면 정지
            if count == 10: break


        if count == 0:
            print("❌ 뉴스 기사를 찾지 못했습니다.")


    except requests.exceptions.RequestException as e:
        print("❌ 웹사이트 연결 오류")
        print(e)


if __name__ == "__main__":
    get_security_news()