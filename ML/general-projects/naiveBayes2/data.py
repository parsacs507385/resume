import pandas as pd

df = pd.read_csv("predata.csv")
df["IsSpam"] = df.Category.apply(lambda x: 1 if x=="spam" else 0)
df.to_csv("data.csv", index=False)