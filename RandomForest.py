import pandas as pd

data = pd.read_csv("adult.csv")
print(data.info())
print(data.isna().sum())

from sklearn.tree import DecisionTreeClassifier
DD = DecisionTreeClassifier()

#39, State-gov, Bachelors, Never-married, Adm-clerical, Not-in-family, White, Male, United-States, <=50K

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for coloumn in data.columns:
    data[coloumn] = le.fit_transform(data[coloumn])
x = data.iloc[:,:-1]        
y = data.iloc[:,-1]             

x = le.fit_transform(x)
y = le.fit_transform(y)

