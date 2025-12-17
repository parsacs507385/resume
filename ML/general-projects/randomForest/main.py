from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
digits = load_digits()

df = pd.DataFrame(digits.data)
df["target"] = digits.target
XTrain, XTest, yTrain, yTest = train_test_split(df.drop("target", axis=1), df.target, test_size=0.2)

model = RandomForestClassifier()
model.fit(XTrain, yTrain)
print(model.score(XTest, yTest))