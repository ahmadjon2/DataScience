import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as gu
import numpy as np
from sklearn.impute import SimpleImputer

data = pd.read_csv("titanic.csv")
"""
1How many passengers are in the dataset?
2What are the column names and data types?
3How many missing values exist in each column?
4What percentage of passengers survived?
5How many males vs females were onboard?
6Which passenger class (Pclass) had the most passengers?
7What is the average age of passengers?
8What is the oldest and youngest passenger age?
"""
#1
print(len(data))
#2
print(np.array(data.info()))
#3
print(data.isna().sum())
#4
print(len(data[data["Survived"] == 1]) / len(data["Survived"]) * 100)
#5
print(len(data[data["Sex"] == "male"]), (len(data[data["Sex"] == "female"])))
#6
print(data["Pclass"].value_counts().idxmax())
#7
print(data["Age"].mean())
#8
print(data["Age"].max(), data["Age"].min())

