import numpy as np
import pandas as pd

data = [1,3,5,6,8]
series = pd.Series(data)

df = pd.DataFrame(data=np.arange(1,49).reshape(12,4), columns = ["X1", "X2", "X3","X4"])
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df["X1"])
print(df["X1"]+2)
print(df.head())
print(df.head(10))
print(df.info())
print(df.describe())
print(df.sort_values(by="X2",ascending = False))