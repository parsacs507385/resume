from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = load_digits()
print(dir(df))
XTrain, XTest, yTrain, yTest = train_test_split(df.data, df.target, test_size=0.2)
model = RandomForestClassifier()
model.fit(XTrain, yTrain)

yP = model.predict(XTest)
yT = yTest

print(confusion_matrix(yT, yP))
print(f"SCORE: {model.score(XTest, yTest)}")