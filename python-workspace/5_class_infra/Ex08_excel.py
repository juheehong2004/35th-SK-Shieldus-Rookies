from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font
from pathlib import Path

def create_excel_report(news_data):
    wb = Workbook() # 새 엑셀 파일 생성
    ws = wb.active  # 현재 활성화된 워크시트 가져오기
    ws.title = "Security_Report" 
    # 1. 헤더 설정 및 스타일 적용
    headers = ["순번", "뉴스 제목", "위험도"]
    ws.append(headers)

    # 첫 행(헤더) 강조
    header_fill = PatternFill(start_color="333333", fill_type="solid")
    for cell in ws[1]:
        cell.font = Font(color="FFFFFF", bold=True)
        cell.fill = header_fill

    # 2. 데이터 추가
    for i, title in enumerate(news_data, 1):
        risk = "High" if "취약점" in title or "유출" in title else "Normal"
        row = [i, title, risk]
        ws.append(row)

        # 위험도가 High인 행은 빨간색 글자 처리
        if risk == "High":
            ws.cell(row=ws.max_row, column=3).font = Font(color="FF0000", bold=True)

    # 현재 디렉토리에 파일 저장
    # wb.save("Daily_Security_Report.xlsx")
    
    # output 폴더에 파일 저장
    # output 없으면 자동으로 생성해서 에러 발생 없이 실행해야함
    # pathlib : Python의 현대적인 파일·경로 관리 모듈 (이전은 os)
    # 디렉토리 경로 객체 생성 및 폴더 생성
    Path("output").mkdir(parents=True, exist_ok=True)

    # 파일 저장
    wb.save("output/Daily_Security_Report.xlsx")
    




if __name__ == "__main__":
    test_news = ["Windows 커널 취약점 발견", "신규 보안 패치 안내", "개인정보 유출 사고"]
    create_excel_report(test_news)