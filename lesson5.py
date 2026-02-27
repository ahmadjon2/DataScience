import matplotlib.pyplot as plt

"""

x = [2,5,6,7,3]
y = [1,4,10,8,9]

font1 = { "family": "arial" , "color" : "Blue" , "size" : 20 }

plt.plot(x,y,"g*:")
plt.title("Coordinates",fontdict=font1)
plt.xlabel("X-coordinates")
plt.ylabel("Y-coordinates")
plt.show()



# HOMEWORK perform differnt opperations on iris - mean,median ect

import pandas as pd
data = pd.read_csv("iris.csv")
print(data[["sepal_length"]].mean())
print(data[["sepal_length"]].median())
print(data[["sepal_length"]].max())
print(data[["sepal_length"]].min())

def add_item(item, container=[]):
    container.append(item)
    return container

#bar graph

x1 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
y1 = [3,4,2,4,3,3,1]

font2 = { "family": "arial" , "color" : "Green" , "size" : 20 }
font3 = { "family": "arial" , "color" : "Black" , "size" : 10 }

plt.bar(x1,y1)
plt.title("Weekly Hours of study",fontdict=font2)
plt.xlabel("Days",fontdict=font3)
plt.ylabel("Hours of study",fontdict=font3)
plt.show()

#pie chart

x2 = [8,3,9,4]
y2 = ["school/work","eating","sleeping","Football"]

plt.pie( x2,labels = y2,colors =  ["Blue","Yellow","Orange","Purple"],shadow = True, autopct = "%1.1f%%")
plt.title("What i did in my day",fontdict=font1)
plt.show()

"""

#histogram

import numpy as np

ages = np.random.randint(1,50,50)
intavals = [10,20,30,40,50]

plt.hist(ages,intavals)
plt.show()

#HOMEWORK make some graph like this from titanic data in pie chart then bar graph