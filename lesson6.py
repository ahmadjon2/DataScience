#HOMEWORK make some graph like this from titanic data in pie chart then bar graph

#bar graph
import matplotlib.pyplot as plt
import pandas as pd
"""
data = pd.read_csv("titanic.csv")
x = data["Sex"].value_counts()

plt.bar(x.index,x.values)
print(x)
plt.show()

data = pd.read_csv("titanic.csv")
x1 = data["Pclass"].value_counts()
plt.pie(x1.values,labels=x1.index,autopct = "%1.1f%%")
plt.show()

x2 = [1,6,7,4,9]
y2 = [2,8,5,10,3]

plt.scatter(x2,x2)
plt.show()"""

#stackplot

Activities = ["football","sleep","videogames","studying"]
Monday = [4,8,2,3]
Tuesday = [1,9,4,4]
Wednesday = [6,9,3,4]
Thursday = [6,8,1,3]
Friday = [3,10,5,3]

plt.stackplot(Activities,Monday,Tuesday,Wednesday,Thursday,Friday,labels=["Monday","Tuesday","Wednesday","Thursday","Friday"])
plt.legend()
plt.xlabel("Activities")
plt.ylabel("Hours")
plt.show()

#subplot

plt.figure()
plt.subplot(231)
x = ["Games","Work"]
y = [2,3]
plt.bar(x,y)
plt.subplot(235)
x = ["Games","Work"]
y = [2,3]
plt.bar(x,y)


plt.show()
