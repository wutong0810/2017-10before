# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:41:02 2017

@author: wutongshu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


timeRange=pd.read_csv(r'E:\huaweiDataDeal\0716carTimes1.csv',encoding='gbk')

timeRange1=timeRange[timeRange.iloc[:,1]<250]


a=np.zeros((202,4))
for i in range(202):
    a[i,0]=i
    a[i,1]=len(timeRange1[timeRange1.iloc[:,1]==i])    
    
    
a[:,2]=np.cumsum(a[:,1])

a[:,3]=a[:,2]/len(timeRange1)









path1=r'D:\huaweiDeal\数据可视化/timesDis.png'
path2=unicode(path1,"utf8") 


sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(19,9))
plt.plot(a[:,0],a[:,3])
plt.ylim(0,1.01)
ax.set_xlabel(u'检测次数/次',fontsize=13)
ax.set_ylabel(u'所占百分比',fontsize=13)
sns.despine() 
plt.savefig(path2,dpi=200) 
















