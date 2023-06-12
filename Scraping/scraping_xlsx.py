import openpyxl
import requests
import os
from bs4 import BeautifulSoup


def crawl_naver_news_category(category_code):
    url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={category_code}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        articles = soup.select('div.cluster_text a')

        news_list = []

        for article in articles:
            title = article.get_text().strip()
            link = article.get('href')
            news_list.append({"title": title, "link": link})

        return news_list
    else:
        print("Error: Failed to request page")
        return None


def adjust_column_widths(worksheet):
    # 글꼴 설정
    font = openpyxl.styles.Font(name='맑은 고딕', size=11)

    # 열 너비 자동 조정
    for column in worksheet.columns:
        max_length = 0
        column_letter = openpyxl.utils.get_column_letter(column[0].column)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        worksheet.column_dimensions[column_letter].width = adjusted_width
        for cell in column:
            cell.font = font


workbook = openpyxl.Workbook()

if os.path.exists("news.xlsx"):
    os.remove("news.xlsx")    

worksheet = workbook.active
worksheet.title = "데이터"
# Define category codes and their corresponding names
categories = {
    '100': '정치(Politics)',
    '101': '경제(Economy)',
    '102': '사회(Society)',
    '103': '라이프/문화(Life/Culture)',
    '104': '세계(World)',
    '105': 'IT/과학(IT/Science)'
}

# Crawl multiple categories
all_news = {}

print(f"Start Naver News Scraping")
for category_code, category_name in categories.items():
    news_list = crawl_naver_news_category(category_code)
    all_news[category_name] = news_list

    # Write data to the worksheet
    worksheet.append([category_name])
    worksheet.append(["제목", "주소"])
    for news in news_list:
        worksheet.append([news["title"], news["link"]])

    # Adjust column widths
    adjust_column_widths(worksheet)

# Save the Excel file
workbook.save("news.xlsx")

print(f"FINISH")
