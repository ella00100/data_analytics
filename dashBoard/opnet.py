import pandas as pd
import seaborn as sns
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

oil_prices = pd.read_excel("./data/전체주유소_가격.xlsx")

oil_prices["지역"].value_counts()

seoul_oil=oil_prices.loc[oil_prices["지역"]=="서울특별시", ["고급휘발유", "휘발유", "경유","실내등유"]]

seoul_oil.loc[seoul_oil["고급휘발유"]=="-", "고급휘발유"] = 0
seoul_oil.loc[seoul_oil["휘발유"]=="-", "휘발유"] = 0
seoul_oil.loc[seoul_oil["경유"]=="-", "경유"] = 0
seoul_oil.loc[seoul_oil["실내등유"]=="-", "실내등유"] = 0

seoul_oil["고급휘발유"]=seoul_oil["고급휘발유"].astype('int')
seoul_oil["휘발유"]=seoul_oil["휘발유"].astype('int')
seoul_oil["경유"]=seoul_oil["경유"].astype('int')
seoul_oil["실내등유"]=seoul_oil["실내등유"].astype('int')

df=seoul_oil.mean().reset_index()
df.columns=["oil type", "avg prices"]
df["oil type"] = ["highend", "normal", "light", "inside"]
print(df)

sns.barplot(data=df,
           x="oil type",
           y="avg prices",
           palette="Set2" )

seoul_oil.columns =["highend","normal","light","inside"]
sns.histplot(data=seoul_oil, x="normal", bins=40)
sns.scatterplot(data=seoul_oil, x="normal", y="highend")