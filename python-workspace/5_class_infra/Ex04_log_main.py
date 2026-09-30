# 파일명: log_main.py (다른 파일에서 log_analyzer 모듈 활용)
from Ex04_log_analyzer import LogAnalyzer

logs = [
    "[2026-10-06 12:01:22][INFO] 서비스 시작.",
    "[2026-10-06 12:01:23][ERROR] DB 연결 실패.",
    "[2026-10-06 12:01:27][WARNING] 저장공간 부족.",
]

# log_analyzer 모듈 활용
analyzer = LogAnalyzer(logs)
print(analyzer.filter_by_level('ERROR'))