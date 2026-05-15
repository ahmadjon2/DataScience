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
m = np.sum((x - mx)*(y - my) / sum(x - mx)**2)
c = my - m*mx

#findding line of best fit 

"""
y = mx + c

m = np.sum((xi - mx)(yi - my) / sum(xi - mx**2))
c = my - m*mx
"""

y1 = mx + c
print(m, c, y)

predictionY = m * x + c