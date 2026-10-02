'''
[파이썬 PBL 기본-1] 방화벽 패킷 손실률 실시간 모니터링
'''

# 1. 데이터 준비
import random

line_names = [f'LINE-{i:02d}' for i in range(1, 13)] # 문제 제공 데이터, 아래에서 사용되지는 않음
# 정상 데이터와 비정상/예외 데이터를 섞어서 테스트 데이터 생성
raw_logs = [random.randint(1, 100) for _ in range(10)] + [0, "Timeout", None, 99, "Error"]
random.shuffle(raw_logs) # 리스트 내 요소 무작위로 섞음(원본 리스트 바뀜)

# 2. 반복 구조 설계
print("--- 실시간 네트워크 트래픽 점검 시작 ---")
processed_logs = [] # 예외 없이 정상적으로 처리된 값을 저장하기위한 리스트

# 각 로그를 하나씩 확인하며 손실률에 따라 상태 판정
for log in raw_logs:
    # 3. 에러 가드 설치
    try:
        # 문자열 등 입력값을 실수형으로 변환
        float_log = float(log)

        # 4. 조건 우선순위 설정
        # 가장 위험한 99% 이상을 먼저 확인하고 이후 낮은 기준을 검사
        if float_log >= 99:
            print(f'🚨 [EMERGENCY] {float_log}% 감지! 대규모 DDoS 공격 의심으로 전체 점검 중단!')
            break
        elif float_log >= 95:
            print(f'🔴 [CRITICAL] 패킷 손실률 {float_log}%: 즉시 회선 차단 및 우회 경로 전환')
        elif float_log >= 70:
            print(f'🟡 [WARNING] 패킷 손실률 {float_log}%: 관리자 호출 및 회선 점검 필요')
        elif float_log == 0:
            print(f'⚪ [CHECK] 패킷 손실률 {log}%: 트래픽 없음 (회선 다운 의심)')
        else:
            print(f'🟢 [NORMAL] 패킷 손실률 {float_log}%: 회선 정상')

         # 예외 없이 정상적으로 처리된 값만 결과 리스트에 저장
        processed_logs.append(float_log)

    # 5. 예외 핸들링
    except (ValueError, TypeError):
        # 숫자로 변환할 수 없는 데이터는 오류 메시지만 출력하고 다음 로그로 진행
        print(f'❌ [DATA ERROR] 읽을 수 없는 로그 형식입니다. (입력값: {log})')
        continue

    # 6. 공통 마감 출력
    # 정상 처리/예외 여부와 관계없이 점검 완료 메시지 출력
    finally:
        print(f'{"-"*15} 점검 완료 {"-"*15}')


# 7. 요약 출력
# 정상적으로 처리된 값들 중 70이상인 값만 List Comprehension으로 추출
warning_logs = [log for log in processed_logs if log >= 70] 
print(f'\n[요약] 위험(WARNING 이상) 손실률 목록: {warning_logs}')