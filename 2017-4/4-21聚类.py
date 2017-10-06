# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:03:11 2017

@author: wutongshu
"""
import numpy as np
import pandas as pd
import seaborn as sns
chuxing=pd.read_csv(r'D:\python_data\2017-04\chuxing.csv',encoding='gbk')
chuxing1=np.array(chuxing.iloc[:,4])
from sklearn.cluster import KMeans
#from sklearn import preprocessing
#X_scale=preprocessing.MinMaxScaler()
#x_train=X_scale.fit_transform(chuxing1)
ylabel=KMeans(n_clusters=5,init='k-means++').fit(chuxing1)
aa=ylabel.labels_
cc=ylabel.cluster_centers_
cc1=X_scale.inverse_transform(cc)

gg=np.hstack((chuxing1,aa.reshape(-1,1)))
aa1=pd.DataFrame(gg)
aa1.iloc[:,-1].value_counts()


summed_kde = np.sum(chuxing.iloc[:,4], axis=0)
sns.distplot(chuxing.iloc[:,4], hist=False)
sns.kdeplot(chuxing.iloc[:,4], cumulative=True)
gh=np.cumsum(chuxing1)






import matplotlib.pyplot as plt
a2=plt.figure()
a2=plt.hist(chuxing1,500,histtype='step',cumulative=True)
