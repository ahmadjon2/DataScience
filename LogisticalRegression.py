import pandas as pd

data = pd.read_csv("titanic.csv")
print(data.info())
print(data.isna().sum())

from sklearn.model_selection import train_test_split

X = data[["Pclass","Sex","Age","Siblings/Spouses Aboard","Parents/Children Aboard"]]
y = data["Survived"]
#Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(X["Sex"])
X["Sex"] = le.transform(X["Sex"])

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.7,random_state=10)
print(Xtrain,Xtest,Ytrain,Ytest)

from sklearn.linear_model import LogisticRegression
object = LogisticRegression()
object.fit(Xtrain,Ytrain)
YtrainPredict = object.predict(Xtrain)
YtestPredict = object.predict(Xtest)

from sklearn.metrics import confusion_matrix,classification_report
cmtrain = confusion_matrix(Ytrain,YtrainPredict)
cmtest = confusion_matrix(Ytest,YtestPredict)
print(cmtrain)
print(cmtest)

#tp - truepositive,fn - falsenegative,fp - falsepositive,tn - truenegative
#2columns and 2 rows for surving and not surviving.

print(classification_report(Ytrain,YtrainPredict))
print(classification_report(Ytest,YtestPredict))

#precision = tp / (tp + fp)
#recall = tp / (tp + fn)
#accuracy = (tp + tn) / (tp + tn + fp + fn)
