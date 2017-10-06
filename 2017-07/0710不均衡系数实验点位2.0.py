# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:25:47 2017

@author: wutongshu
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os
import re


#计算点位信息数据
def matrixCal(x,y):
    m=(x-1)*28+y
    return m
def listConcat(data):
    medDataFinal=data[0]
    for i in range(1,len(data)):
        medDataFinal=np.vstack([medDataFinal,data[i]])
    return medDataFinal   

pos=[7,11,8,14,6,23,26]
mat=np.zeros((84,3))
for i in range(7):
    for j in range(7):
        if i==j:
            pass
        else :
            mat[7*i+j,0]=pos[i]
            mat[7*i+j,1]=pos[j]
            mat[7*i+j,2]=matrixCal(pos[i],pos[j])

c=mat[mat[:,2]>0]

#读取所有行程时间，取出自由流速度
path1=r'D:\Data\数据\2017-07\20170703宏观态势数据\预处理后数据\selecetData'
path2=unicode(path1,"utf8")
filename_total=[]
for dirpath, dirnames, filenames in os.walk(path2):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.csv':
            filename2=os.path.join(dirpath,filename)
#            print filename2
            filename_total.append(filename2)     

totalV=[]
for i in filename_total:
    print i
    data=np.loadtxt(i,delimiter=',')
    nn=np.zeros((len(data),1))
    regex=re.compile(r'tt[0-9]{3}')
    findData=re.findall(regex,i)
    print findData
    number=int(findData[0][2:])
    nn[:]=int(findData[0][2:])
    data1=np.hstack([data,nn.reshape(-1,1)])
#    data2=data1[data1[:,5]>0]
    totalV.append(data1)


#取自由流行程时间，得到自有流速度
freeTime=[]
L=[426,900,426,720,700,900,320,720,320,500,500,500]
for i in range(12):
    dataMedium=totalV[i]
    print  totalV[i][0,-1]
    dataNight=dataMedium[(dataMedium[:,0]>0)&(dataMedium[:,0]<3600*6)]
    freeTime.append(L[i]/np.percentile(dataNight[:,5],20)*3.6)
    print L[i]/np.percentile(dataNight[:,5],20)*3.6


#计算各区间行程时间
totalV3=[]
L=[426,900,426,720,700,900,320,720,320,500,500,500]
for i in range(12):
    dataMedium=totalV[i]
    datafinal=np.zeros((96,3))
    datafinal[:,0]=range(96)
    for j in range(96):
        dataM=dataMedium[(dataMedium[:,0]>3*300*j)&(dataMedium[:,0]<3*300*(j+1))]
        if len(dataM)>3:
            datafinal[j,1]=L[i]/np.mean(dataM[:,5])*3.6
            datafinal[j,2]=L[i]/np.median(dataM[:,5])*3.6
    totalV3.append(datafinal)
    
    
#补全数据，均值计算       
for i in range(12):
    for j in range(96):
        if j<4*6: 
            if totalV3[i][j,1]==0:
                totalV3[i][j,1]=freeTime[i]
        else:
            if totalV3[i][j,2]==0:
                print i,j
                totalV3[i][j,1]=np.mean(totalV3[i][j-3:j,1])
            
  

#补全数据,中位数       
for i in range(12):
    for j in range(96):
        if j<4*6: 
            if totalV3[i][j,2]==0:
                totalV3[i][j,2]=freeTime[i]
        else:
            if totalV3[i][j,2]==0:
                print i,j
                totalV3[i][j,2]=np.mean(totalV3[i][j-3:j,2])
            
            
            
            

#计算拥堵系数
totalV4=[]      
for i in range(12):
    dataV=1-totalV3[i][:,1]/freeTime[i]
    t=np.hstack([totalV3[i],dataV.reshape(-1,1)])
    totalV4.append(t)
    
#计算拥堵系数，用中位数计算      

totalV4=[]      
for i in range(12):
    dataV=1-totalV3[i][:,2]/freeTime[i]
    t=np.hstack([totalV3[i],dataV.reshape(-1,1)])
    totalV4.append(t) 
    
    
    
#不均衡系数负数的变为0
for i in range(12):
    for j in range(96):
        if totalV4[i][j,3]<0:
            totalV4[i][j,3]=0    
    
    
    
#数据整合   
dataFinal=listConcat(totalV4)    
#计算均衡系数
unbalance=np.zeros((96,2))
for i in range(96):
    dataMedium1=dataFinal[dataFinal[:,0]==i] 
    dataMedium2=dataMedium1[:,3]
    dataMedium3=np.sort(dataMedium2)
    dataMedium4=np.cumsum(dataMedium3, dtype=float) 
    dataMedium5=dataMedium4/np.sum(dataMedium3)
    unbalance1=1-1*(1/float(len(dataMedium5)))*(2*np.sum(dataMedium5[:-1])+1)
    unbalance[i,0]=i/4.
    unbalance[i,1]=unbalance1    
    
    
#绘图
a2=plt.figure()
for i in range(12):
    a2=plt.subplot(4,3,i+1)
    a2=plt.plot(totalV3[i][:,0]/4.,totalV3[i][:,2])   
    a2=plt.xlim(0,24)
    a2=plt.ylim(0,60)  


#绘图
a2=plt.figure()
for i in range(12):
#    a2=plt.subplot(4,3,i+1)
    a2=plt.plot(totalV4[i][:,0]/4.,totalV4[i][:,3])   
    a2=plt.xlim(2,6)
    a2=plt.ylim(0,1)  

a2=plt.figure()
for i in range(12):
#    a2=plt.subplot(4,3,i+1)
    a2=plt.plot(totalV4[i][:,0]/4.,pd.Series(totalV4[i][:,3]).map(state))   
    a2=plt.xlim(0,24)
    a2=plt.ylim(0,5)  






a3=plt.figure()
plt.plot(unbalance[:,0],unbalance[:,1])
plt.xlim(0,24)
plt.ylim(0,0.8) 



#原始数据
a2=plt.figure()
for i in range(12):
    a2=plt.subplot(4,3,i+1)
    a2=plt.scatter(totalV[i][:,0],totalV[i][:,5],s=10)   
    a2=plt.xlim(0,86400)
    a2=plt.ylim(0,800)      
    
    
    
def listHConcat(data):
    medDataFinal=data[0]
    for i in range(1,len(data)):
        medDataFinal=np.hstack([medDataFinal,data[i]])
    return medDataFinal 

def state(x):
    if (x>=0)&(x<0.2):
        y=0
    elif (x>=0.2)&(x<0.4):
        y=1
    elif (x>=0.4)&(x<0.6):
        y=2
    elif (x>=0.6)&(x<0.8):
        y=3
    elif x>=0.8:
        y=4
    return y




totalV5=[]
for i in range(12):
    totalV5.append(totalV3[i][:,[2]])
dataTotal=listHConcat(totalV5)      
path1=r'D:\Data\数据\2017-07\20170703宏观态势数据\预处理后数据\selecetData\s.csv'
path2=unicode(path1,"utf8")
np.savetxt(path2,dataTotal,delimiter=',')    
    
    



totalV6=[]
for i in range(12):
    totalV6.append(totalV4[i][:,[3]])
dataTotal=listHConcat(totalV6)      
path1=r'D:\Data\数据\2017-07\20170703宏观态势数据\预处理后数据\selecetData\s.csv'
path2=unicode(path1,"utf8")
np.savetxt(path2,dataTotal,delimiter=',')   






























    
    
    
    
    
    
    
    
    
    
    