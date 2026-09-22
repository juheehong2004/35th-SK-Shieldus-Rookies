
## 7-1. 기본 try-except
# 점검할 서버 대수를 입력하세요: 10
# 점검할 서버 대수를 입력하세요: a # 문자 입력 시 예외 발생

try:
    num_hosts = int(input("점검할 서버 대수를 입력하세요: ")) 
    per_thread = 100 / num_hosts
    print(f"스레드당 할당량: {per_thread:.1f}")
except:
    print("[경고] 숫자만 입력하세요.")

print()

## 7-2. 구체적인 예외 처리

total_host = 1
patched_hosts = 3




print()

## 7-3. else와 finally

try:
    print("데이터베이스 연결 시도...")
except Exception as e: # 예외 발생시 실행  
    print("연결 실패!")
else: # 예외가 없을 때만 실행
    print("연결 성공 - 감사 쿼리를 실행합니다")  
finally: # 예외발생 여부(성공/실패 여부)와 무관하게 항상 실행(앞에서 return 수행되도 finally는 반드시 실행됨)
    print("연결 시도 로그를 서버에 기록하고 종료합니다") # ex) 네트워크 닫을때 등

print("프로그램 정상 종료")


print()
#============================================
'''
문제 1  — 
    port_input = "abc" 문자열을 int()로 변환하려고 합니다. 
    변환에 실패하면 "숫자로 된 포트 번호를 입력하세요"를 출력하는 try-except를 작성해 봅시다.
'''
try:
    port_input = "abc"
    print(int(port_input))
except:
    input("숫자로 된 포트 번호를 입력하세요: ")


'''
문제 2 — 
    아래 vuln 딕셔너리에서 "remediation" 키를 조회하려고 합니다. 
    해당 키가 없으면 KeyError를 잡아서 "조치 방안이 아직 등록되지 않았습니다"를 출력해 봅시다.

    vuln = {"cve_id": "CVE-2026-22221", "cvss": 7.4}
 
'''

vuln = {"cve_id": "CVE-2026-22221", "cvss": 7.4}

try:
    search = vuln["remediation"]
    print(f'조회 결과: {search}')
except KeyError as e:
    print(f"조회 실패! : {e} - 조치 방안이 아직 등록되지 않았습니다")
   
