# 테스트용(IPTIME 재실행 코드, 2023.05.25)
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
    thread = threading.Thread(target=iptime)
    thread.deamon = True
    thread.start()

window = tk.Tk()

def iptime():

# 백그라운드
#    chrome_options = Options()
#    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
#    # browser = webdriver.Chrome(options=chrome_options) # 현재파일과 동일한 경로일 경우 생략 가능

    browser = webdriver.Chrome() # 현재파일과 동일한 경로일 경우 생략 가능

    # ID & PW
    user_id = 'ID'
    user_pw = 'PW'

    # 1. 홈페이지 이동
    browser.get('http://192.168.0.1')

    # 2. id 복사 붙여넣기
    elem_id = browser.find_element(By.NAME, 'username')
    elem_id.click()
    pyperclip.copy(user_id)
    elem_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(0.25)
    
    
    # 3. pw 복사 붙여넣기
    elem_pw = browser.find_element(By.NAME, 'passwd')
    elem_pw.click()
    pyperclip.copy(user_pw)
    elem_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(0.25)

    # 4. 로그인하기
    browser.find_element(By.ID, 'submit_bt').click()
    time.sleep(0.25)

    # 5. 관리도구 이동
    browser.find_element(By.CSS_SELECTOR, "area[coords='45,35,100,110']").click()
    time.sleep(0.25)

    # 6. 시스템 관리 Hidden 열기
    browser.switch_to.frame('main_body') 
    browser.switch_to.frame('navi_menu_advance')
    
    elem_advance = browser.find_element(By.ID, "advance_setup_td")
    elem_advance.click()
    time.sleep(0.25)
    
    # 7. 기타 설정 이동
    browser.find_element(By.ID, "sysconf_setup_td").click()
    time.sleep(0.25)

    # 8. 공유기 다시 시작
    browser.find_element(By.ID, "sysconf_misc_3_td").click()
    time.sleep(0.25)

    browser.switch_to.default_content() # frame 초기화
    browser.switch_to.frame('main_body') # frame 이동
    browser.switch_to.frame('main')
    browser.switch_to.frame('sysconf_misc_iframe')

    browser.find_element(By.ID, "restart").click()
    time.sleep(3)

    browser.switch_to.default_content() # frame 초기화
    browser.switch_to.frame('main_body') # frame 이동
    browser.switch_to.frame('main')

    browser.find_element(By.ID, "apply_bt").click()
    browser.switch_to.alert.accept() # Confirm창 확인
    time.sleep(60)

    # html 정보 출력
    # print(browser.page_source) 

    # 9. 종료
    browser.quit() # 전체 브라우저 종료
    time.sleep(2)
    window.quit() # 프로그램 종료
    
    
button = tk.Button(window, overrelief="solid", command=startThread, text='IPTIME Reboot')
button.pack(ipadx=10, pady=30, ipady=10)

# Frame title, icon
window.title('자동 로그인 툴 by HSKIM')
# window.iconphoto(True, PhotoImage(file=resource_path('icon.png')))

# Frame size
window.geometry("300x150")

# 윈도우 실행
window.mainloop()
time.sleep(1)
messagebox.showinfo("Notification", "프로그램 종료")