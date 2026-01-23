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

#array of random numbers:

randnum = np.random.randint(1,20,5)
print(randnum)

print(np.random.permutation(randnum))

array10 = np.random.randint(1,10,4)
array10 = array10.reshape(2,2)
print(array10)
print(np.random.permutation(array10))

z10 = np.random.randint(1,50,6)
z10 = np.sort(z10)
print(z10)

print(z10[2:-1])
print(z10[0:5:+2])
print(z10+10)                                     #on array only
print(z10)
print(z10[[1,3]])

#conditional slicing

print(z10[z10%2 == 0])
print(z10[z10>20])
print(z10[(10<z10)&(z10<20)])