import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("C:\data/titanic.csv")

# titanic.info()
# titanic.describe()

idx_sex = pd.pivot_table(data=titanic,index="Sex", values="Survived",
               aggfunc = ["mean", "sum", "count"])
print(idx_sex)

idx_Pclass = pd.pivot_table(data=titanic,index="Pclass", values="Survived",
               aggfunc = ["mean", "sum", "count"])
print(idx_Pclass)

idx_Sex_Pclass = pd.pivot_table(data=titanic,index=["Sex","Pclass"], values="Survived",
               aggfunc = ["mean", "sum", "count"])
print(idx_Sex_Pclass)