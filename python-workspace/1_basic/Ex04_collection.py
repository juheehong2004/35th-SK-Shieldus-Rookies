
#-------------------------------------------------------
# 1. list - 순서있음, 수정가능, 중복허용, [] 대괄호 사용
# 오늘 취약점 스캔을 돌려야 하는 호스트 대기열

scan_queue = ["prd-bastion-01", "prd-db-02", "stg-api-01"] # prd는 Production, stg는 Staging의 약어
print(scan_queue)
print(scan_queue[0])
print(scan_queue[-1])

# 리스트 끝에 요소 추가 - 원본 변경 O
scan_queue.append('prd-cache-01')
print(scan_queue)

# 리스트 요소 삭제 - 원본 변경 O
scan_queue.remove('stg-api-01')
print(scan_queue)

# 리스트 정렬 - 원본 변경 O
scan_queue.sort()
print(scan_queue)

# 마지막 요소 반환하면서 제거 - 원본 변경 O
print(scan_queue.pop())

print()







# 아래 출력를 했을 때 어떤 결과가 나올지 미리 예측을 하시고 확인하시기 바랍니다.

# 패치 대상 관리
patch_queue = ["prd-db-02", "prd-api-04"]
patch_queue.append("stg-cache-01")     # 새 취약 호스트 추가 - ["prd-db-02", "prd-api-04", "stg-cache-01"]
patch_queue.insert(0, "prd-bastion-01")  # 치명적 취약점 호스트를 맨 앞으로 - ["prd-bastion-01", "prd-db-02", "prd-api-04", "stg-cache-01"]
patch_queue.remove("prd-api-04")       # 패치 완료된 호스트 제외 - ["prd-bastion-01", "prd-db-02", "stg-cache-01"]
patch_queue.sort() # ["prd-bastion-01", "prd-db-02", "stg-cache-01"]
print(patch_queue) # ["prd-bastion-01", "prd-db-02", "stg-cache-01"]
print()

#-------------------------------------------------------
# 2. tuple - 순서있음, 수정불가, 중복허용, () 소괄호 사용
#  (프로토콜, 포트, 액션)
#  감사 스크립트가 실행 도중에 방화벽 규칙을 실수로 고치면 안 되므로, 변경 불가로 묶습니다.
firewall_rule = ("TCP", 22, "ALLOW")
firewall_rule = "TCP", 22, "ALLOW" # 소괄호 안적어도 자동으로 튜플로 생성됨

print(f"프로토콜: {firewall_rule[0]}, 포트: {firewall_rule[1]}, 액션: {firewall_rule[2]}")

# 튜플은 수정 불가
# firewall_rule[1] = 2222 # -> TypeError: 'tuple' object does not support item assignment


#-------------------------------------------------------
# 3. Set - 순서없음, 중복불가
names = { "홍길동", "김철수", "이영희", "홍길동"}  # 중복된 이름은 1개만 남음
print(names) # {"김철수", "이영희", "홍길동"}

# Set은 순서가 없으므로 인덱스 쓰면 오류
# print(names[0])




# — 비인가 개방 포트 탐지
# 이번 스캔에서 실제로 열려있는 포트들
scanned_open_ports = {22, 80, 443, 3306, 6379}

# 보안 정책상 공식 허용된 포트 목록
approved_ports = {22, 80, 443}

# 허용되지 않은데 열려있는 포트 (차집합)
unauthorized_ports = scanned_open_ports - approved_ports
# 아래 출력를 했을 때 어떤 결과가 나올지 미리 예측을 하시고 확인하시기 바랍니다.
print(f"비인가 개방 포트: {unauthorized_ports}")  # {3306, 6379}

# 이전 주/이번 주 모두 열려있던 포트 (교집합, 상시 노출 포트)
# 교집합 : intersection() 또는 & 연산자 사용
# 합집합 : union() 또는 | 연산자 사용
scanned_open_ports = {22, 80, 443, 3306, 6379}
last_week_open_ports = {22, 443, 6379, 8080}
persistent_exposed_ports = scanned_open_ports.intersection(last_week_open_ports)
# # 아래 출력를 했을 때 어떤 결과가 나올지 미리 예측을 하시고 확인하시기 바랍니다.
print(f"2주 연속 노출 포트: {persistent_exposed_ports}") # {22, 443, 6379}


#-------------------------------------------------------
# 4. 딕셔너리 - key-value 쌍, key값으로 value 조회

security_event = {
    "cve_id"    : "CVE-2026-30112",
    "host"      : "prd-db-02",
    "severity"  : "HIGH",
    "cvss"      : 8.1,
    "patched"      : False
}
print(f"취약점: {security_event['cve_id']} ({security_event['severity']})")


cve_card = {"id": "CVE-2026-11450", "cvss": 9.4}
# 딕셔너리 key 리스트
print(cve_card.keys())     # dict_keys(['id', 'cvss'])
# 딕셔너리 value 리스트
print(cve_card.values())   # dict_values(['CVE-2026-11450', 9.4])
# 딕셔너리 key-value 리스트(내부는 튜플)
print(cve_card.items())    # dict_items([('id', 'CVE-2026-11450'), ('cvss', 9.4)])


# 딕셔너리에서 키 값으로 value 조회할때 get 사용하기!([] 사용하면 에러남)
# get() : 없는 필드를 찾을 때 에러 대신 기본값 반환
print(cve_card['id']) # get과 같음
print(cve_card.get('id'))

# print(cve_card['assigned']) # get과 같지만 없는 필드면 에러
print(cve_card.get('assigned')) # 에러 안남, 기본값 None 반환
print(cve_card.get('assigned', '미배정')) # 에러 안남, 기본값 '미배정' 반환


# 딕셔너리 키-값 추가(존재하지않는 키값 입력)
cve_card['assigned'] = '홍길동'
cve_card['patched'] = True

print(cve_card)
