import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("MODEL")

def getDrug(age, gender, bp, cholesterol, NatoK):
    match gender:
        case "female":
            gender = 0
        case "male":
            gender = 1
        case _:
            gender = ""
    if gender == "":
        return "Error"
    
    match bp:
        case "low":
            bp = 0
        case "normal":
            bp = 1
        case "high":
            bp = 2
        case _:
            bp = ""
    if bp == "":
        return "Error"
    
    match cholesterol:
        case "normal":
            cholesterol = 1
        case "high":
            cholesterol = 2
        case _:
            cholesterol = ""
    if cholesterol == "":
        return "Error"
    
    try:
        ans = model.predict(np.array([[age, gender, bp, cholesterol, NatoK]]))[0]
    except Exception:
        return "Error"
    match ans:
        case 0:
            ans = "drugA"
        case 1:
            ans = "drugB"
        case 2:
            ans = "drugC"
        case 3:
            ans = "drugX"
        case 4:
            ans = "drugY"
        
    return ans
age = input("AGE: ").strip()
gender = input("GENDER: ").strip().lower()
bp = input("BLOOD PRESSURE: ").strip()
cholesterol = input("CHOLESTEROL: ").strip().lower()
NatoK = input("Na/K RATIO: ").strip()
print()
print(f"RECOMMENDED DRUG: {getDrug(age, gender, bp, cholesterol, NatoK)}")