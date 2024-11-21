from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# chrome 키기
crom = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 긁어올 스팀 일일 최다 플레이 차트
url = "https://store.steampowered.com/charts/mostplayed"
crom.get(url)

time.sleep(5)  # 페이지 로딩 

table_rows = crom.find_elements(By.CSS_SELECTOR, 'table > tbody > tr')

for row in table_rows: 
    try:
        # 동시접속자 , 최다 동시 접속자, 가격 클래스 뽑아오기
        player_count = row.find_element(By.CSS_SELECTOR, 'td._3L0CDDIUaOKTGfqdpqmjcy').text.strip()
        daily_highest_player_count = row.find_element(By.CSS_SELECTOR, 'td.yJB7DYKsuTG2AYhJdWTIk').text.strip()
        price= row.find_element(By.CSS_SELECTOR, 'td._3IyfUchPbsYMEaGjJU3GOP').text.strip()
        
        # 게임 이름 가져요기
        game_name = row.find_element(By.CSS_SELECTOR, 'td > a').text.strip()

        # 확인용 출력
        print(f"게임: {game_name}, 동시 접속자 수: {player_count}, 최고 동시 접속자 수: {daily_highest_player_count}, 가격 : {price}")
    except Exception as e:
        print()

crom.quit()