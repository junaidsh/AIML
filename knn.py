import numpy as np
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
print(x[:5],y[:5])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,size=0.4,random_state=1)
print(iris.data.shape)
print(len(x_train))
print(len(y_test))
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
pred=knn.predict(x_test)
from sklearn import metrics
print("Acuracy",metrics.accuracy_score(y_test,pred))
print(iris.target_names[2])
y_testn=[iris.target_names[i] for i in y_test]
predn=[iris.target_names[i] for i in pred]
print(" predicted   Actual")
for i in range(len(pred)):
    print(i," ",predn[i],"  ",y_testn[i])
