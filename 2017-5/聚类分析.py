# -*- coding: utf-8 -*-
"""
Created on Tue May 16 09:39:31 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from pandasql import sqldf












Clustering=pd.read_csv(r'F:\python_data\2017-5\julei.csv',encoding='gbk')
Clustering1=Clustering.iloc[:,[1,3,5]]
Clustering2=np.array(Clustering1)

ylabels=KMeans(n_clusters=5,init='k-means++').fit(Clustering2)

Label=ylabels.labels_
Center=ylabels.cluster_centers_

guodu=np.hstack((Clustering,Label.reshape(-1,1)))
final=pd.DataFrame(guodu)
commute=final[final.iloc[:,-1]==3]
commute.columns=['carnumber','total_times','id','appear','d_id','d_times','labels']


pysqldf = lambda q: sqldf(q, globals())
pysqldf("SELECT count(*) FROM commute t where t.carnumber like '贵%' ;")





commute.iloc[:,[0,-1]].to_csv(r'f:\label.csv',index=False,encoding='utf-8')





Label1=pd.DataFrame(Label)

Label1.iloc[:,0].value_counts()
