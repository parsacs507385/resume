import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("predata.csv")
# print(df[df["HeartDisease"] == 1].groupby("Sex").describe())
# print(df[df["HeartDisease"] == 1].groupby("ExerciseAngina").describe())
df = df.drop(["ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "Oldpeak", "Age"], axis=1)

df = pd.concat([df, pd.get_dummies(df.Sex, dtype=int, drop_first=True), pd.get_dummies(df.ExerciseAngina, dtype=int, drop_first=True), pd.get_dummies(df.ST_Slope, dtype=int, drop_first=True)], axis=1)




#print(df)
df.to_csv("data.csv", index=False)