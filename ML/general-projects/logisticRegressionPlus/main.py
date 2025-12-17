import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

df = load_digits()
print(dir(df))
model = linear_model.LogisticRegression()
score = 0

while score < 0.9:
    XTrain, XTest, yTrain, yTest = train_test_split(df.data, df.target, test_size=0.2)
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(score)

print(f"SCORE: {score}")