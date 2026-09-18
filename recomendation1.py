"""alcohol,malic_acid,ash,alcalinity_of_ash,magnesium,total_phenols,flavanoids,nonflavanoid_phenols,proanthocyanins,color_intensity,hue,od280/od315_of_diluted_wines,proline
"""
import pandas as pd

data = pd.read_csv("wine.csv")
print(data.info())

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

le = LabelEncoder()

X = data.iloc[:,1:]
y = data.iloc[:,0]

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.5,random_state=10)

from sklearn.neighbors import KNeighborsClassifier

KNC = KNeighborsClassifier(n_neighbors=10)
KNC.fit(Xtrain,Ytrain)
YtrainPredict = KNC.predict(Xtrain)
YtestPredict = KNC.predict(Xtest)

from sklearn.metrics import confusion_matrix,classification_report

cmtest = confusion_matrix(Ytest,YtestPredict)
cmtrain = confusion_matrix(Ytrain,YtrainPredict)
print(cmtrain)
print(cmtest)

crtrain = classification_report(Ytrain,YtrainPredict)
crtest = classification_report(Ytest,YtestPredict)
print(crtrain)
print(crtest)