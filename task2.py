import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data.csv")

sns.lineplot(x="age", y="spending_score", data=df)

plt.xlabel("Age")
plt.ylabel("Spending score")
plt.show()