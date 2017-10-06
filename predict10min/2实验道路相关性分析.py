# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 21:06:57 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\exp')
from all_func import *





#实验路段相关性分析




#相关性分析，数据集主要包括其1.每天所处的时刻，2.星期，3.历史前4个的行程时间，4.历史前3个的行程时间，5.历史前2个的行程时间，6.历史前1个的行程时间
#7.上游路段1的前3个的行程时间，8.上游路段1的前2个的行程时间，9.上游路段1的前1个的行程时间，10.下游路段3的前3个的行程时间
#11.下游路段3的前2个的行程时间，12.下游路段3的前1个的行程时间，13.历史前4个时间窗至前3个时间窗的行程时间变化量；
#13.历史前4个时间窗至前3个时间窗的行程时间变化量；14.历史前3个时间窗至前2个时间窗的行程时间变化量；15.历史前2个时间窗至前1个时间窗的行程时间变化量
#16.历史前2个时间窗的路段驶入量
#17.历史前1个时间窗的路段驶入量
#18.历史前2个时间窗的路段驶出量
#19.历史前1个时间窗的路段驶出量
#20.历史前2个时间窗的路段累计量
#21.历史前1个时间窗的路段累计量
#22.对应的行程时间
col_data=[]
for i in range(0,21):
    deal=np.zeros((288,22))
    deal[:,0]=range(288)
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
    col_data.append(deal)    
    
    
total_corr=[]
for i in range(21):
    corr=np.zeros((1,21))
    c=col_data[i]
    for j in range(0,21):
        corr[0,j]=np.abs(computeCorrelation(c[:,j],c[:,21]))
    corr_med=pd.DataFrame(corr)
    total_corr.append(corr_med)


corTotal=pd.concat(total_corr, ignore_index=True)    
    
    
    
    