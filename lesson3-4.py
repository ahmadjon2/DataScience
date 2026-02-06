import pandas as pd

dictionary = {"name":["Ahmadjon","Shobhit"],"age":[14,18],"country":["Uzbekistan","India"]}
print(type(dictionary))
data1 = pd.DataFrame(dictionary)
print(type(data1))

data = pd.read_csv("titanic.csv")
print(data)
print(data.info())
print(data.shape)
print(data.describe())
print(data.tail(10))
print(data.dtypes)
print(data[["Age","Name"]])

# filtering rows

print(data[data["Age"] < 18]) 
print(data[data["Sex"] == "male" ]) 
print(data[(data["Sex"] == "male") | (data["Age"] < 18)])

#counting

print(data["Pclass"].value_counts())
print(data["Sex"].value_counts())
print(data["Survived"].value_counts())

#Homework

# maleSecondClass

print(data[(data["Sex"] == "male") & (data["Pclass"] == 2)])

# femaleSecondClass

print(data[(data["Sex"] == "female") & (data["Pclass"] == 2)])

# maleThirdClass

print(data[(data["Sex"] == "male") & (data["Pclass"] == 3)])

# femaleThirdClass

print(data[(data["Sex"] == "female") & (data["Pclass"] == 3)])

# femaleFirstClass

print(data[(data["Sex"] == "female") & (data["Pclass"] == 1)])

#agrigate functions : sum, mean, count, median, min, max

print(data[["Age","Sex","Pclass"]].groupby(["Sex","Pclass"]).mean())
print(data[["Pclass","Name"]].groupby(["Pclass"]).count())
print(data[["Fare","Pclass","Age"]].groupby(["Pclass","Age"]).max())

# loc and iloc

print(data.loc[data["Age"] < 18, ["Name","Age"]])
print(data.iloc[0:50,0:])
data["dicount"] = data["Fare"]*0.15
print(data.iloc[:,-2:])

# sorting data by name

print(data.sort_values(by = "Name"))

# sorting data by age

print(data.sort_values(by = "Age"))

# text based sorting

data["namelowecase"] = data["Name"].str.lower()
print(data)

data["M/F"] = data["Sex"].str[0]
print(data)