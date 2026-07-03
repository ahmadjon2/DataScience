import pandas as pd

data = pd.read_csv("iris.csv")
print(data.info())
print(data.isna().sum())

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

le = LabelEncoder()
X = data[["sepal_length","sepal_width","petal_length","petal_width"]]
y = data["species"]
y = le.fit_transform(y)
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.7,random_state=10)

from sklearn.linear_model import LogisticRegression
object = LogisticRegression()
object.fit(Xtrain,Ytrain)
YtrainPredict = object.predict(Xtrain)
YtestPredict = object.predict(Xtest)

from sklearn.neighbors import KNeighborsClassifier
KNC = KNeighborsClassifier(n_neighbors=10)
KNC.fit(Xtrain,Xtest)
YtrianPredict = object.predict(Xtrain)
YtestPredict = object.predict(Xtest)

from sklearn.metrics import confusion_matrix,classification_report

cmtrain = confusion_matrix(Ytrain,YtrainPredict)
cmtest = confusion_matrix(Ytest,YtestPredict)
print(cmtrain)
print(cmtest)

crtrain = classification_report(Ytrain,YtrainPredict)
crtest = classification_report(Ytest,YtestPredict)
print(crtrain)
print(crtest)
