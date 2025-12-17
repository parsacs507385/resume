import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("data.csv")

titleLE = LabelEncoder()
genresLE = LabelEncoder()

df["title"] = titleLE.fit_transform(df[["title"]])
# print(df)
df["genres"] = genresLE.fit_transform(df[["genres"]])

X = df[["genres"]]
y = df[["title"]]
genresCount = len(df.genres.unique())
model = KNeighborsClassifier(n_neighbors=genresCount)
model.fit(X, y)
# print(titleLE.inverse_transform([model.predict(np.array([[genresLE.transform(np.array(["Drama"]))[0]]]))[0]])[0])

def getNameRec(genre):
    try:
        return(titleLE.inverse_transform([model.predict(np.array([[genresLE.transform(np.array([str(genre).strip().title()]))[0]]]))[0]])[0])
    except Exception:
        return("salighe ajib (found no matches).")

print()
print()
print()
inp = input(f"ENTER A GENRE (you can add multiple genres by using the '/' character):")
print(getNameRec(inp))