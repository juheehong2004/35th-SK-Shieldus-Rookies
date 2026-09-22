## 5-1. while 기본 — 서비스 기동 대기 시뮬레이션

status = "Starting"
check_count = 0

while status != "Running":
    check_count += 1
    print(f'서비스 상태 확인 중... ({check_count}번째 시도)')
    if check_count >= 3:
        status = "Running" # 3번째 확인에서 정상 가동 확인 (예시용)

print("")







print()
# ============================================
'''
[ 문제 1 ] — 
    count = 0에서 시작해서, count가 5 미만인 동안 "재시도 중... (count)"를 출력하고 
    count를 1씩 증가시키는 while문을 작성해 봅시다.
'''
count = 0

while count < 5:
    print(f'재시도 중... {count}')
    count += 1

print()
'''
[ 문제 2 ] — 
    포트 스캔 재시도 로직입니다. 
    max_retry = 5, attempt = 0에서 시작해서, attempt가 max_retry 미만인 동안 반복하면서 
    매번 attempt를 1 증가시키고 "스캔 시도 {attempt}회"를 출력합니다. 
    반복이 끝난 뒤에는 "최대 재시도 횟수 초과 - 스캔 실패 처리"를 출력해 봅시다.
'''
max_retry = 5
attempt = 0

while attempt < max_retry:
    attempt += 1
    print(f'스캔 시도 {attempt}회')

print(f'최대 재시도 횟수 초과 - 스캔 실패 처리')

print()
'''
[ 문제 3 ] — 
    계정 잠금 해제까지 남은 시간(lockout_ttl = 5, 초 단위)을 표현해 봅시다. 
    lockout_ttl이 0보다 큰 동안 "잠금 해제까지 {lockout_ttl}초"를 출력하고 1씩 감소시키다가, 
    0이 되면 반복문을 빠져나와 "계정 잠금이 해제되었습니다"를 출력해 봅시다.
'''
loctout_ttl = 5

while loctout_ttl > 0:
    print(f'잠금 해제까지 {loctout_ttl}초')
    loctout_ttl -= 1

print("계정 잠금이 해제되었습니다")
