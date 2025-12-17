import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#df = pd.DataFrame([[100, 1000000000],
#                  [200, 1400000000],
#                  [300, 1800000000],
#                  [500, 2400000000]], columns=["area", "price"])
#plt.scatter(df.area, df.price)
#plt.xlabel("area(m^3)")
#plt.ylabel("price(IRT)")
#plt.show()
#lreg = linear_model.LinearRegression()
#lreg.fit(df[["area"]], df.price)
#post = pd.read_csv("postCSV.csv")
#plt.scatter(df.area, df.price)
#plt.plot(post.area, post.price, color="black")
#plt.show()



df = pd.read_csv("data.csv")
model = linear_model.LinearRegression()
model.fit(df[["year"]], df.income)
plt.xlabel("Year")
plt.ylabel("Income($)")
plt.plot(df.year, model.predict(df[["year"]]), color="red")
plt.scatter(df.year, df.income, marker=".", color="green")
plt.show()