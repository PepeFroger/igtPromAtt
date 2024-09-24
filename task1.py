import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

uniqueVal = data["whoAmI"].unique()

oneHot = pd.DataFrame()

for i in uniqueVal:
    oneHot[i] = (data["whoAmI"] == i).astype(int)

data = pd.concat([data, oneHot], axis=1)

print(data.head())