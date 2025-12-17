import pandas as pd

df = pd.read_csv("predata.csv")
models = pd.get_dummies(df.Model, dtype=int)
dfgo = pd.concat([df, models], axis=1)
dfgo = dfgo.drop(["Model", "Mercedez Benz C class"], axis=1)
dfgo.to_csv("data.csv", index=False)