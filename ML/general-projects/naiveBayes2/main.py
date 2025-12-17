import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

df = pd.read_csv("data.csv")
XTrain, XTest, yTrain, yTest = train_test_split(df.Message, df.IsSpam, test_size=0.3)
v = CountVectorizer()
XTrainV = v.fit_transform(XTrain.values).toarray()
XTestV = v.transform(XTest.values).toarray()

model = MultinomialNB()
model.fit(XTrainV, yTrain)

print(model.score(XTestV, yTest))