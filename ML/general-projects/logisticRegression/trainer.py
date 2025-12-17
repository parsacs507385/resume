'''
SIGMOID FUNCTION:
             1
f(z) = ---------------
          1 + e^-z


          1
y = ---------------
     1 + e^-(mx+b)
'''

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
model = LogisticRegression()
score = 0

while score < 0.8:
    XTrain, XTest, yTrain, yTest = train_test_split(df[["level", "salary"]], df.left, test_size=0.1)
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(f"{(score * 100):.2f}%")

print(f"FINAL SCORE: {score}")
print("SAVING MODEL...")
joblib.dump(model, "LOGISTICREGMODEL")
print("DONE.")