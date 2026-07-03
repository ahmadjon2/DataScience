
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report

data = pd.read_csv("iris.csv")
data.info()
print(data.isna().sum())

from sklearn.model_selection import train_test_split

X = data[["sepal_length","sepal_width","petal_length","petal_width"]]
y = data["species"]
y = le.fit_transform(y)

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.7,random_state=10)
print(Xtrain,Xtest,Ytrain,Ytest)

object = LogisticRegression()
object.fit(Xtrain,Ytrain)
YtrainPredict = object.predict(Xtrain)
YtestPredict = object.predict(Xtest)

cmtrain = confusion_matrix(Ytrain,YtrainPredict)
cmtest = confusion_matrix(Ytest,YtestPredict)
print(cmtrain)
print(cmtest)

