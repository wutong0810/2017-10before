# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 22:34:18 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *



train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])






#分别计算MAPE
Mape=np.zeros((1,7))
Rmse=np.zeros((1,7))
gbm0 = RandomForestRegressor(n_estimators=130, min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=9,max_features='sqrt',random_state=10)  
gbm0.fit(train_x,train_y)
for i in range(7):
    test_x=np.array(test_data2.iloc[96*i:96*(i+1),:-1])
    test_y=np.array(test_data2.iloc[96*i:96*(i+1),-1])
    
    aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    aa4=(aa1[:,0]-aa1[:,1])**2
    c1=np.sum(aa3[:,2])/len(aa3)
#    print aa4
    Mape[0,i]=c1
    Rmse[0,i]=np.sqrt(np.sum(aa4)/len(aa3))






#得到预测精度及结果
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
gbm0 = RandomForestRegressor(n_estimators=130, min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=9,max_features='sqrt',random_state=10)    
gbm0.fit(train_x,train_y)
aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
aa3=np.hstack([aa1,aa2.reshape(-1,1)])
c1=np.sum(aa3[:,2])/len(aa3)




state=pd.DataFrame(aa3)
#state['true']=state.iloc[:,0].apply(lambda x:max(1-68.3/x,0))
#state['predict']=state.iloc[:,1].apply(lambda x:max(1-68.3/x,0))
state['true1']=state.iloc[:,0].map(stateMap)
state['predict1']=state.iloc[:,1].map(stateMap)


fig, ax = plt.subplots(2,4,figsize=(18,10))
for i in range(7):
    plt.subplot(2,4,i+1)
    plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,0],'o-',markersize=3,label='true') 
    plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,1],'o-',markersize=3,label='predict')
    plt.legend()
    plt.ylim(0,700)
plt.savefig('F:\python_script\data_deal/predict_result.png',dpi=200) 



fig, ax = plt.subplots(2,4,figsize=(18,10))
for i in range(7):
    plt.subplot(2,4,i+1)
    plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,3],'o-',markersize=3,label='true') 
    plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,4],'o-',markersize=3,label='predict')
    plt.legend()
    plt.ylim(0,4)
plt.savefig('F:\python_script\data_deal/predict_result_state.png',dpi=200) 







