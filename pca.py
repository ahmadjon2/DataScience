# principal component analysis
import pandas as pd
from sklearn import datasets
dataCancer = datasets.load_breast_cancer()
data = pd.DataFrame(dataCancer.data,columns = dataCancer.feature_names)
data["isCancer"] =  dataCancer.target
#print(data.info())

from sklearn.preprocessing import MinMaxScaler
scaling = MinMaxScaler()
scaledata = scaling.fit_transform(data)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
new_data = pca.fit_transform(scaledata)

variable_data = pd.DataFrame(new_data,columns=["PC1","PC2"])
print(variable_data)

#negative number = negative correlation

import matplotlib.pyplot as plt

plt.scatter(variable_data["PC1"],variable_data["PC2"])
plt.show()

pca4 = PCA(n_components = 4)
new_data4 = pca4.fit_transform(scaledata)
variable_data4 = pd.DataFrame(new_data4,columns=["PC1","PC2","PC3","PC4"])
plt.scatter(variable_data4["PC1"],variable_data4["PC2"],variable_data4["PC3"],variable_data4["PC4"])
plt.show()