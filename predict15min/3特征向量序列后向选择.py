# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 21:52:11 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\exp')
from all_func import *
train_data=[]
for i in range(0,18):
    deal=np.zeros((96,22))
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
            deal[j,5]=freeV2
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV3
            deal[j,10]=freeV3
            deal[j,11]=freeV3
            deal[j,12]=0
            deal[j,13]=0
            deal[j,14]=0
            if j<=1:
                deal[j,15]=0
                deal[j,16]=0
                deal[j,17]=0
                deal[j,18]=0
                deal[j,19]=0
                deal[j,20]=0
            else :
                deal[j,15]=q[j-2,2]
                deal[j,16]=q[j-1,2]
                deal[j,17]=q[j-2,3]
                deal[j,18]=q[j-1,3]
                deal[j,19]=q[j-2,2]-q[j-2,3]
                deal[j,20]=q[j-1,2]-q[j-1,3]
            deal[j,21]=link2[j,5]
        else :
            deal[j,2]=link2[j-4,5]
            deal[j,3]=link2[j-3,5]
            deal[j,4]=link2[j-2,5]
            deal[j,5]=link2[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link3[j-3,5]
            deal[j,10]=link3[j-2,5]
            deal[j,11]=link3[j-1,5]
            deal[j,12]=link2[j-3,5]-link2[j-4,5]
            deal[j,13]=link2[j-2,5]-link2[j-3,5]
            deal[j,14]=link2[j-1,5]-link2[j-2,5]
            deal[j,15]=q[j-2,2]
            deal[j,16]=q[j-1,2]
            deal[j,17]=q[j-2,3]
            deal[j,18]=q[j-1,3]
            deal[j,19]=q[j-2,2]-q[j-2,3]
            deal[j,20]=q[j-1,2]-q[j-1,3]
            deal[j,21]=link2[j,5]
    train_data.append(deal)     
train_data1=[]
for i in range(18):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)
train_data2 = pd.concat(train_data1, ignore_index=True)     
    
 



valid_data=[]
for i in range(18,21):
    deal=np.zeros((96,22))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    q=q_total2[i]
    deal[:,1]=(i+2)%7
    for j in range(288):
        if j<4:
            deal[j,2]=freeV2
            deal[j,3]=freeV2
            deal[j,4]=freeV2
            deal[j,5]=freeV2
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV3
            deal[j,10]=freeV3
            deal[j,11]=freeV3
            deal[j,12]=0
            deal[j,13]=0
            deal[j,14]=0
            if j<=1:
                deal[j,15]=0
                deal[j,16]=0
                deal[j,17]=0
                deal[j,18]=0
                deal[j,19]=0
                deal[j,20]=0
            else :
                deal[j,15]=q[j-2,2]
                deal[j,16]=q[j-1,2]
                deal[j,17]=q[j-2,3]
                deal[j,18]=q[j-1,3]
                deal[j,19]=q[j-2,2]-q[j-2,3]
                deal[j,20]=q[j-1,2]-q[j-1,3]
            deal[j,21]=link2[j,5]
        else :
            deal[j,2]=link2[j-4,5]
            deal[j,3]=link2[j-3,5]
            deal[j,4]=link2[j-2,5]
            deal[j,5]=link2[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link3[j-3,5]
            deal[j,10]=link3[j-2,5]
            deal[j,11]=link3[j-1,5]
            deal[j,12]=link2[j-3,5]-link2[j-4,5]
            deal[j,13]=link2[j-2,5]-link2[j-3,5]
            deal[j,14]=link2[j-1,5]-link2[j-2,5]
            deal[j,15]=q[j-2,2]
            deal[j,16]=q[j-1,2]
            deal[j,17]=q[j-2,3]
            deal[j,18]=q[j-1,3]
            deal[j,19]=q[j-2,2]-q[j-2,3]
            deal[j,20]=q[j-1,2]-q[j-1,3]
            deal[j,21]=link2[j,5]
    valid_data.append(deal)   

valid_data1=[]
for i in range(len(valid_data)):
    a=pd.DataFrame(valid_data[i])
    valid_data1.append(a)
valid_data2 = pd.concat(valid_data1, ignore_index=True)  



gbm0 = RandomForestRegressor(n_estimators=180, min_samples_split=10,\
                                      min_samples_leaf=20,max_depth=11,max_features='sqrt',random_state=0)  
import copy
Mape1=np.zeros((1,15))
Vector=[]
minMape=1
index=0
total=range(15)
for i in range(14):
    minMape=1
    for j in total:
        total1=copy.deepcopy(total)
        total1.remove(j)
        train_x1=np.array(train_data2.iloc[:,:-1])
        train_y=np.array(train_data2.iloc[:,-1])
        train_x=train_x1[:,total1]
        test_x1=np.array(valid_data2.iloc[:,:-1])
        test_x=test_x1[:,total1]
        test_y=np.array(valid_data2.iloc[:,-1])
        gbm0.fit(train_x,train_y)
        aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
#        print c1
        if c1<minMape:
#            mapechange=True
            minMape=c1
            index=j
    Mape1[0,i]=minMape
#    if mape
    total.remove(index) 
    total2=copy.deepcopy(total)
    Vector.append(total2)





   