# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:45:58 2017

@author: wutongshu
"""
#特征向量提取
#计算相关性系数
import sys
sys.path.append('D:\python_script\predict')
from all_func import *


test_data=[]
#特征工程构建，寻找相关性，第1列为时间，第2列为前t-5数据，第3列为前t-4数据，第4列为前t-3数据，第5列为为前t-2数据，第6列为为前t-1数据
#第7列为上游的t-4，第8列为上游的t-3，第9列为上游的t-2，第10列为上游的t-1，
#第11列为下游的t-4，第12列为下游的t-3，第13列为下游的t-2，第14列为下游的t-1，第15列当前时刻时间
for i in range(0,21):
    deal=np.zeros((288,15))
    deal[:,0]=range(288)
    a=tt_deal_5min2[i]#上游
    b=tt_deall_5min2[i]#中游
    c=tt_deal3_5min2[i]#下游
    for j in range(288):
        if j<5:
            deal[j,1]=65+12
            deal[j,2]=65+12
            deal[j,3]=65+12
            deal[j,4]=65+12
            deal[j,5]=65+12
            deal[j,6]=65+12
            deal[j,7]=65+12
            deal[j,8]=65+12
            deal[j,9]=65+12
            deal[j,10]=65+12
            deal[j,11]=65+12
            deal[j,12]=65+12
            deal[j,13]=65+12
            deal[j,14]=b[j,5]
        else :
            deal[j,1]=b[j-5,5]
            deal[j,2]=b[j-4,5]
            deal[j,3]=b[j-3,5]
            deal[j,4]=b[j-2,5]
            deal[j,5]=b[j-1,5]
            deal[j,6]=a[j-4,5]
            deal[j,7]=a[j-3,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=c[j-4,5]
            deal[j,11]=c[j-3,5]
            deal[j,12]=c[j-2,5]
            deal[j,13]=c[j-1,5]
            deal[j,14]=b[j,5]
    test_data.append(deal)    








#计算相关性

total_corr=[]
for i in range(21):
    corr=np.zeros((1,14))
    c=test_data[i]
    for j in range(1,14):
        corr[0,j]=np.abs(computeCorrelation(c[:,j],c[:,14]))
    corr_med=pd.DataFrame(corr)
    total_corr.append(corr_med)
    

cc=pd.concat(total_corr, ignore_index=True)