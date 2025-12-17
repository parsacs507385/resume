import pandas as pd
from word2number import w2n

df = pd.read_csv("predata.csv")
for c in df.experience:
    if pd.isna(c):
        continue
    rowNum = df[df.experience == c].index[0]
    df.iat[rowNum, 0] = w2n.word_to_num(c)
df.experience = df.experience.fillna(df.experience.median())
df.test_score = df.test_score.fillna(df.test_score.median())

df.to_csv("data.csv", index=False)