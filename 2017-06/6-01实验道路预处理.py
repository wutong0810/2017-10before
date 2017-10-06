# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 20:30:40 2017

@author: Administrator
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *




#预处理,分车道
dataDeal1=loopDeal(match_total_final1,claneNum=[3,4,5])
dataDeal2=loopDeal(match_total_final2,claneNum=[1])
dataDeal3=loopDeal(match_total_final3,claneNum=[1,2,3,4])
dataDeal4=loopDeal(match_total_final4,claneNum=[1,2,3,4])








#处理成15min数据
data_15min1,freeV1=loop_15min(dataDeal1,num1=3)

data_15min2,freeV2=loop_15min(dataDeal2,num1=3)

data_15min3,freeV3=loop_15min(dataDeal3,num1=3)

data_15min4,freeV4=loop_15min(dataDeal4,num1=3)



























    a1=plt.figure()
    for i in range(28):
        a1=plt.subplot(5,7,i+1)
        a1=plt.plot(data_15min2[i][:,0],data_15min2[i][:,5])
        a1=plt.xlim(0,24)
        a1=plt.ylim(0,900)
#
#
#    a1=plt.figure()
#    for i in range(31):
#        a1=plt.subplot(5,7,i+1)
#        a1=plt.scatter(dataDeal3[i].iloc[:,1],dataDeal3[i].iloc[:,8])
#        a1=plt.xlim(0,86400)
#        a1=plt.ylim(0,1200)












#相关性分析，数据集主要包括其1.每天所处的时刻，2.星期，3.历史前4个的行程时间，4.历史前3个的行程时间，5.历史前2个的行程时间，6.历史前1个的行程时间
#7.上游路段1的前3个的行程时间，8.上游路段1的前2个的行程时间，9.上游路段1的前1个的行程时间，10.上游路段2的前3个的行程时间
#11.上游路段2的前2个的行程时间，12.上游路段2的前1个的行程时间，13.下游路段4的前3个行程时间，14.下游路段4的前2个行程时间，15.下游路段4的前1个的行程时间
#16.对应的行程时间

#相关性分析




















col_data=[]
for i in range(0,21):
    deal=np.zeros((96,19))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV2
            deal[j,10]=freeV2
            deal[j,11]=freeV2
            deal[j,12]=freeV4
            deal[j,13]=freeV4
            deal[j,14]=freeV4
            deal[j,15]=0
            deal[j,16]=0
            deal[j,17]=0
            deal[j,18]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link2[j-3,5]
            deal[j,10]=link2[j-2,5]
            deal[j,11]=link2[j-1,5]
            deal[j,12]=link4[j-3,5]
            deal[j,13]=link4[j-2,5]
            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j-3,5]-link3[j-4,5]
            deal[j,16]=link3[j-2,5]-link3[j-3,5]
            deal[j,17]=link3[j-1,5]-link3[j-2,5]
            deal[j,18]=link3[j,5]
    col_data.append(deal)    




total_corr=[]
for i in range(21):
    corr=np.zeros((1,16))
    c=col_data[i]
    for j in range(2,18):
        corr[0,j-2]=np.abs(computeCorrelation(c[:,j],c[:,18]))
    corr_med=pd.DataFrame(corr)
    total_corr.append(corr_med)


cc=pd.concat(total_corr, ignore_index=True)


#创建数据集

all_data=[]
for i in range(0,31):
    deal=np.zeros((96,16))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV2
            deal[j,10]=freeV2
            deal[j,11]=freeV2
            deal[j,12]=freeV4
            deal[j,13]=freeV4
            deal[j,14]=freeV4
            deal[j,15]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link2[j-3,5]
            deal[j,10]=link2[j-2,5]
            deal[j,11]=link2[j-1,5]
            deal[j,12]=link4[j-3,5]
            deal[j,13]=link4[j-2,5]
            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j,5]
    all_data.append(deal)    

    
    
    
    
    
    
    
    
    

train_data=[]
#得到训练数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为对应星期日，第10列当前时刻时间
for i in range(0,21):
    deal=np.zeros((96,16))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
#            deal[j,6]=freeV1
#            deal[j,7]=freeV1
#            deal[j,8]=freeV1
#            deal[j,9]=freeV2
#            deal[j,10]=freeV2
#            deal[j,11]=freeV2
#            deal[j,12]=freeV4
#            deal[j,13]=freeV4
#            deal[j,14]=freeV4
            deal[j,15]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
#            deal[j,6]=link1[j-3,5]
#            deal[j,7]=link1[j-2,5]
#            deal[j,8]=link1[j-1,5]
#            deal[j,9]=link2[j-3,5]
#            deal[j,10]=link2[j-2,5]
#            deal[j,11]=link2[j-1,5]
#            deal[j,12]=link4[j-3,5]
#            deal[j,13]=link4[j-2,5]
#            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j,5]
    train_data.append(deal)        
    
train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)
train_data2 = pd.concat(train_data1, ignore_index=True) 


#获取验证集，以调参
valid_data=[]
for i in range(21,25):
    deal=np.zeros((96,16))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
#            deal[j,6]=freeV1
#            deal[j,7]=freeV1
#            deal[j,8]=freeV1
#            deal[j,9]=freeV2
#            deal[j,10]=freeV2
#            deal[j,11]=freeV2
#            deal[j,12]=freeV4
#            deal[j,13]=freeV4
#            deal[j,14]=freeV4
            deal[j,15]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
#            deal[j,6]=link1[j-3,5]
#            deal[j,7]=link1[j-2,5]
#            deal[j,8]=link1[j-1,5]
#            deal[j,9]=link2[j-3,5]
#            deal[j,10]=link2[j-2,5]
#            deal[j,11]=link2[j-1,5]
#            deal[j,12]=link4[j-3,5]
#            deal[j,13]=link4[j-2,5]
#            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j,5]
    valid_data.append(deal) 




valid_data1=[]
for i in range(len(valid_data)):
    a=pd.DataFrame(valid_data[i])
    valid_data1.append(a)
valid_data2 = pd.concat(valid_data1, ignore_index=True) 


#获取验证集，以调参
test_data=[]
for i in range(25,31):
    deal=np.zeros((96,16))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV2
            deal[j,10]=freeV2
            deal[j,11]=freeV2
            deal[j,12]=freeV4
            deal[j,13]=freeV4
            deal[j,14]=freeV4
            deal[j,15]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link2[j-3,5]
            deal[j,10]=link2[j-2,5]
            deal[j,11]=link2[j-1,5]
            deal[j,12]=link4[j-3,5]
            deal[j,13]=link4[j-2,5]
            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j,5]
    test_data.append(deal) 




test_data1=[]
for i in range(len(test_data)):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)

    
    

test_data2 = pd.concat(test_data1, ignore_index=True) 

























