'''

# [ 도전 실습 ] — 보안 감사 자동화 엔진 Ver.2

오늘 배운 조건문·반복문·예외 처리를 모두 결합해서, 앞에서 만든 스캔 대상 호스트 List와 CVE Dict를 자동으로 순회·판정하는 미니 엔진을 완성해 봅시다.

- **요구사항**
    1. `scan_queue` 리스트(스캔 대상 호스트 3~4개)와 `cve_inventory` 딕셔너리(CVE ID를 Key로, `{host, cvss, patched}`를 Value로 하는 구조)를 준비합니다.
    2. `for`문으로 `cve_inventory`를 순회하면서, CVSS 점수를 기준으로 `if-elif-else`로 `CRITICAL/HIGH/MEDIUM/LOW` 등급을 매깁니다.
    3. 미패치(`patched: False`) 상태이면서 등급이 `CRITICAL`이면 `"[긴급] ..."` 메시지를 출력하고, 그 즉시 `break`로 점검을 중단합니다. (가장 위험한 것 하나만 먼저 보고한다는 실무 시나리오입니다.)
    4. 전체 순회 과정을 `try-except`로 감싸서, `cve_inventory`의 값 중 예상치 못한 자료형이 들어와도 스크립트가 죽지 않고 `"[오류] 데이터 형식을 확인하세요"`를 출력하도록 방어합니다.
    5. List Comprehension을 사용해서, 최종적으로 **미패치 CVE ID만 모은 리스트**를 별도로 출력합니다.

# — CVSS 점수 기반 심각도 등급 분류
# |       점수 | 위험도 |
# | ---------: | ---   |
# |        0.0 | 없음  |
# |  0.1 ~ 3.9 | 낮음  |
# |  4.0 ~ 6.9 | 중간  |
# |  7.0 ~ 8.9 | 높음  |
# | 9.0 ~ 10.0 | 치명적 |
'''

scan_queue = ["prd-bastion-01", "prd-db-02", "prd-api-04"]
cve_inventory = {
    "CVE-2026-30112": {"host": "prd-db-02", "cvss": 8.1, "patched": False},
    "CVE-2026-11450": {"host": "prd-api-04", "cvss": 9.4, "patched": True},
}

for cve in cve_inventory:
    cvss_score = cve.value()["cvss"]
    