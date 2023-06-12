# 테스트용(네이버 로그인 코드, 230524)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tkinter import messagebox
import pyperclip
import time
import tkinter as tk
import threading

# 윈도우 생성

def startThread():
    thread = threading.Thread(target=login)
    thread.deamon = True
    thread.start()

window = tk.Tk()

def login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    # browser = webdriver.Chrome(options=chrome_options) # 현재파일과 동일한 경로일 경우 생략 가능
    browser = webdriver.Chrome(options=chrome_options) # 현재파일과 동일한 경로일 경우 생략 가능

    user_id = 'Naver ID'
    user_pw = 'Naver PW'

    # 1. 네이버 이동
    browser.get('http://naver.com')

    # 2. 로그인 버튼 클릭
    elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")

    # elem = browser.find_element_by_class_name('link_login')
    elem.click()

    # 3. id 복사 붙여넣기
    elem_id = browser.find_element(By.ID, 'id')
    # elem_id = browser.find_element_by_id('id')
    elem_id.click()
    pyperclip.copy(user_id)
    elem_id.send_keys(Keys.CONTROL, 'v')
    # elem_id.send_keys(user_id)
    time.sleep(1)

    # 4. pw 복사 붙여넣기
    elem_pw = browser.find_element(By.ID, 'pw')
    # elem_pw = browser.find_element_by_id('pw')
    elem_pw.click()
    pyperclip.copy(user_pw)
    elem_pw.send_keys(Keys.CONTROL, 'v')
    # elem_pw.send_keys(user_pw)
    time.sleep(1)

    # 5. 로그인 버튼 클릭
    browser.find_element(By.ID, 'log.login').click()
    # browser.find_element_by_id('log.login').click()
    time.sleep(5)
    # 6. html 정보 출력
    print(browser.page_source)

    # 7. 브라우저 종료
    # browser.close() # 현재 탭만 종료
    browser.quit() # 전체 브라우저 종료
    messagebox.showinfo("Notification", "로그인 완료")
    

button = tk.Button(window, overrelief="solid", command=startThread, text='네이버 로그인')
button.pack(ipadx=10, pady=30, ipady=10)

# Frame title, icon
window.title('자동 로그인 툴 by HSKIM')
# window.iconphoto(True, PhotoImage(file=resource_path('icon.png')))

# Frame size
window.geometry("300x150")

# 윈도우 실행
window.mainloop()