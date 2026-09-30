# 파일명: log_analyzer.py
import re

print("모듈 시작")

class LogAnalyzer:
    def __init__(self, log_lines):
        self.log_lines = log_lines
        self.parsed_logs = [
            parsed for line in log_lines
            if (parsed := self.__parse_line(line)) is not None
        ]
    def __parse_line(self, line):
        pattern = r"\[(.*?)\]\[(.*?)\] (.*)"
        match = re.match(pattern, line)
        if match:
            timestamp, level, message = match.groups()
            return {"timestamp": timestamp, "level": level, "message": message, "raw": line}
        return None

    def filter_by_level(self, level):
        return [log for log in self.parsed_logs if log and log['level'] == level]

    def search(self, keyword):
        return [log for log in self.parsed_logs if log and keyword in log['message']]


# 확인(테스트), 외부에 import 됐을땐 실행안됨
if __name__ == "__main__" :
    print('__main__ 실행')
    sample = LogAnalyzer(["[2026-10-19 12:01:22][INFO] 서비스 시작"])
    print(sample.filter_by_level('INFO'))