# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:09:01 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a=pd.read_csv(r'F:\python_data\first_using.csv',encoding='gbk')
b=pd.read_csv(r'F:\python_data\first_appear.csv',encoding='gbk')
#plt.hist(a.iloc[:,-1])



#绘制第一次出行从同一地点低于5次的图，其每个月使用的分布图
fig,ax=plt.subplots()
sns.distplot(a.iloc[:,-1],hist=False)
plt.xlim(0,25)


#绘制使用频度图
fig,ax=plt.subplots()
plt.hist(a.iloc[:,-1],bins=20)




#绘制使用第一次出行图
fig,ax=plt.subplots()
plt.hist(b.iloc[:,-1])