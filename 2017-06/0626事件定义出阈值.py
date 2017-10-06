# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:46:22 2017

@author: wutongshu
"""
dataDeal1=loopDeal(match_total_final1,claneNum=[2,3,4])
dataDeal2=loopDeal(match_total_final2,claneNum=[3,4,5,6])
dataDeal3=loopDeal(match_total_final3,claneNum=[1,2,3])



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#车道由内至外，1到最大值
import sys
sys.path.append(r'E:\Hisense\python_script\predict15min')
from all_func import *


dataTotal=[]
for i in range(len(dataDeal2)):
    data=np.zeros((288,7))
    data[:,0]=range(288)
    qTotal=rj_zyData[rj_zyData.iloc[:,-1]==(i+1204)]
    qTotal1=qTotal[qTotal.iloc[:,3]==1]
    tt=dataDeal2[i]
    for j in range(288):
        q5min=qTotal1[(qTotal1.iloc[:,-2]>300*j)&(qTotal1.iloc[:,-2]<300*(j+1))]
        q5min3=q5min[q5min.iloc[:,2]==3]
        q5min4=q5min[q5min.iloc[:,2]==4]
        q5min5=q5min[q5min.iloc[:,2]==5]
        q5min6=q5min[q5min.iloc[:,2]==6]
        tt1=tt[(tt.iloc[:,1]>300*j)&(tt.iloc[:,1]<300*(j+1))]
        if len(q5min3)>0:
            data[j,1]=len(q5min3)
        if len(q5min4)>0:
            data[j,2]=len(q5min4)
        if len(q5min5)>0:
            data[j,3]=len(q5min5)
        if len(q5min6)>0:
            data[j,4]=len(q5min6)
        if len(tt1)>0:
            data[j,5]=np.median(tt1.iloc[:,8])
            data[j,6]=np.mean(tt1.iloc[:,8])
    dataTotal.append(data)
        
   




import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.subplot(5,7,i+1)
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,1],'-o',label='q3')
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,2],'-o',label='q4')
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,3],'-o',label='q5')
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,4],'-o',label='q6')
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,5]*0.1,'-o',label='tt_medium')
#    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,6],'-o',label='tt_mean')
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,80)
    plt.legend()



import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
#plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.plot(dataTotal[i][:,0],dataTotal[i][:,5],'-o',markersize=5,label=str(i))
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,900)
    plt.legend()
    


dataAll=listConcat(dataTotal)
tt90=np.zeros((288,3))
tt90[:,0]=range(288)
for i in range(288):
    dataMedium=dataAll[dataAll[:,0]==i]
    tt90[i,1]=np.percentile(dataMedium[:,5],90)
    tt90[i,2]=np.percentile(dataMedium[:,6],90)



fig, ax = plt.subplots(figsize=(22,11))
a1=plt.plot( tt90[:,0], tt90[:,1],'-o',markersize=5,label='medium')
a1=plt.plot( tt90[:,0], tt90[:,2],'-o',markersize=5,label='mean')
a1=plt.xlim(0,288)
a1=plt.ylim(0,800)
plt.legend()















