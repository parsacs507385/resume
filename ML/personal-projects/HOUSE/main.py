# sqft, bedrooms, garages, age
import joblib

model = joblib.load("MODEL")
print(f"PRICE: IRT {model.predict([[753.474, 1, 1, 50]])[0]*90000:,.0f}")