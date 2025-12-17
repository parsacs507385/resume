# https://github.com/jadijadi/machine_learning_with_python_jadi

# import pandas as pd
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

# df = pd.read_csv("data.csv")
# kRange = range(1, len(df))
# SSE = []

# for k in kRange:
#     km = KMeans(n_clusters=k)
#     km.fit_transform(df[["AgeS"]], df[["IncomeS"]])
#     SSE.append(km.inertia_)

# plt.plot(kRange, SSE)
# plt.show()

############## K = 3 IS THE ELBOW

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
model = KMeans(n_clusters=3)
model.fit(df[["AgeS", "IncomeS"]])
df["Cluster"] = model.predict(df[["AgeS", "IncomeS"]])


# print(df)
plt.scatter(df["Age"], df["Income"], c=df["Cluster"])
plt.show()