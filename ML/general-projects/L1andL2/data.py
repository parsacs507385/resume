import pandas as pd

df = pd.read_csv("predata.csv")
df = df.drop(["Suburb", "Address", "Method", "SellerG", "Date", "Distance", "Postcode", "Bedroom2", "Car", "BuildingArea", "CouncilArea", "Lattitude", "Longtitude", "Propertycount"], axis=1)
df.Price = df.Price.fillna(df.Price.mean())
df.Bathroom = df.Bathroom.fillna(df.Bathroom.median())
df.Landsize = df.Landsize.fillna(df.Landsize.median())
df.YearBuilt = df.YearBuilt.fillna(df.YearBuilt.median())
df = df.dropna()

df = pd.concat([df, pd.get_dummies(df["Type"], dtype=int), pd.get_dummies(df["Regionname"], dtype=int)], axis=1)
#print(df)
df.to_csv("data.csv", index=False)