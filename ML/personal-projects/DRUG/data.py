import pandas as pd

df = pd.read_csv("predata.csv")
# p-values| Age: 0.86, Sex: 0.71, BP: 5.04, Chol: 0.00, Na/K: 0.45

df.Sex = df.Sex.apply(lambda x: 1 if x=="M" else 0)

def f1(x):
    if x=="LOW": return 0
    if x=="NORMAL": return 1
    if x=="HIGH": return 2
df.BP = df.BP.apply(f1)

df.Cholesterol = df.Cholesterol.apply(lambda x: 2 if x=="HIGH" else 1)

def f2(x):
    if x=="drugA": return 0
    if x=="drugB": return 1
    if x=="drugC": return 2
    if x=="drugX": return 3
    if x=="drugY": return 4
df.Drug = df.Drug.apply(f2)

# print(df)
# df.to_csv("data.csv", index=False)