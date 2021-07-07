from joblib import dump, load
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("dataset.csv")
# print(data.keys())
clf = DecisionTreeClassifier()
clf.fit(data.drop(columns = ["Name ","Roll number","placement"]),data["placement"])
dump(clf, "model.ml")


