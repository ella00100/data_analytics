import requests
import bs4

page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
print(page_url)
source = requests.get(page_url).text
source = bs4.BeautifulSoup(source)
source.prettify()

dates = source.find_all('td', class_ = 'date')
print(dates)

print(dates[0].text)

date_list = []
for date in dates:
    date_list.append(date.text)

print(date_list)