'''
입력 예시
CVE-2024-1003
APP-01
'''

# 1. 환경 설정 및 모듈 임포트
import os
import random
from dotenv import load_dotenv

# .env 파일의 환경변수들을 시스템 환경변수로 로드
load_dotenv()

# .env의 SCANNER_NAME 사용, 없으면 기본값 "Local-Scanner"
scanner = os.getenv("SCANNER_NAME", "Local-Scanner")


# 2. 기초 데이터 선언
critical_hosts = ("WEB-01", "DB-01")
vuln_assets = [
    {"cve": "CVE-2024-1001", "host": "WEB-01", "patched": False},
    {"cve": "CVE-2024-1002", "host": "DB-01", "patched": True}
]


# 3. 입력 처리
new_cve = input("추가할 CVE ID: ")
new_host = input("추가할 대상 호스트: ")

vuln_assets.append({"cve" : new_cve, "host" : new_host, "patched" : False})


# 4. 데이터 수정
# 첫 번째 취약점의 `patched` 상태를 `True` 로 변경
vuln_assets[0]["patched"] = True

# 새로 추가된 취약점(`vuln_assets` 의 가장 마지막 항목)에 실수형 CVSS 점수를 부여 (`random` 을 이용한 0~10 실수 생성)
vuln_assets[-1]["cvss"] = random.uniform(0,10)


# 5. 포매팅 출력
divider = "-" * 50

print(f'''총 {len(vuln_assets)}건의 취약점에 대한 패치 점검을 수행합니다.
{divider}
[스캐너: {scanner}] {vuln_assets[0].get("cve")} ({vuln_assets[0].get("host")}) 패치 상태: {vuln_assets[0].get("patched")}
핵심 자산 여부: {vuln_assets[0].get("host") in critical_hosts}
{divider}
[스캐너: {scanner}] {vuln_assets[1].get("cve")} ({vuln_assets[1].get("host")}) 패치 상태: {vuln_assets[1].get("patched")}
핵심 자산 여부: {vuln_assets[1].get("host") in critical_hosts}
{divider}
[스캐너: {scanner}] {vuln_assets[2].get("cve")} ({vuln_assets[2].get("host")}) 패치 상태: {vuln_assets[2].get("patched")}
핵심 자산 여부: {vuln_assets[2].get("host") in critical_hosts} / 현재 위험도: {vuln_assets[2].get("cvss"):.1f}
{divider}''')