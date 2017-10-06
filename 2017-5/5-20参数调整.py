# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:48:54 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
#方向：1北，3南进口道，2西进口，4东进口道
#读写交叉口信息
#青云路与兴关路
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *







tt_deal_5min6_1=tt_deal3_5min3
#获取训练集
train_data=[]
#得到训练数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为对应星期日，第10列当前时刻时间
for i in range(18):
    deal=np.zeros((96,10))
    deal[:,0]=range(96)
    b=tt_deal_5min6_1[i]
    for j in range(96):
        if j<4:
            deal[j,1]=65
            deal[j,2]=65
            deal[j,3]=65
            deal[j,4]=65
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
    train_data.append(deal)            
        


train_data1=[]
for i in range(18):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)


train_data2 = pd.concat(train_data1, ignore_index=True) 






















#获取验证集，以调参
valid_data=[]
#得到验证数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为对应星期日，第10列当前时刻时间
for i in range(19,24):
    deal=np.zeros((96,10))
    deal[:,0]=range(96)
    b=tt_deal_5min6_1[i]
    for j in range(96):
        if j<4:
            deal[j,1]=65
            deal[j,2]=65
            deal[j,3]=65
            deal[j,4]=65
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
    valid_data.append(deal)            
        


valid_data1=[]
for i in range(18):
    a=pd.DataFrame(train_data[i])
    valid_data1.append(a)


valid_data2 = pd.concat(train_data1, ignore_index=True) 




#1在固定以下参数下进行树的棵树调整，min_samples_split=70,min_samples_leaf=20,max_depth=8


minMape,minPam,MAPE=gridSearch(train_data=train_data2,valid_data=valid_data2,pamater=range(20,300,20))
#最佳棵树180
minPam






#2.得到另外两个参数的最优结果    

#'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)

pam1=range(3,20,2)
pam2=range(5,201,20)

MAPE2=np.zeros((len(pam1),len(pam2)))
minMape=1
minPam1=0
minPam2=0
for z,h in enumerate(pam1):
    for i,j in enumerate(pam2):
        gbm0 = RandomForestRegressor(n_estimators=180, min_samples_split=j,\
                                      min_samples_leaf=20,max_depth=h,max_features='sqrt',random_state=0)    
        gbm0.fit(train_x,train_y)
        aa1=np.hstack([valid_y.reshape(-1,1), gbm0.predict(valid_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        MAPE2[z,i]=c1 

        if c1<minMape:
            minMape=c1
            minPam1=z
            minPam2=i
pam1[minPam1]
#11
pam2[minPam2]    
#50



test_data=[]
#得到验证数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为对应星期日，第10列当前时刻时间
for i in range(24,31):
    deal=np.zeros((96,10))
    deal[:,0]=range(96)
    b=tt_deal_5min6_1[i]
    for j in range(96):
        if j<4:
            deal[j,1]=65
            deal[j,2]=65
            deal[j,3]=65
            deal[j,4]=65
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
    test_data.append(deal)          


test_data1=[]
for i in range(len(test_data)):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)


test_data2 = pd.concat(test_data1, ignore_index=True) 

train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])



gbm0 = RandomForestRegressor(n_estimators=180, min_samples_split=10,\
                                      min_samples_leaf=20,max_depth=11,max_features='sqrt',random_state=0)    
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


def stateMap(x):
    c=0
    if (x>=0)&(x<=0.4):
        c=0
    elif (x>0.4)&(x<=0.75):
        c=1
    elif x>0.75:
        c=2
    return c

    fig, ax = plt.subplots(2,4,figsize=(6,5))
    for i in range(7):
        plt.subplot(2,4,i+1)
        plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,3],'o-',markersize=3,label='true') 
        plt.plot(np.linspace(0,24,96),state.iloc[i*96:(i+1)*96,4],'o-',markersize=3,label='predict')
        plt.legend()
#        xticks =range(0,25)
#        ax[i].set_xticks(xticks)
#        ax[i].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
#        plt.xlim(0,24.1)
#        plt.ylim(0,900) 


































































#    
#    
#MAPE=np.zeros((1,len(pamater)))
#    train_x=np.array(train_data.iloc[:,:-1])
#    train_y=np.array(train_data.iloc[:,-1])
#    valid_x=np.array(valid_data.iloc[:,:-1])
#    valid_y=np.array(valid_data.iloc[:,-1])
#    for i,j in enumerate(pamater):
#        gbm0 = RandomForestRegressor(n_estimators=j, min_samples_split=100,\
#                                      min_samples_leaf=20,max_depth=8,max_features='sqrt')  
#        gbm0.fit(train_x,train_y)
#        aa1=np.hstack([valid_y.reshape(-1,1), gbm0.predict(valid_x).reshape(-1,1)])
#        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
#        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
#        c1=np.sum(aa3[:,2])/len(aa3)
#        minMape=1
#        minPam=0
#        if c1<minMape:
#            minMape=c1
#            minPam=i
#        MAPE[0,i]=c1    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
#    gbm0.fit(X_train,y_train) 
#    aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
#    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
#    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
#    c1=np.sum(aa3[:,2])/len(aa3)
#    mape1[z,i]=c1
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#















































































import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation, metrics



train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
param_test1 = {'n_estimators':range(20,400,10)}
gsearch1 = GridSearchCV(estimator = RandomForestRegressor(min_samples_split=100,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt'), 
                       param_grid = param_test1,scoring='neg_mean_squared_error', iid=False,cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


#360



param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)}
gsearch2 = GridSearchCV(estimator =RandomForestRegressor(n_estimators= 360, 
                                  min_samples_leaf=20,max_features='sqrt' ),
   param_grid = param_test2, scoring='neg_mean_squared_error',iid=False, cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_


#({'max_depth': 13, 'min_samples_split': 50}, -2925.5893609052123)














train_data=[]
#得到训练数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为对应星期日，第10列当前时刻时间
for i in range(7):
    deal=np.zeros((96,10))
    deal[:,0]=range(96)
    b=tt_deal_5min6_1[i]
    for j in range(96):
        if j<4:
            deal[j,1]=65
            deal[j,2]=65
            deal[j,3]=65
            deal[j,4]=65
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=b[j,4]
            deal[j,9]=b[j,5]
    train_data.append(deal)            
        


train_data1=[]
for i in range(7):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)


train_data2 = pd.concat(train_data1, ignore_index=True) 



import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation, metrics



train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
param_test1 = {'n_estimators':range(20,400,10)}
gsearch1 = GridSearchCV(estimator = RandomForestRegressor(min_samples_split=100,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt'), 
                       param_grid = param_test1,scoring='neg_mean_squared_error', iid=False,cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


#360



param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(50,201,20)}
gsearch2 = GridSearchCV(estimator =RandomForestRegressor(n_estimators= 360, 
                                  min_samples_leaf=20,max_features='sqrt' ),
   param_grid = param_test2, scoring='neg_mean_squared_error',iid=False, cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_

#({'max_depth': 13, 'min_samples_split': 50}, -2925.5893609052123)













train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
param_test1 = {'n_estimators':range(20,400,10)}
gsearch1 = GridSearchCV(estimator = RandomForestRegressor(min_samples_split=100,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt'), 
                       param_grid = param_test1,scoring='neg_mean_squared_error', iid=False,cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_




























param_test4 = {'learning_rate':[0.001,0.005,0.01,0.1,1]}
gsearch4 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=80,max_depth=9, min_samples_leaf =40, 
               min_samples_split =500, subsample=0.8, random_state=10), 
                       param_grid = param_test4, iid=False, cv=5)
gsearch4.fit(train_x,train_y)
gsearch4.best_params_ 


param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(100,801,200)}
gsearch2 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=180, min_samples_leaf=20, 
      max_features='sqrt', subsample=0.8, random_state=10), 
   param_grid = param_test2,iid=False, cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_


























