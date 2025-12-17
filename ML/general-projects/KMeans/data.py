import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("predata.csv")
scaler = MinMaxScaler()
df["AgeS"] = scaler.fit_transform(df[["Age"]])
df["IncomeS"] = scaler.fit_transform(df[["Income"]])

# plt.scatter(df.AgeS, df.IncomeS)
# plt.show()

df.to_csv("data.csv", index=0)