# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:30:13 2017

@author: wutongshu
"""



import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR



from sklearn import preprocessing 
import numpy as np  
min_max_scaler = preprocessing.MinMaxScaler() 
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
X_train_minmax = min_max_scaler.fit_transform(train_x) 


svr_rbf = SVR(kernel='rbf', C=0.5, gamma=0.1)
import datetime
starttime = datetime.datetime.now()
svr_rbf.fit(X_train_minmax,train_y)
endtime = datetime.datetime.now()
print endtime-starttime
#2.065s




import datetime
starttime = datetime.datetime.now()
rf1=RandomForestRegressor(n_estimators=180,max_features='sqrt',max_depth=4,random_state=10)
rf1.fit(train_x,train_y) 
endtime = datetime.datetime.now()
print endtime-starttime
#1.158s




import datetime
starttime = datetime.datetime.now()
gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  
endtime = datetime.datetime.now()
print endtime-starttime
#1.237s







#绘制工作日与非工作日数据
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(5,5))
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.plot(tt_deall_5min3[23][:,0],tt_deall_5min3[23][:,5],'--',label=u'12月27日-休息日') 
plt.plot(tt_deall_5min3[21][:,0],tt_deall_5min3[21][:,5],'-',label=u'12月25日-工作日') 
plt.subplots_adjust(left=0.15, bottom=0.14, top=0.88,right=0.93) 
plt.xlim(0,289)
plt.ylim(0,500)
plt.legend(loc=2, fontsize=13)
ax.set_xlabel(u'时间',fontsize=13)
ax.set_ylabel(u'行程时间/(s)',fontsize=13) 
sns.despine()       
plt.savefig('d:/picture/workday.png',dpi=200) 


a=np.zeros((4,2))
a[:,0]=range(1,5)
a[0,1]=1.23
a[1,1]=2.06
a[2,1]=1.15
a[3,1]=0.88

#绘制工作日与非工作日数据
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(5,5))
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.bar(a[:,0],a[:,1],width=0.5)
#plt.plot(tt_deall_5min3[23][:,0],tt_deall_5min3[23][:,5],'--',label=u'12月27日-休息日') 
#plt.plot(tt_deall_5min3[21][:,0],tt_deall_5min3[21][:,5],'-',label=u'12月25日-工作日') 
plt.subplots_adjust(left=0.16, bottom=0.11, top=0.91,right=0.95) 
plt.text(0.85, 1.26, r"1.23", fontsize=13, color="black")
plt.text(2-0.15, 2.09, r"2.06", fontsize=13, color="black")
plt.text(3-0.15, 1.18, r"1.15", fontsize=13, color="black")
plt.text(4-0.15, 0.91, r"0.88", fontsize=13, color="black")
#plt.xlim(0,289)
plt.ylim(0,2.5)
#plt.legend(loc=2, fontsize=13)
#ax.set_xlabel(u'时间',fontsize=13)
ax.set_ylabel(u'运行时间/s',fontsize=13)
xticks=['GBRT','SVM','RF','ARIMA']
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(["$%s$" % y for y in xticks], fontsize=12)
#ax.set_ylabel(u'行程时间/(s)',fontsize=13) 
sns.despine()       
plt.savefig('d:/workday.png',dpi=200) 
