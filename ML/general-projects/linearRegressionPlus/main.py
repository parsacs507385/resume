import pandas as pd
from sklearn import linear_model

df = pd.read_csv("data.csv")
model = linear_model.LinearRegression()
model.fit(df[["experience", "test_score", "interview_score"]], df.salary)

print(round(model.predict([[5, 10, 8]])[0], 0))