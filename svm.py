import pandas as pd
from sklearn import datasets
dataCancer = datasets.load_breast_cancer()
#print(type(dataCancer))
data = pd.DataFrame(dataCancer.data,columns = dataCancer.feature_names)
data["isCancer"] =  dataCancer.target
#print(data)
#print(data.info())
from sklearn.model_selection import train_test_split

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.5,random_state=10)

from sklearn.svm import SVC
model = SVC(kernel = "linear")
model.fit(Xtrain,Ytrain)

YtrainPredict = model.predict(Xtrain)
YtestPredict = model.predict(Xtest)

from sklearn.metrics import confusion_matrix,classification_report

cmtest = confusion_matrix(Ytest,YtestPredict)
cmtrain = confusion_matrix(Ytrain,YtrainPredict)
print(cmtrain)
print(cmtest)

CrTest = classification_report(Ytest,YtestPredict)
CrTrain = classification_report(Ytrain,YtrainPredict)
print(CrTest)
print(CrTrain)