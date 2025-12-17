import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("predata.csv")
df = df.drop(["PassengerId", "Name", "SibSp", "Parch", "Ticket", "Cabin", "Embarked"], axis=1)
#df.to_csv("predata1.csv", index=0)

df = pd.read_csv("predata1.csv")

leSex = LabelEncoder()
df["SexN"] = leSex.fit_transform(df["Sex"])
df = df.drop(["Sex"], axis=1)
#df.to_csv("data.csv", index=0)