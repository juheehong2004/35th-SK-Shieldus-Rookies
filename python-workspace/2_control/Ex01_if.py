# — 로그인 실패 임계치 판정
failed_login_count = int( input('로그인 실패 횟수를 입력하세요-> '))

if failed_login_count >= 8:
    print(f"[경고] 실패 횟수 {failed_login_count}회 - 계정 잠금 정책 발동 대상입니다")



print()

# — 인증서 만료 임박 판정

cert_days_left = int( input('인증서 만료 남은 일을 입력하세요-> '))

if cert_days_left <= 7:
    print(f"[경고] TLS 인증서가 {cert_days_left}일 후 만료됩니다. 즉시 갱신하세요")
else:
    print(f"[정상] 인증서 만료까지 {cert_days_left}일 남았습니다")




print()

# — CVSS 점수 기반 심각도 등급 분류
# |       점수 | 위험도 |
# | ---------: | ---   |
# |        0.0 | 없음  |
# |  0.1 ~ 3.9 | 낮음  |
# |  4.0 ~ 6.9 | 중간  |
# |  7.0 ~ 8.9 | 높음  |
# | 9.0 ~ 10.0 | 치명적 |

    
    
cvss_score = 8.1

if cvss_score >= 9.0:
    severity = "CRITICAL"
elif cvss_score >= 7.0:
    severity = "HIGH"
elif cvss_score >= 4.0:
    severity = "MEDIUM"
else:
    severity = "LOW"

print(f"CVSS {cvss_score} -> 등급: {severity}")






print()

# 불리언으로 처리되는 조건
# failed_login = True
# failed_login = False
# failed_login = 3 # 파이썬은 숫자 들어오면 True 처리(딴, 0은 False)
# failed_login = 0 # 파이썬 0은 False
failed_login = -1 # 0 제외 True 취급

if failed_login:
    print(f"로그인 실패 {failed_login}회 - 계정 확인 필요") # True, 3, -1
else:
    print("로그인 실패 없음 - 정상") # False, 0


word = "korea"
if(word.find('k')): # find()는 'k'의 인덱스가 나옴
    print(f'k는 {word}에 포함') # true 일줄 알았는데 아님 -> 인덱스 0이기때문에 false 취급됨

if(word.find('b')): # 없는 글자 찾으면 -1 반환
    print(f'k는 {word}에 포함') # find 해서 없으면 -1 반환 -> true 취급됨




print()

#============================================
# [ 연습문제 ]
'''
[ 문제 1 ] 
    변수 failed_count = 15가 있습니다. 
    값이 10 이상이면 "계정 잠금 필요", 아니면 "정상"을 출력하는 코드를 작성해 봅시다.

'''
failed_count = 15

if(failed_count >= 10):
    print("계정 잠금 필요")
else:
    print("정상10")


print()
'''
[ 문제 2 ] 
    patched = False, cvss_score = 9.2 두 변수가 있습니다. 
     패치가 안 되어 있으면서 CVSS가 9.0 이상이면 "즉시 패치 필요", 
     패치는 안 됐지만 CVSS가 9.0 미만이면 "패치 예정", 
     이미 패치되어 있으면 "조치 완료"를 출력하는 if-elif-else를 작성해 봅시다.
'''
patched = False
cvss_score = 9.2

if(patched == False):
    if(cvss_score >= 9.0): 
        print("즉시 패치 필요")
    elif(cvss_score < 9.0):
        print("패치 예정")
else:
    print("조치 완료")


print()
'''
[문제 3  ]
  open_port = 6379, approved_ports = {22, 80, 443} (허용 포트 Set)가 있습니다.
   open_port가 approved_ports에 포함되어 있지 않으면 
   "비인가 포트 감지: 6379"를 출력하는 코드를 in 연산자로 작성해 봅시다.
'''
open_port = 6379
approved_ports = {22, 80, 443}

if(open_port not in approved_ports):
    print(f'비인가 포트 감지: {open_port}')
