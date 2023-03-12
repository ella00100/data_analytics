import requests
import bs4
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import warnings

warnings.simplefilter('ignore')

driver = Chrome('./chromedriver')
driver.get(f"https://search.shopping.naver.com/search/all?query=삼성&prevQuery=삼성")
time.sleep(1)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
time.sleep(1)

list_basis = driver.find_element(By.CLASS_NAME, "list_basis")
item_list = list_basis.find_elements(By.CLASS_NAME, 'basicList_inner__xCM3J')

query = '삼성'
titles = []
prices =[]
review_counts = []
buy_counts = []
published_dates = []
likes = []


item = item_list[0]
title = item.find_element(By.CLASS_NAME,'basicList_title__VfX3c')
titles.append(title.text)

price = item.find_element(By.CLASS_NAME,"price_num__S2p_v").text[:-1].replace(',', '')
prices.append(price)

footer = item.find_element(By.CLASS_NAME,'basicList_etc_box__5lkgg')  # .text
reviews = footer.find_elements(By.CLASS_NAME,'basicList_num__sfz3h')
footer_text = footer.text

try:
    if "구매건수" in footer_text:
                review_counts.append(int(reviews[0].text.replace(',', '')))
                buy_counts.append(int(reviews[1].text.replace(',', '')))
                likes.append(int(reviews[2].text.replace(',', '')))

    else:
                review_counts.append(int(reviews[0].text.replace(',', '')))
                likes.append(int(reviews[1].text.replace(',', '')))


except IndexError:  ## 리뷰가 아직 충분하지 않아서, 정보가 안뜨는 케이스
            review_counts.append(0)
            likes.append(int(reviews[0].text.replace(',', '')))



print(titles)
print(prices)
print(review_counts)
print(buy_counts)
print(published_dates)
print(likes)
