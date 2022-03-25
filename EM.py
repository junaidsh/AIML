import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
data=pd.read_csv(filepath_or_buffer)
print("ip data and shape")
print(data.shape)
data.head()
f1=data['v1'].values
f2=data['v2'].values
x=np.array(list(zip(f1,f2)))
print("X ",x)
print("the graph for dataset")
plt.scatter(f1,f2,c='black',s=7)
plt.show()
kmean=KMeans(20,random_state=0)
labels=kmean.fit(x).predict(x)
print(labels)
centroids=kmean.cluster_centers_
plt.scatter(x[:,0],x[:,1],c=labels,size=40,cmap='viridis')
print("Graph uisng KMeans")
plt.scatter(centroids[:,0],centroids[:,1],marker='*',s=200,c='#050505')
plt.show()
gmm=GaussianMixture(n_components=1).fit(x)
labels=gmm.predict(x)
probs=gmm.predict_proba(x)
size=10*probs.max(1)**3
print("graph using EM")
plt.scatter(x[:,0],x[:,1],s=size,c=labels,cmap='viridis')
plt.show()