from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = load_digits()

print("LR: ", cross_val_score(LogisticRegression(), df.data, df.target, cv=10).mean())
print("RF: ", cross_val_score(RandomForestClassifier(n_estimators=50), df.data, df.target, cv=10).mean())