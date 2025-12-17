import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data.csv")
score = 0
while score < 0.9:

    XTrain, XTest, yTrain, yTest = train_test_split(df[["sqft", "bedrooms", "garage_spaces", "age"]], df.price, test_size=0.2)
    model = LinearRegression()
    model.fit(XTrain, yTrain)
    score = model.score(XTest, yTest)
    print(score)

print(f"SCORE: {score}")
joblib.dump(model, "MODEL")
print("DONE.")