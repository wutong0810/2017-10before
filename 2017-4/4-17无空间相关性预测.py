# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:12:03 2017

@author: wutongshu
"""
#未使用空间相关性的预测精度
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
train_x1=np.array(train_data2.iloc[:,:8])
train_y1=np.array(train_data2.iloc[:,-1])
gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x1,train_y1)  
bijiao=np.zeros((7,1))
for i in range(7):
    test_med=test_data[i]
    test_x=np.array(test_med[:,:8])
    test_y=np.array(test_med[:,-1])
    
    
    aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,0]=np.sum(aa3[:,2])/len(aa3)