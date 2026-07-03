import numpy as np
import matplotlib.pyplot as plt

Xs = [1,2,3,4,5]
Ys = [3,7,9,10,10.5]

x = np.array(Xs)
y = np.array(Ys)

plt.scatter(x,y)
plt.show()

mx = x.mean()
my = y.mean()
m = np.sum((x - mx)*(y - my)) / np.sum((x - mx)**2)
c = my - m*mx

#finding line of best fit 

"""
y = mx + c

m = np.sum((xi - mx)(yi - my)) / sum((xi - mx)**2)
c = my - m*mx
"""

y1 = mx + c
print(m)
print(c)
print(y)

predictionY = m * x + c

plt.scatter(x,y)
plt.plot(x,predictionY)
plt.show()

# error  -  RMSE : root mean squared error

error = np.sqrt(np.mean((predictionY - y)**2))
print(error)

# using libary 

from sklearn.linear_model import LinearRegression

x = x.reshape(-1,1)
lr = LinearRegression()
lr.fit(x,y)
print("slope",lr.coef_)
print("intercept",lr.intercept_)
predictionY = lr.predict(x)
print(predictionY)

from sklearn.metrics import root_mean_squared_error

errorY = root_mean_squared_error(y,predictionY)
print(errorY)

