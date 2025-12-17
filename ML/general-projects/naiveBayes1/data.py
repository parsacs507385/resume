import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("predata.csv")
df.drop(["PassengerId", "Name", "SibSp", "Parch", "Ticket", "Cabin", "Embarked"], axis=1, inplace=True)
sexLE = LabelEncoder()
df["SexLE"] = sexLE.fit_transform(df["Sex"])
df.drop("Sex", axis=1, inplace=True)
df = df.dropna()

df.to_csv("data.csv", index=False)