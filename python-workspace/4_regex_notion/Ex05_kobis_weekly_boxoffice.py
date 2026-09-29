import os
import requests
from dotenv import load_dotenv

# .env 파일을 읽어서 환경변수 불러오기
load_dotenv()

# 영화진흥위원회(KOBIS) 주간 박스오피스 API

# env 파일에서 값 불러오기
MOVIE_BASE_URL = os.getenv("MOVIE_BASE_URL") # 영화진흥위원회(KOBIS)URL주소
MOVIE_API_KEY = os.getenv("MOVIE_API_KEY") # 발급받은_API_키

print(MOVIE_BASE_URL)
print(MOVIE_API_KEY)

if not MOVIE_API_KEY:
    # 키값이 없으면 일부러 예외 발생시킴
    raise ValueError(".env 파일에 MOVIE_API_KEY 값이 없습니다.")

params = {
    "key" : MOVIE_API_KEY,
    "targetDt" : "20260927"
}
response = requests.get(f"{MOVIE_BASE_URL}/searchWeeklyBoxOfficeList.json"
            , params=params
            , timeout=5) # timeout? 서버의 응답을 기다리는 최대 시간(초 단위)을 의미

# 에러 시 즉시 예외 발생, try-except와 함께 사용(정상일땐 아무것도 안뜸)
response.raise_for_status()

print(f"상태 코드 : {response.status_code}") # <Response [200]> -> 정상적으로 응답 받음
print(f"최종 요청 url : {response.url}")
print(f"데이터 형식 : {response.headers.get('Content-Type')}")

data = response.json()
# print(data)
# print(data['boxOfficeResult'])
# print(data['boxOfficeResult']['weeklyBoxOfficeList'])
# print(data['boxOfficeResult']['weeklyBoxOfficeList'][9])

# 위와 같이 데이터 불러와도되지만 없는 키값 부르면 오류남!
# 우리는 get함수 사용하기!! - 없을때 오류 안나고 None 값 나옴
print(data.get('boxOfficeResult'))

# 없을때 빈 값 나오게
box_office = data.get('boxOfficeResult', {}).get('weeklyBoxOfficeList', [])
# print(box_office)

for movie in box_office:
    print(
        f"[{movie.get('rank')}위] "
        f"{movie['movieNm']}\n"
        f"개봉일 - {movie.get('openDt')}"
        f" / 누적관객수 - {movie.get('audiAcc')}"
        f"{movie['audiAcc']} 명"
    )