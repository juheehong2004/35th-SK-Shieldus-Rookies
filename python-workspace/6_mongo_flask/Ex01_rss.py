import feedparser
import time
import requests
from datetime import datetime

# 보안 뉴스 RSS 주소
# 전체기사: https://www.boannews.com/rss/allArticle.xml
# 인기기사: https://www.boannews.com/rss/clickTop.xml
# 사건·사고: https://www.boannews.com/rss/S1N2.xml
# 공공·정책: https://www.boannews.com/rss/S1N3.xml
# 비즈니스: https://www.boannews.com/rss/S1N4.xml
rss_url = "https://www.boannews.com/rss/clickTop.xml"

feed = feedparser.parse(rss_url)
print(feed.entries)

news_list = feed.entries[:10]
print(news_list[0])
print("-"*40)

for news in news_list:
    print(f'제목 : {news.title}')
    print(f'링크 : {news.link}')

    # 1. 기존 문자열('2026-09-30 16:03:49')을 datetime 객체로 변환
    dt = datetime.strptime(news.published, "%Y-%m-%d %H:%M:%S")

    # 2. 원하는 형태로 포맷팅
    # 형태 : 2026년 09월 30일 16시 03분
    formatted_date = dt.strftime("%Y년 %m월 %d일 %H시 %M분")

    # 출력
    print(f'게시일 : {formatted_date}')



