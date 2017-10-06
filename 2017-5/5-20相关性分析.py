# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:30:01 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *



#相关性分析



test_data=[]
#特征工程构建，寻找相关性，第1列为时间，第2列为前t-5数据，第3列为前t-4数据，第4列为前t-3数据，第5列为为前t-2数据，第6列为为前t-1数据，第7列为当前时刻时间
for i in range(0,21):
    deal=np.zeros((96,7))
    deal[:,0]=range(96)
    b=tt_deal_5min6_1[i]
    for j in range(96):
        if j<5:
            deal[j,1]=65
            deal[j,2]=65
            deal[j,3]=65
            deal[j,4]=65
            deal[j,5]=65
            deal[j,6]=65
        else :
            deal[j,1]=b[j-5,5]
            deal[j,2]=b[j-4,5]
            deal[j,3]=b[j-3,5]
            deal[j,4]=b[j-2,5]
            deal[j,5]=b[j-1,5]
            deal[j,6]=b[j,5]
    test_data.append(deal)    

total_corr=[]
for i in range(21):
    corr=np.zeros((1,6))
    c=test_data[i]
    for j in range(1,6):
        corr[0,j]=np.abs(computeCorrelation(c[:,j],c[:,6]))
    corr_med=pd.DataFrame(corr)
    total_corr.append(corr_med)
    

corr_total=pd.concat(total_corr, ignore_index=True)




















































