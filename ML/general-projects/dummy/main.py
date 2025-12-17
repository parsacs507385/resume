import pandas as pd
from sklearn import linear_model

df = pd.read_csv("data.csv")
model = linear_model.LinearRegression()
X = df[["Mileage", "Age", "Audi A5", "BMW X5"]]
model.fit(X, df["Sell Price"])

print(model.score(X, df["Sell Price"]))