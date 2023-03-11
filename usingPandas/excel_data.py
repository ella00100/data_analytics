import pandas as pd
from glob import glob

stations_files = glob('./otp/*.xls')

total = pd.DataFrame()
for file_name in stations_files:
    temp = pd.read_excel(file_name, header=2)
    total = pd.concat([total, temp])
total = total.sort_values(by="지역")
total = total.reset_index(drop = True)

print(total)

total.to_excel("전체주유소_가격.xlsx", index=False)