# 2-1. 기본 문법 — HTTP 응답 코드 분기
status_code = 403

match status_code:
    case 200:
        print("[SUCCESS] 정상 응답")
    case 401 | 403:
        print("[WARNING] 인증/권한 오류 - 무단 접근 시도 가능성")
    case 500:
        print("[CRITICAL] 서버 내부 오류")
    case _:
        print(f"[UNKNOWN] 처리되지 않은 상태 코드: {status_code}")

print()
# 2-2. | 연산자 — 여러 프로토콜을 하나의 그룹으로 묶기
protocol = "SFTP"

match protocol:
    case "HTTP" | "HTTPS":
        print("웹 트래픽 - 표준 정책 적용")
    case "SSH" | "SFTP":
        print("원격 관리 접속 - 강화된 MFA 정책 적용")
    case _:
        print("기타 트래픽 - 기본 차단 정책 적용")

print()
# 2-3. (심화) 구조 매칭 — 방화벽 로그 파싱
fw_log = ["DENY", "TCP", "203.0.113.55", 6379]

match fw_log:
    case ["DENY", proto, ip, port]:
        print(f"[차단 기록] {proto} {ip}:{port} - 정책 위반으로 차단됨")
    case ["ALLOW", proto, ip, port]:
        print(f"[허용 기록] {proto} {ip}:{port}")
    case _:
        print(f"알 수 없는 로그 형식: {fw_log}")

print()
# ============================================
'''
문제 1  —
    scan_result = "TIMEOUT" 변수가 있습니다. 
    "OPEN"이면 "포트 열림", "CLOSED"이면 "포트 닫힘", "TIMEOUT"이면 "응답 없음 - 방화벽 의심", 
    그 외에는 "알 수 없음"을 출력하는 match-case를 작성해 봅시다.
'''
scan_result = "TIMEOUT"

match scan_result:
	case "OPEN":
		print("포트 열림")
	case "CLOSED":
		print("포트 닫힘")
	case "TIMEOUT":
		print("응답 없음 - 방화벽 의심")
	case _:
		print("알 수 없음")

print()
'''
문제 2 — 
    method = "DELETE" 변수가 있습니다. 
    |연산자를 사용해서 "GET" 또는 "HEAD"이면 "읽기 요청 - 허용",
    "POST" 또는 "PUT" 또는 "DELETE"이면 "쓰기 요청 - 권한 확인 필요"를 출력하는 코드를 작성해 봅시다.
'''
method = "DELETE"

match method:
	case "GET" | "HEAD":
		print("읽기 요청 - 허용")
	case "POST" | "PUT" | "DELETE":
		print("쓰기 요청 - 권한 확인 필요")

print()
''' 
문제 3  — 
    login_event = ["LOGIN_FAIL", "admin", "203.0.113.55"] 형태의 리스트가 있습니다. 
    구조 매칭으로 ["LOGIN_FAIL", user, ip] 패턴이면 "로그인 실패 감지: admin (203.0.113.55)", ["LOGIN_OK", user, ip] 패턴이면 "정상 로그인: admin"을 출력하고, 
    그 외 패턴은 case _로 처리하는 코드를 작성해 봅시다.
'''
login_event = ["LOGIN_FAIL", "admin", "203.0.113.55"]

match login_event:
	case ["LOGIN_FAIL", user, ip]:
		print(f'로그인 실패 감지: {user}({ip})')
	case ["LOGIN_OK", user, ip]:
		print(f'정상 로그인: {user}')
	case _:
		print(f'로그인 이상 감지')

