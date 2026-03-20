import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("titanic.csv")


amount = data["Survived"].value_counts()

"""plt.bar(amount.index,amount.values)
plt.show()"""

"""plt.pie(amount.values,labels = amount.index, autopct = "%1.1f%%")
plt.show()"""

Age = data["Age"]
print(Age)

intervals = [0,10,20,30,40,50,60,60,80,90,100]

plt.hist(Age,intervals)
plt.show()

print(Age.max())

#Plot Age vs Fare using a scatter plot

Fare = data["Fare"]
Pclass = data["Pclass"]

plt.scatter(Pclass,Fare)
plt.title("Pclass vs Fare")
plt.show()