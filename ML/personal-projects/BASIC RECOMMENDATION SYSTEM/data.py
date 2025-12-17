import pandas as pd

df = pd.read_csv("movies.csv")

df = df.drop("movieId", axis=1)

df.genres = df.genres.apply(lambda x: pd.NA if x=="(no genres listed)" else x)
df = df.dropna(subset="genres")

def f1(x):
    lis = str(x).split("(")
    if len(lis) != 2:
        return pd.NA
    lis[1] = str(lis[1])[:4]
    return lis[1]
df["year"] = df.title.apply(f1)
df = df.dropna(subset="year")

def f2(x):
    lis = str(x).split("(")
    lis[0] = str(lis[0]).strip().title()
    return lis[0]

df.title = df.title.apply(f2)

def f3(x):
    lis = str(x).split("|")
    if len(lis) == 1:
        return f"{lis[0]}"
    if len(lis) == 2:
        return f"{lis[0]}/{lis[1]}"
    if 3 <= len(lis):
        return f"{lis[0]}/{lis[1]}"
df.genres = df.genres.apply(f3)

# print(df)
# df = df.reset_index(drop=True)
# df.to_csv("data.csv", index=False)