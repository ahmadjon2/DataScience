import numpy as np
import time
listnum = [1,2,3,4,5,6,7,8,9,"Ahmadjon"]
print(listnum)
print(type(listnum))
nums_array = np.array(listnum)
print(type(nums_array))
"""
list = []
t1 = time.time()
for i in range(99999999):
    list.append(i)
t2 = time.time()
x = t2 - t1 
print(x)

t3 = time.time()
array = np.arange(0, 99999999)
t4 = time.time()
y = t4 - t3
print(y)
"""
z1 = np.ones(6,int)
print(z1)

z0 = np.zeros((4,3),int)
print(z0)
#dimensions of array
print(z1.ndim)
print(z0.ndim)
#shape of the array
print(z1.shape)
print(z0.shape)
#size of the array
print(z1.size)
print(z0.size)

array = np.arange(11, 22,+2)
print(array)

array2 = np.linspace(10,25,7)
print(array2)

array3 = array.reshape(3,2)
print(array3)