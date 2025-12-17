# L1: Lasso
# L2: Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

df = pd.read_csv("data.csv")
XTrain, XTest, yTrain, yTest = train_test_split(df.drop(["Price", "Type", "Regionname"], axis=1), df["Price"], test_size=0.2)

print("Lasso:", cross_val_score(Lasso(), XTest, yTest).mean())
print("RandomForest:", cross_val_score(RandomForestRegressor(), XTest, yTest).mean())
print("Linear:", cross_val_score(LinearRegression(), XTest, yTest).mean())
#fig, axs = plt.subplots(2, 3)
# axs[0, 1].scatter(XTest.Bathroom, yTest)
# axs[0, 2].scatter(XTest.Landsize, yTest)
# axs[1, 1].scatter(XTest.TypeLE, yTest)
# axs[1, 2].scatter(XTest.RegionLE, yTest)
# plt.show()