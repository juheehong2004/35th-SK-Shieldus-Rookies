'''
[ 연습문제 ]

    #### **CPU 위험 등급 판단 함수** — 기본 함수 + `return`
    
    **이 함수는 무엇을 하나요?**
    
    서버 이름(`server_name`)과 CPU 사용률(`cpu`)을 받아서, 사용률에 따라 등급 메시지를 **반환**하는 함수입니다.
    
    - 90 이상              → `"🔴 위험"`
    - 70 이상 90 미만 → `"🟡 주의"`
    - 70 미만              → `"🟢 정상"`
    
    **아래처럼 호출하면 이런 결과가 나옵니다.**
    print(get_cpu_grade("prd-web-01", 95))   # [prd-web-01] 🔴 위험 (95%)
    print(get_cpu_grade("prd-db-02",  73))   # [prd-db-02]  🟡 주의 (73%)
    print(get_cpu_grade("stg-api-03", 40))   # [stg-api-03] 🟢 정상 (40%)
    
    **함수 구조를 완성하세요.**
    def get_cpu_grade(server_name, cpu):
        """서버 이름과 CPU 사용률을 받아 위험 등급 메시지를 반환하는 함수"""
        # pass를 지우고 여기에 작성하세요
        pass
'''

def get_cpu_grade(server_name, cpu):
    """서버 이름과 CPU 사용률을 받아 위험 등급 메시지를 반환하는 함수"""
    danger_grade = ''
    if cpu >= 90:
          danger_grade = "🔴 위험"
    elif cpu < 90 and cpu >= 70:
          danger_grade = "🟡 주의"
    elif cpu < 70:
        danger_grade = "🟢 정상"

    return f"[{server_name}] {danger_grade} ({cpu}%)"

print(get_cpu_grade("prd-web-01", 95))   # [prd-web-01] 🔴 위험 (95%)
print(get_cpu_grade("prd-db-02",  73))   # [prd-db-02]  🟡 주의 (73%)
print(get_cpu_grade("stg-api-03", 40))   # [stg-api-03] 🟢 정상 (40%)
    





'''
[ 연습 문제 ]

—  간단한 보안 리포트 생성

1. 포트 번호 리스트 `raw_data = [22, 80, 443, 8080, 21]` 가 있습니다.
2. `filter`와 `lambda`를 사용해 100번 미만의 잘 알려진 포트만 골라주세요.
3. `map`과 `lambda`를 사용해 골라낸 포트 뒤에 `":OPEN"` 문구를 붙여주세요.
4. 마지막으로 최종 결과를 리스트로 출력하세요.
'''

raw_data = [22, 80, 443, 8080, 21]

# -----------------------------------
# 1. 100 미만 필터링 - 아래 작성합니다.
known_port = filter(lambda p: p < 100, raw_data)
open_port = map(lambda p: f'{p}:OPEN', known_port)

# -----------------------------------
# 2. 형식 변경 - 아래 작성합니다.
list_port = list(open_port)

print(f"보안 점검 리포트: {list_port}")
