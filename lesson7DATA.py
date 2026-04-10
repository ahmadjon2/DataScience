import pandas as pd
import numpy as np

data = pd.read_csv("Data.csv")
print(data)
print(data.isna().sum())

# Taking care of missing data

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
data[["Age","Salary"]] = imputer.fit_transform(data[["Age","Salary"]])
print(data)

# Seperating features (in capital) and target

X = data.iloc[:,0:3]
print(X)
y = data.iloc[:,3]
print(y)

# Encoding the data

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(y)
y = le.transform(y)
print(y)

# One hot encoding

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],remainder="passthrough")
Xencoded = ct.fit_transform(X)
print(Xencoded)