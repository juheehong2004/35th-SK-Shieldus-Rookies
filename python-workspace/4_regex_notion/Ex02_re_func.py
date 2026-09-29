# 2. re 모듈 주요 함수 — search · match · findall · compile

# 2-1. re.search() — 문자열 어디든 일치하는 첫 지점 반환
import re

log_line = "192.168.0.1 - - [05/Apr/2026] GET /etc/passwd 403"

match = re.search(r"/etc/passwd", log_line)
if match:
    print(f"[위험] 민감 파일 접근 시도 감지: {match.group()}") # [위험] 민감 파일 접근 시도 감지: /etc/passwd


#-------------------------------------------
# 2-2. re.match() — 문자열의 시작부터 일치하는지 확인
import re

log_line = "[ERROR] Unauthorized access attempt from 192.168.0.1"

# [] 대괄호를 문자로 인식시키려면 \ 앞에 붙여야함
pattern = r"\[ERROR\]" # 보안 위협 로그입니다: [ERROR]
# pattern = r"[ERROR]" # ERROR로 시작하는 로그가 아닙니다
m = re.match(pattern, log_line)

if m:
    print(f"보안 위협 로그입니다: {m.group()}")
else:
    print("ERROR로 시작하는 로그가 아닙니다")

#-------------------------------------------
# 2-3. re.findall() — 일치하는 모든 부분을 리스트로 반환
import re

text = "요청1 처리결과: 200, 요청2 처리결과: 404, 요청3 처리결과: 500"

# codes = re.findall(r"\d{3}", text) # 추출된 상태 코드 목록: ['200', '404', '500']
codes = re.search(r"\d{3}", text) # 추출된 상태 코드 목록: <re.Match object; span=(10, 13), match='200'>
print(f"추출된 상태 코드 목록: {codes}")


#-----------------------------------------------
# 2-4. re.compile() — 대용량 로그 반복 검사를 위한 사전 컴파일
import re

ip_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

logs = ["1.1.1.1 GET ...", "invalid line", "2.2.2.2 POST ..."]

for line in logs:
    if ip_pattern.search(line):
        print(f"IP 발견: {line}")
