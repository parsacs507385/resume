'''
SIGMOID FUNCTION:
             1
f(z) = ---------------
          1 + e^-z


          1
y = ---------------
     1 + e^-(mx+b)
'''

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
model = joblib.load("LOGISTICREGMODEL")
_, XTest, _, yTest = train_test_split(df[["level", "salary"]], df.left, test_size=0.4)

print(model.predict([[0.2, 1]]))