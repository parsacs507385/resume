import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
s = MinMaxScaler()
df = pd.read_csv("predata.csv")
df = df.drop(["has_pool", "is_new", "crime_rate", "walk_score", "days_on_market", "condition", "has_fireplace", "floors", "id", "zipcode", "bathrooms", "year_built", "lot_size", "heating_type", "hoa_fee", "price_per_sqft"], axis=1)

df["price_sqft"] = df.price/df.sqft
df = df[(df["price_sqft"].quantile(0.25) < df["price_sqft"]) & (df["price_sqft"] < df["price_sqft"].quantile(0.75))]
df = df.drop("price_sqft", axis=1)

df["sqftS"] = s.fit_transform(df[["sqft"]])
df["bedroomsS"] = s.fit_transform(df[["bedrooms"]])
df = df[(df["bedroomsS"] < df["sqftS"])]
df = df.drop(["bedroomsS", "sqftS"], axis=1)

df["sqftS"] = s.fit_transform(df[["sqft"]])
df["garageS"] = s.fit_transform(df[["garage_spaces"]])
df = df[df["garageS"] < df["sqftS"]]
df = df.drop(["garageS", "sqftS"], axis=1)

df = df[(df.age.quantile(0) < df["age"]) & (df["age"] < df.age.quantile(0.8))]



#plt.scatter(df.has_pool, df.price)
#lr.fit(df[["age"]], df["price"])
#plt.plot(df.age, lr.predict(df[["age"]]))
#plt.show()
df["priceH"] = df["price"]
df["price"] = df["age"]
df["age"] = df["priceH"]
df = df.drop("priceH", axis=1)
df = df.rename(columns={"age": "price", "price": "age"})
#print(df)
df.to_csv("data.csv", index=False)