# 3.  포맷별 패턴과 그룹 추출

# ----------------------------------------------------------
## 3-1. 서버 포맷별 추출 패턴
import re

log = "Failed password for admin from 192.168.1.100 port 22 ssh2"

# result = re.search(r"from\s(\d{1,3}(?:\.\d{1,3}){3})", log)
result = re.search(r"from\s(\d+\.\d+\.\d+\.\d+)", log)

print(result.group(1))


# ----------------------------------------------------------
# 3-2. 그룹 다수로 한 번에 뜯어보기
import re

apache_log = '192.168.10.55 - admin [05/Apr/2026:14:20:01 +0900] GET /etc/passwd HTTP/1.1 403 531'

pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s'
    r'-\s(\S+)\s'
    r'\[([^\]]+)\]\s'
    r'(\S+)\s(\S+)\sHTTP/[\d.]+\s'
    r'(\d{3})\s'
    r'(\d+)'
)

m = pattern.search(apache_log)
if m:
    print(f"{m.group(0)}") # 192.168.10.55 - admin [05/Apr/2026:14:20:01 +0900] GET /etc/passwd HTTP/1.1 403 531
    print(f"IP: {m.group(1)}")
    print(f"사용자: {m.group(2)}")
    print(f"타임스탬프: {m.group(3)}")
    print(f"메서드: {m.group(4)}, 경로: {m.group(5)}")
    print(f"상태 코드: {m.group(6)}, 전송 크기: {m.group(7)}바이트")



#---------------------------------------------------
# 3-3. 보안 로그용 필수 패턴 모음
