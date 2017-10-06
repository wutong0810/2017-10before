# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:14:49 2016

@author: 梧桐叔
"""
import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
def data_deal(match_time):
    match_time1=np.array(match_time)
    for i in range(4,24*60):
        time_wd=(i-4)*60
        time_wu=(i+1)*60
        data_medium=match_time1[(match_time1[:,1]>time_wd)&(match_time1[:,1]<time_wu)]
        if len(data_medium)>0:                        
            up_quantile=np.percentile(data_medium[:,3],75)
            down_quantile=np.percentile(data_medium[:,3],25)
            R=up_quantile-down_quantile
            up_limit=1.5*R+up_quantile
            down_limit=-1.5*R+down_quantile
            down_limit1=min(down_limit,40)
            indice=np.where((match_time1[:,1]>time_wd)&(match_time1[:,1]<time_wu)&((match_time1[:,3]>up_limit)|(match_time1[:,3]<down_limit)))
            match_time1[indice,3]=-1
    match_tf=pd.DataFrame(match_time1)
    match_tf1=match_tf[match_tf.iloc[:,3]>-1]
    return match_tf1

    
def data_deal2(data,r=0.2,sample=45):
    scalar=StandardScaler()
    scalar.fit(data)
    data1=scalar.transform(data)
    db = DBSCAN(eps=r, min_samples=sample).fit(data1)
    data3=db.components_
    data4=scalar.inverse_transform(data3)
    return data4
data=pd.read_csv('D:/script/2016-12/data/matchi_time316.csv',encoding='gbk')  
data1=data.iloc[:,[2,10]]
a1=figure()
a1=plt.scatter(data1.iloc[:,0],data1.iloc[:,1])
a1=plt.xlim(0,86400)

a1=figure()
a1=plt.plot(data1.iloc[:,0],marker='o')


#63182,63207
aa=data1[(data1.iloc[:,0]>63182)&(data1.iloc[:,0]<63207)]
a1=figure()
a1=sns.distplot(aa.iloc[:,1])

#62884,62909(比较好的数据)
aa=data1[(data1.iloc[:,0]>62884)&(data1.iloc[:,0]<62909)]
a1=figure()
a1=sns.distplot(aa.iloc[:,1])








    
    
