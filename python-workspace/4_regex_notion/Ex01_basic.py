# 1. 정규표현식 문법 기초 

# 1-1. 문자, 숫자 매치
import re

# log_line = "203.0.113.55 - admin [05/Apr/2026:14:20:01] GET /etc/passwd HTTP/1.1 403 531"
log_line = "admin GET /etc/passwd HTTP"

# \d : 숫자 하나, \w : 문자/숫자 매치 하나, \s : 공백 문자
has_digit = re.search(r"\d", log_line) # r : \뒤의 문자를 그대로로 받아들이겠다라는 의미
print(has_digit)
print("-"*30)

first_word =  re.search(r"\w+", log_line)


print(f"숫자 포함 여부: {bool(has_digit)}") # True
print(f"첫 번째 문자 매치: {first_word.group()}") # 203 (r"\w" 로 매칭하면 2 로 출력됨)
                                                # admin




# 1-2. 반복 횟수 지정 (길이 조절)
import re

status_line = "GET /index.html HTTP/1.1 200 1024"

# \d{3} : 숫자가 정확히 3자리 인 걸 매칭 (HTTP 상태 코드 자릿수)
match = re.search(r"\d{3}", status_line)
if match:
    print(f"상태 코드 후보: {match.group()}")

# https? : s가 0번 또는 1번 나올 수 있음 (http/https 둘 다 허용)
internal_url = "http://api.internal.company.com/v1/alerts"
internal_url = "https://api.internal.company.com/v1/alerts"
internal_url = "ftp://api.internal.company.com/v1/alerts"

# http or https 있으면
if re.search(r"https?://", internal_url):
    print("정상적인 http url 입니다")


# 1-3. 위치 · 범위 · 그룹 · OR 연산자
import re

auth_log = "Failed password for root from 211.23.45.10 port 54321 ssh2"

# ( | ) : 여러 값 중 하나라도 일치하면 매칭 (OR)
if re.search(r"(admin|root)", auth_log):
    print("[경고] 관리자급 계정을 대상으로 한 로그인 시도 감지")

# ^ : 문자열의 시작, $ : 문자열의 끝
release_tag = "2026-04-05-hotfix"
if re.match(r"^2026-", release_tag):
    print("2026년도 릴리스 태그입니다")

# [ ] 문자 집합, - 범위, [^] 부정(그 문자들이 아닌 것)
password_candidate = "P@ssw0rd!"
if re.search(r"[^a-zA-Z0-9]", password_candidate):
    print("특수문자가 포함되어 비밀번호 정책을 만족합니다")

password_candidate = "passw0rd"
if re.search(r"[^a-z0-9]", password_candidate):
    print("특수문자가 포함되어 비밀번호 정책을 만족합니다")

password_candidate = "피assw0rd"
# 한글 매치는 ㄱ-힣
if re.search(r"[^a-zA-Z0-9ㄱ-힣]", password_candidate):
    print("특수문자가 포함되어 비밀번호 정책을 만족합니다")


# re.search() vs re.match() 
import re

log_line = "ERROR: Login failed from 192.168.1.100"

# search()
result = re.search(r"Login", log_line)
print(result.group())   # Login

# match()
result = re.match(r"Login", log_line)
print(result)            # None


log_line2 = "PREFIX 2026-09-16 ERROR Login failed"

# 1. match()는 문자열 시작 부분이 '2026'이 아니므로 실패
print(re.match(r"2026", log_line2))   # None

# 2. search()는 위치 상관없이 '2026'을 찾아냄
print(re.search(r"2026", log_line2))  # <re.Match object; span=(7, 11), match='2026'>

# 3. search()에 ^를 붙이면 맨 앞만 검사하게 되므로 실패
print(re.search(r"^2026", log_line2)) # None