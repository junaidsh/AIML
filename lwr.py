import numpy as np
from matplotlib.pyplot import plt
import pandas as pd
tou=0.5
data=pd.read_csv(filepath_or_buffer)
x_train=np.array(data.total_bill)
print(x_train)
x_train=x_train[:,np.newaxis]
print(x_train)
y_train=np.array(data.tip)
x_test=[x/10 for x in range(500)]
x_test=x_test[:,np.newaxis]
y_test=[]
count=0
for r in range(len(x_test)):
    wts=np.exp(np.sum((x_train-x_test[r])**2,axis=1)/(2*tou**2))
    w=np.diag(wts)
    factor1=np.linalg.inv(x_train.T.dot(w).dot(x_train))
    parameters=factor1.dot(x_train.T).dot(w).dot(y_train)
    predictions=x_test[r].dot(parameters)
    y_test.append(predictions)
    count+=1
print(len(y_test))
y_test=np.array(y_test)
plt.plot(x_train.squeeze(), y_train,'0')
plt.plot(x_test.squeeze(), y_test,'0')
plt.show()  