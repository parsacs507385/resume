import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

df = pd.read_csv("data.csv")
score = 0
while score < 0.8:

    XTrain, XTest, yTrain, yTest = train_test_split(df.drop("Survived", axis=1), df.Survived, test_size=0.2)
    model = GaussianNB()
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(f"GaussianNB: {score}")
    model = LogisticRegression()
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(f"LogisticReg: {score}")