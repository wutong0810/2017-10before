# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 12:00:00 2017

@author: wutongshu
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import numpy as np



#加载数据
file1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\0817数据清洗后数据质量\0817评估数据总量.csv'
file2=unicode(file1,'utf-8')
q_total=pd.read_csv(file2,header=None)
q_total.columns=['year','month','day','N']



#绘制各个月的变化图
import matplotlib as mpl
mpl.rc('xtick', labelsize=20) 
mpl.rc('ytick', labelsize=20) 

sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(19*0.6,9*0.8))
sns.boxplot(x=q_total.month,y=q_total.N,data=q_total,linewidth = 2.5)
plt.xlabel('Month', fontsize=28)
plt.ylabel('sum', fontsize=28)
plt.savefig(r'd:/deal.jpg',dpi=200) 

#读取所有文件路径
def pathGet(path1=r'E:\华为数据\测试',dataFomat='.txt'):
    path2=unicode(path1,"utf8")
    filename_total=[]
    for dirpath, dirnames, filenames in os.walk(path2):
        for filename in filenames:
            if os.path.splitext(filename)[1]==dataFomat:
                filename2=os.path.join(dirpath,filename)
    #            print filename2
                filename_total.append(filename2) 
    return filename_total







#读取数据



dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\0817数据清洗后数据质量\车辆数统计distinct',dataFomat='.csv')


dataAll=[]
for i in dataPath:
       test=pd.read_csv(i,header=None) 
       dataAll.append(test)
dataFinal=pd.concat(dataAll, ignore_index=True) 
dataFinal.columns=['year','month','day','car','N']   

dataFinal2=dataFinal.sort(["year","month","day","N"],ascending=False)




















dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\0817数据清洗后数据质量\分车道数据',dataFomat='.csv')


dataAll=[]
for i in dataPath:
       test=pd.read_csv(i,header=None) 
       dataAll.append(test)
dataFinal=pd.concat(dataAll, ignore_index=True) 

