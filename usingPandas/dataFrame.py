import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import using_seaborn as sns

data = [1,3,5,6,8]
series = pd.Series(data)

df = pd.DataFrame(data=np.arange(1,49).reshape(12,4), columns = ["X1", "X2", "X3","X4"])

print(df["X1"])
print(df[0:3])

# df.loc["row에 대한 조건", "col에 대한 조건"]
print(df.loc[2])
print()

print(df.loc[2][2])
print()

print(df.loc[4,"X2"])
print()

print(df.loc[[0,3],["X1","X3"]])
print()

print(df.loc[0:4, "X1":"X3"])
print()

mask = df["X2"] >= 20
print(df.loc[mask])
print(df.loc[mask, "X4"])

mask2 = (df["X3"] >= 10) & (df["X3"] <= 30)
print(df.loc[mask2])

mask3 = (df["X3"]<=10) | (df["X3"] >= 30)
print(df.loc[mask3])
print()

print(df.iloc[2:7, 0:3])