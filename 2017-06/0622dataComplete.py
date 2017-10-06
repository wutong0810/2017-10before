# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 10:44:20 2017

@author: wutongshu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#车道由内至外，1到最大值
import sys
sys.path.append(r'E:\Hisense\python_script\exp')
from all_func import *



#随机选择数据
    
    
def listConcat(data):
    medDataFinal=data[0]
    for i in range(1,len(data)):
        medDataFinal=np.vstack([medDataFinal,data[i]])
    return medDataFinal



a=listConcat(data_15min2)
b=a[a[:,6]==1]
c=b[(b[:,0]>0)&(b[:,0]<28)]







#绘制补全数据分布
a1=plt.figure()
sns.distplot(b[:,0],bins=50,kde=False, rug=False)



import random
random.seed(a=50)
oril=range(2688)
cc=np.where([a[:,0]>24])[1]
orial2=random.sample(cc,100)
aa=np.zeros((100,7))
for i in range(100):
    j=orial2[i]
    if (a[j,6]==0)&(a[j-1,6]==0)&(a[j-2,6]==0)&(a[j-3,6]==0):
        aa[i,5]=1
        aa[i,0]=a[j,0]
        aa[i,1]=a[j,1]
        aa[i,2]=a[j-1,1]
        aa[i,3]=a[j-2,1]
        aa[i,4]=a[j-3,1]
        aa[i,6]=np.mean(aa[i,2:5])
bb=aa[aa[:,5]==1]
np.sqrt(np.sum(((np.abs(bb[:,6]-bb[:,1]))**2))/len(bb))




























