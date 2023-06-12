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

if os.path.exists("log.txt"):
    os.remove("log.txt")        

print(f"Start Naver News Scraping")
for category_code, category_name in categories.items():
    news_list = crawl_naver_news_category(category_code)
    all_news[category_name] = news_list
    # print(f"{category_name} News:")

    f = open('log.txt', 'a', encoding='utf-8')
    f.write(f"\n{category_name}")
    for news in news_list:
        f.write(f"\n- 제목: {news['title']}\n- 주소: ({news['link']})\n")
        # f.write(f"{category_name}\n- Title: {news['title']}\n- Link: {news['link']}\n\n")
            
    # print("\n")
print(f"FINISH")