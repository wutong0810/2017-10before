# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:56:34 2017

@author: wutongshu
"""
#参数调整import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3, random_state=0)




#c=1时
mape1=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape1[z,i]=c1

#c=4时
mape3=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=4, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape3[z,i]=c1


#c=1，调整学习率
mape4=np.zeros((6,6))

for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape4[i,z]=c1        



#c=4，调整学习率
mape5=np.zeros((6,6))
for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=4, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape5[i,z]=c1 


#绘制学习深度变化图    
#学习率=0.5    
mape6=np.zeros((3,4))

for i,j in enumerate([1000,2000,8000]):
    for z,h in enumerate([1,2,3,4]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=0.5, max_depth=h, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape6[i,z]=c1       
        
        
#学习率=0.005        
mape7=np.zeros((3,4))
for i,j in enumerate([1000,2000,8000]):
    for z,h in enumerate([1,2,3,4]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=0.005, max_depth=h, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape7[i,z]=c1        
                
        
        
        
        
        
        