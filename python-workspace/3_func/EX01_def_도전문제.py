'''[ 도전문제 1-A ]

### 문제 1-A. 서버 점검 함수 설계 (*args + 단일 책임 원칙)

아래 요구사항에 맞게 두 개의 함수를 각각 작성하세요.

1. `is_high_risk(risk_score)` : 위험 점수가 80 이상이면 `True`, 아니면 `False` 반환
2. `check_servers(*server_names)` : 여러 서버 이름을 받아 각 서버마다 `"[점검 중] <서버명>"` 출력 후, 점검한 서버 수를 반환

두 함수는 **서로를 호출하지 않습니다** (단일 책임 원칙).

def is_high_risk(risk_score):
		# pass를 지우고 여기에 작성하세요
    pass

def check_servers(*server_names):
		# pass를 지우고 여기에 작성하세요
    pass
    

# 실행 예시
print(is_high_risk(90))   # True
print(is_high_risk(70))   # False

count = check_servers("prd-web-01", "prd-db-02", "stg-api-03")
print(f"점검 완료: {count}대")   # 점검 완료: 3대

💡 힌트: *args로 받은 값은 튜플이므로 len()과 for문 모두 사용 가능합니다.
'''

def is_high_risk(risk_score):
    '''
    매개변수로 넘어오는 위험 점수가 80 이상이면 `True`, 아니면 `False` 반환
    
    Args:
        risk_score(int) : 위험 판단할 위험 점수
    Returns:
        bool : 위험 여부(80점 이상 'True', 아니면 'False')
    '''
    return risk_score >= 80

def check_servers(*server_names):
    '''
    여러 서버 이름을 받아 각 서버마다 `"[점검 중] <서버명>"` 출력 후, 점검한 서버 수를 반환

    Args:
        *server_names(tuple): 여러개의 서버 이름들
    Returns:
        int : 점검한 서버 개수
    '''
    for server in server_names:
        print(f'[점검 중] <{server}>')

    return len(server_names)


print(is_high_risk(90))   # True
print(is_high_risk(70))   # False

count = check_servers("prd-web-01", "prd-db-02", "stg-api-03")
print(f"점검 완료: {count}대")   # 점검 완료: 3대




'''
[ 도전 문제 1-B ]

### 문제 1-B. lambda + filter / map / sorted 조합

아래 서버 인벤토리 데이터를 활용해 세 가지 작업을 각각 한 줄로 완성하세요.

servers = [
    {"name": "prd-web-01",  "risk": 55},
    {"name": "prd-db-02",   "risk": 92},
    {"name": "stg-api-03",  "risk": 78},
    {"name": "prd-bastion", "risk": 88},
]

# 1. risk가 80 이상인 서버만 골라내기 (filter + lambda)
high_risk = _______________

# 2. 모든 서버 이름 앞에 "[점검대상] " 태그 붙이기 (map + lambda)
tagged = _______________

# 3. risk 점수 기준 내림차순 정렬 (sorted + lambda)
sorted_servers = _______________

print(list(high_risk))
print(list(tagged))
print(sorted_servers)

기대 출력:
[{'name': 'prd-db-02', 'risk': 92}, {'name': 'prd-bastion', 'risk': 88}]
['[점검대상] prd-web-01', '[점검대상] prd-db-02', '[점검대상] stg-api-03', '[점검대상] prd-bastion']
[{'name': 'prd-db-02', 'risk': 92}, {'name': 'prd-bastion', 'risk': 88}, {'name': 'stg-api-03', 'risk': 78}, {'name': 'prd-web-01', 'risk': 55}]

💡 힌트: filter와 map의 결과는 list()로 감싸야 출력됩니다.
'''

servers = [
    {"name": "prd-web-01",  "risk": 55},
    {"name": "prd-db-02",   "risk": 92},
    {"name": "stg-api-03",  "risk": 78},
    {"name": "prd-bastion", "risk": 88},
]

# 1. risk가 80 이상인 서버만 골라내기 (filter + lambda)
high_risk = list(filter(lambda s: s["risk"] >= 80, servers))

# 2. 모든 서버 이름 앞에 "[점검대상] " 태그 붙이기 (map + lambda)
tagged = list(map(lambda s: f'[점검대상] {s["name"]}', servers))

# 3. risk 점수 기준 내림차순 정렬 (sorted + lambda) - true가 기본값, 생략 가능
sorted_servers = sorted(servers, key=lambda s: s["risk"], reverse=True)

print(list(high_risk))
print(list(tagged))
print(sorted_servers)