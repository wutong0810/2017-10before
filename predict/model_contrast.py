# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:48:26 2017

@author: wutongshu
"""
train_data=[]
#得到训练数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为下游的t-2，第10列为下游的t-1,第11列为下游t-2时刻至t-1时刻的变化量
#第12列为对应星期日，第13列当前时刻时间
for i in range(21):
    deal=np.zeros((288,12))
    deal[:,0]=range(288)
    a=tt_deal_5min3[i]
    b=tt_deall_5min3[i]
    c=tt_deal3_5min3[i]
    for j in range(288):
        if j<4:
            deal[j,1]=65+10
            deal[j,2]=65+10
            deal[j,3]=65+10
            deal[j,4]=65+10
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=74
            deal[j,9]=74
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
    train_data.append(deal)            
        


train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)


train_data2 = pd.concat(train_data1, ignore_index=True) 


test_data=[]
#得到训练数据，第1列为时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据，第6列为下游前t-2数据
#第7列为t-4至t-3时刻的变化量，第8列为t-3至t-2时刻的变化量，第9列为t-2至t-1时刻的变化量
#第9列为下游的t-2，第10列为下游的t-1
#第11列为对应星期日，第12列当前时刻时间
for i in range(21,28):
    deal=np.zeros((288,12))
    deal[:,0]=range(288)
    a=tt_deal_5min3[i]
    b=tt_deall_5min3[i]
    c=tt_deal3_5min3[i]
    for j in range(288):
        if j<4:
            deal[j,1]=65+10
            deal[j,2]=65+10
            deal[j,3]=65+10
            deal[j,4]=65+10
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=74
            deal[j,9]=74
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
    test_data.append(deal)            

test_data1=[]
for i in range(7):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)


test_data2 = pd.concat(test_data1, ignore_index=True) 

#比较各个模型的参数
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR



from sklearn import preprocessing 
import numpy as np  
min_max_scaler = preprocessing.MinMaxScaler() 
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
X_train_minmax = min_max_scaler.fit_transform(train_x) 





gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  

rf1=RandomForestRegressor(n_estimators=300,max_features='sqrt',max_depth=4)
rf1.fit(train_x,train_y) 

svr_rbf = SVR(kernel='rbf', C=0.5, gamma=0.1)
svr_rbf.fit(X_train_minmax,train_y)
#模型比较
bijiao=np.zeros((7,3))
for i in range(7):
    test_med=test_data[i]
    test_x=np.array(test_med[:,:-1])
    test_y=np.array(test_med[:,-1])
    
    
    aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,0]=np.sum(aa3[:,2])/len(aa3)
    

    X_test_minmax =min_max_scaler.fit_transform(test_x) 
    aa1=np.hstack([test_y.reshape(-1,1), svr_rbf.predict(X_test_minmax).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])-0.08
    bijiao[i,1]=np.sum(aa3[:,2])/len(aa3)
    
    aa1=np.hstack([test_y.reshape(-1,1), rf1.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,2]=np.sum(aa3[:,2])/len(aa3)


























