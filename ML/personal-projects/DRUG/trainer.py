import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data.csv")
XTrain, XTest, yTrain, yTest = train_test_split(df.drop("Drug", axis=1), df[["Drug"]], test_size=0.2, random_state=0)

model = RandomForestClassifier()
model.fit(XTrain, yTrain)
print(model.score(XTest, yTest))

joblib.dump(model, "MODEL")