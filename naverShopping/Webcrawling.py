import requests
import bs4
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import warnings

warnings.simplefilter('ignore')

query = '애플'
titles = []
prices =[]
review_counts = []
buy_counts = []
likes = []


driver = Chrome('./chromedriver')

for page_no in range(1,6):

    page_url = f"https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={query}&pagingIndex={page_no}&pagingSize=40&productSet=total&query={query}&sort=rel&timestamp=&viewType=list"
    driver.get(page_url)
    time.sleep(1)

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)

    list_basis = driver.find_element(By.CLASS_NAME, "list_basis")
    item_list = list_basis.find_elements(By.CLASS_NAME, 'basicList_inner__xCM3J')

    item = []
    for i in range(len(item_list)):
        item = item_list[i]
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
            likes.append(int(reviews[0].text.replace(',', '')))


print(len(titles), len(prices), len(review_counts), len(likes))
result = pd.DataFrame({"제품명" : titles,
                       "가격" : prices,
                       "리뷰수" : review_counts,
                       "찜하기" : likes})
print(result)
result.to_excel(f"naver_shopping({query}).xlsx", index=False)