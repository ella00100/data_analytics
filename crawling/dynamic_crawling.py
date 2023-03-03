# 1. webdriver를 킨다.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver')

# 2. 지역별 주유소 찾기 접속
driver.get("https://www.opinet.co.kr/searRgSelect.do")
time.sleep(2)
driver.execute_script('goSubPage(0,0,99)')

# 3. sido 목록을 가져온다.
time.sleep(2)
sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
sido_names = sido.find_elements(By.TAG_NAME, 'option')

sido_list = []
for sido_name in sido_names:
    sido_list.append(sido_name.get_attribute('value'))

sido_list = sido_list[1:]

# 4. 원하는 지역으로 이동한다.
for sido_name in sido_list:
    sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
    sido.send_keys(sido_name)
    time.sleep(2)

    # 5. 시/군/구 목록을 가져온다.
    sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
    sigungu_names = sigungu.find_elements(By.TAG_NAME, 'option')

    sigungu_list = []
    for sigungu_name in sigungu_names:
        sigungu_list.append(sigungu_name.get_attribute('value'))

    sigungu_list = sigungu_list[1:]
    sigungu.send_keys(sigungu_list[0])

    for sigungu_name in sigungu_list:
        sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
        sigungu.send_keys(sigungu_name)
        time.sleep(2)
        # 6. 얻어온 목록으로 반복문을 수행하면서, 조회를 누르고 엑셀저장을 누른다.
        driver.find_element(By.XPATH, '//*[@id="searRgSelect"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="glopopd_excel"]').click()