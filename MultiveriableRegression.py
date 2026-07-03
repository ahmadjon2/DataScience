# y = mx + c
# y = m1x1 + m2x2 + c

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("iris.csv")

print(data.info())

#finding no values

print(data.isna().sum())

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y)
y = le.transform(y)
print(y)

from sklearn.model_selection import train_test_split

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,train_size=0.7,random_state=10)

from sklearn.linear_model import LinearRegression

object = LinearRegression()
object.fit(Xtrain,Ytrain)
m = object.coef_
c = object.intercept_
Ytrainpredict = object.predict(Xtrain)
Ytestpredict = object.predict(Xtest)

from sklearn.metrics import root_mean_squared_error

errorY = root_mean_squared_error(Ytrain,Ytrainpredict)
print(errorY)
errorTestY = root_mean_squared_error(Ytest,Ytestpredict)
print(errorTestY)

#polynomial regression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly = PolynomialFeatures(degree=2)
XtrainPoly = poly.fit_transform(Xtrain)
linR = LinearRegression()
linR.fit(XtrainPoly,Ytrain)
XtestPoly = poly.transform(Xtest)
Ytrainpredictpoly = linR.predict(XtrainPoly)
Ytestpredictpoly = linR.predict(XtestPoly)

polyerrorTrainY = root_mean_squared_error(Ytrain,Ytrainpredictpoly)
print(polyerrorTrainY)
polyerrorTestY = root_mean_squared_error(Ytest,Ytestpredictpoly)
print(polyerrorTestY)


