import matplotlib.pyplot as plt
import pandas as pd
import pandas as pnd
import seaborn as sns

df = pd.read_csv("data.csv")

sns.scatterplot(x="salary", y="bonus",size="years_at_company", data=df)

plt.xlabel("Salary")
plt.ylabel("Bonus")
plt.show()