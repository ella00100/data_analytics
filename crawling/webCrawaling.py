import requests
import bs4
import pandas as pd

page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={1}"
source = requests.get(page_url).text
source = bs4.BeautifulSoup(source)
last_url = source.find_all('td', class_="pgRR")[0].find_all('a')[0]["href"]
last_page = int(last_url.split('&page=')[-1])

date_list = []
prices_list = []

for page in range(2, last_page + 1):
    page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page}"

    dates = source.find_all('td', class_='date')

    for date in dates:
        date_list.append(date.text)

    prices = source.find_all('td', class_='number_1')

    for price in prices[::4]:
        prices_list.append(price.text)

print(len(date_list))

print(date_list)
print(prices_list)

df = pd.DataFrame({"date" : date_list, "price" : prices_list}).dropna()
print(df)


