import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

samsung = pd.read_excel("./naver_shopping(삼성).xlsx")

from collections import Counter

product_names = []
for row in samsung["제품명"].str.split().tolist():
    product_names += row

print(Counter(product_names).most_common(30))

price_hist = sns.histplot(data=samsung, x="가격", bins=30)
plt.show()

sns.scatterplot(data=samsung, x="리뷰수", y="가격")
plt.show()

index_like =sns.lineplot(x=samsung.index, y=samsung["찜하기"])
plt.show()

onePone= samsung[samsung["제품명"].str.startswith('1+1')]
print(onePone)

