import pandas as pd

data = pd.read_csv("adult.csv")
print(data.info())
print(data.isna().sum())

from sklearn.tree import DecisionTreeClassifier
DD = DecisionTreeClassifier()

#39, State-gov, Bachelors, Never-married, Adm-clerical, Not-in-family, White, Male, United-States, <=50K

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
le = LabelEncoder()

for coloumn in data.columns:
    data[coloumn] = le.fit_transform(data[coloumn])
x = data.iloc[:,:-1]        
y = data.iloc[:,-1]             

object = RandomForestClassifier()

Xtrain,Ytrain,Xtest,Ytest =  train_test_split(x,y,train_size=0.7,random_state=10)
object.fit(Xtrain,Ytrain)

YtrainPredict = object.predict(Xtrain)
YtestPredict = object.predict(Xtest)

from sklearn.metrics import classification_report, confusion_matrix
cmtest = confusion_matrix(Ytest,YtestPredict)
cmtrain = confusion_matrix(Ytrain,YtrainPredict)

print(cmtest)
print(cmtrain)
