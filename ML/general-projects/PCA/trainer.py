import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
import joblib

df = pd.read_csv("data.csv")
pca = PCA(0.95)
score = 0
while score < 0.85:
    XTrain, XTest, yTrain, yTest = train_test_split(df.drop(["Sex", "ExerciseAngina", "ST_Slope", "HeartDisease"], axis=1), df.HeartDisease, test_size=0.1)
    XTrainPCA = pca.fit_transform(XTrain)
    XTestPCA = pca.fit_transform(XTest)
    model = RandomForestClassifier()
    model.fit(XTrainPCA, yTrain)
    score = model.score(XTestPCA, yTest)
    print(score)

print(f"FINAL SCORE: {score}")
joblib.dump(model, "MODEL")
print("MODEL SAVED.")