import os
import random

from dotenv import load_dotenv

# .env 파일의 환경변수들을 시스템 환경변수로 로드
load_dotenv()

# 스캐너명 확보
scanner = os.getenv("SCANNER_NAME", "Local-Scanner")

# 기초 데이터 선언
critical_hosts = ("WEB-01", "DB-01")
vuln_assets = [
    {"cve": "CVE-2024-1001", "host": "WEB-01", "patched": False},
    {"cve": "CVE-2024-1002", "host": "DB-01", "patched": True}
]

vuln_assets.append({input(2):input(2)})

print(vuln_assets)