import pandas as pd
from sklearn.svm import SVC
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

model = SVC()
X = df.drop("target", axis=1)
model.fit(X, df.target)
print(model.score(X, df.target))