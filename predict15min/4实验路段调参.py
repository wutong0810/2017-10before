# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 22:09:42 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation, metrics


#数据集主要包括其1.每天所处的时刻，2.星期，3.历史前3个的行程时间，4.历史前2个的行程时间，5.历史前1个的行程时间
#6.上游路段1的前1个的行程时间，
#7.历史前3个时间窗至前2个时间窗的行程时间变化量；
#8.历史前2个时间窗至前1个时间窗的行程时间变化量；
#9.历史前2个时间窗的驶入量
#10.历史前1个时间窗的驶入量
#11.历史前2个时间窗的驶出量
#12.历史前1个时间窗的驶出量
#13.对应的行程时间


train_data=[]
for i in range(0,21):
    deal=np.zeros((96,13))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    q=q_total2[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV2
            deal[j,3]=freeV2
            deal[j,4]=freeV2
            deal[j,5]=freeV1
            deal[j,6]=0
            deal[j,7]=0
            if j<=1:
                deal[j,8]=0
                deal[j,9]=0
                deal[j,10]=0
                deal[j,11]=0
            else :
                deal[j,8]=q[j-2,2]
                deal[j,9]=q[j-1,2]
                deal[j,10]=q[j-2,3]
                deal[j,11]=q[j-1,3]
            deal[j,12]=link2[j,5]
        else :
            deal[j,2]=link2[j-3,5]
            deal[j,3]=link2[j-2,5]
            deal[j,4]=link2[j-1,5]
            deal[j,5]=link1[j-1,5]
            deal[j,6]=link2[j-2,5]-link2[j-3,5]
            deal[j,7]=link2[j-1,5]-link2[j-2,5]
            deal[j,8]=q[j-2,2]
            deal[j,9]=q[j-1,2]
            deal[j,10]=q[j-2,3]
            deal[j,11]=q[j-2,3]
            deal[j,12]=link2[j,5]
    train_data.append(deal)


train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)

train_data2 = pd.concat(train_data1, ignore_index=True) 




#获得测试集  
test_data=[]
for i in range(21,28):
    deal=np.zeros((96,13))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    q=q_total2[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV2
            deal[j,3]=freeV2
            deal[j,4]=freeV2
            deal[j,5]=freeV1
            deal[j,6]=0
            deal[j,7]=0
            if j<=1:
                deal[j,8]=0
                deal[j,9]=0
                deal[j,10]=0
                deal[j,11]=0
            else :
                deal[j,8]=q[j-2,2]
                deal[j,9]=q[j-1,2]
                deal[j,10]=q[j-2,3]
                deal[j,11]=q[j-1,3]
            deal[j,12]=link2[j,5]
        else :
            deal[j,2]=link2[j-3,5]
            deal[j,3]=link2[j-2,5]
            deal[j,4]=link2[j-1,5]
            deal[j,5]=link1[j-1,5]
            deal[j,6]=link2[j-2,5]-link2[j-3,5]
            deal[j,7]=link2[j-1,5]-link2[j-2,5]
            deal[j,8]=q[j-2,2]
            deal[j,9]=q[j-1,2]
            deal[j,10]=q[j-2,3]
            deal[j,11]=q[j-2,3]
            deal[j,12]=link2[j,5]
    test_data.append(deal) 


test_data1=[]
for i in range(7):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)
test_data2 = pd.concat(test_data1, ignore_index=True)   





train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])

param_test1 = {'n_estimators':range(20,300,10)}
gsearch1 = GridSearchCV(estimator =RandomForestRegressor( min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=4,max_features='sqrt',random_state=10) , 
                       param_grid = param_test1,iid=False,scoring='neg_mean_squared_error',cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


#得到最优的树的棵树为130







param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(50,120,20)}
gsearch2 =  GridSearchCV(estimator =RandomForestRegressor( n_estimators= 130\
                                      ,min_samples_leaf=20,max_features='sqrt',random_state=10) , 
                       param_grid = param_test2,iid=False,scoring='neg_mean_squared_error',cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_

# 最优参数{'max_depth':9, 'min_samples_split': 50},








































