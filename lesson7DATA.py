import pandas as pd
import numpy as np

data = pd.read_csv("Data.csv")
print(data)
print(data.isna().sum())

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
data[["Age","Salary"]] = imputer.fit_transform(data[["Age","Salary"]])
print(data)

