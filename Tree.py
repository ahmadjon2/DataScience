
import pandas as pd

data = pd.read_csv("car.csv")
data.columns = ("sales","maintanance","doors","persons","boot_space","safety","class")
print(data.info())
print(data.isna().sum())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data["sales"] = le.fit_transform(data["sales"])
data["maintanance"] = le.fit_transform(data["maintanance"])
data["doors"] = le.fit_transform(data["doors"])
data["persons"] = le.fit_transform(data["persons"])
data["boot_space"] = le.fit_transform(data["boot_space"])
data["safety"] = le.fit_transform(data["safety"])
data["class"] = le.fit_transform(data["class"])

print(data.info())
from sklearn.model_selection import train_test_split

X = data[["sales","maintanance","doors","persons","boot_space","safety"]]
y = data["class"]
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.7,random_state=10)
print(Xtrain,Xtest,Ytrain,Ytest)

from sklearn.tree import DecisionTreeClassifier
DD = DecisionTreeClassifier()
DD.fit(Xtrain,Ytrain)
YtrainPredict = DD.predict(Xtrain)
YtestPredict = DD.predict(Xtest)

from sklearn.metrics import confusion_matrix,classification_report

cmTrain = confusion_matrix(Ytrain,YtrainPredict)
cmTest = classification_report(Ytest,YtestPredict)
print(cmTrain)
print(cmTest)