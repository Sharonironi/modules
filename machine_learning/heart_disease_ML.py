import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.preprocessing import StandardScaler

# link to download this data: https://www.kaggle.com/cdabakoglu/heart-disease-classifications-machine-learning/data?select=heart.csv

df = pd.read_csv("heart.csv")
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=101)

scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)


lg = LogisticRegression()
lg.fit(x_train, y_train)
pred = lg.predict(x_test)

print(classification_report(y_test, pred))
print()
print(confusion_matrix(y_test,pred))