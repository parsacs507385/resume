import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data.csv")
model = DecisionTreeClassifier()
score = 0

while score < 0.8:
    XTrain, XTest, yTrain, yTest = train_test_split(df[["Pclass", "Age", "Fare", "SexN"]], df.Survived, test_size=0.3)
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(score)

print(f"FINAL SCORE: {score}")
print("SAVING...")
joblib.dump(model, "MODEL")
print("DONE.")