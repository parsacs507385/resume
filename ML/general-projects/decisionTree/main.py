import joblib
import pandas as pd

df = pd.read_csv("data.csv")
model = joblib.load("MODEL")

print(model.predict([[0, 20, 10, 0]]))