'''
#### [ 도전 문제 3-A ]

### 문제 3-A. CSV DictWriter / DictReader 왕복 저장·읽기

아래 보안 이벤트 데이터를 CSV 파일로 저장한 뒤, 다시 읽어서 severity가 "Critical"인 항목만 출력하세요.

```jsx
import csv

events = [
    {"host": "prd-web-01",  "event": "Port Scan",    "severity": "High"},
    {"host": "prd-db-02",   "event": "SQL Injection", "severity": "Critical"},
    {"host": "stg-api-03",  "event": "XSS Attempt",   "severity": "Medium"},
    {"host": "prd-bastion", "event": "Brute Force",    "severity": "Critical"},
]

# 1. security_events.csv로 저장 (DictWriter, utf-8-sig, newline="")

# 2. 저장한 파일을 읽어서 severity가 "Critical"인 항목만 출력 (DictReader)
```

기대 출력:
[Critical] prd-db-02 — SQL Injection
[Critical] prd-bastion — Brute Force

💡 힌트: DictWriter 사용 시 fieldnames 리스트를 먼저 정의하고, writeheader()로 헤더를 쓴 뒤 writerows()로 데이터를 저장합니다.
'''






'''
#### [ 도전 문제 3-B ]

### 문제 3-B. JSON 직렬화·역직렬화 + with 블록 안전 처리

아래 스캔 결과를 JSON 파일로 저장하고, 다시 읽어서 open_ports 중 1024 미만인 포트만 필터링해 출력하세요.
파일 입출력은 반드시 with 블록을 사용하고, 읽기 과정에는 try/except 예외처리를 포함하세요.

```jsx
import json

scan_result = {
    "target": "10.0.1.50",
    "scan_time": "2026-09-27",
    "open_ports": [22, 80, 443, 3306, 8080, 8443],
    "is_admin_exposed": True
}

# 1. scan_result.json 파일로 저장 (with 블록, indent=2)

# 2. scan_result.json 파일을 읽어서 1024 미만 포트만 필터링 후 출력
#    (with 블록 + try/except 포함)
```

기대 출력:
저장 완료: scan_result.json
1024 미만 개방 포트: [22, 80, 443]

💡 힌트: json.dump()는 파일 객체에 직접 씁니다. json.load()는 파일 객체를 읽어 파이썬 딕셔너리로 반환합니다. 포트 필터링은 리스트 컴프리헨션이나 filter()로 가능합니다.
'''
