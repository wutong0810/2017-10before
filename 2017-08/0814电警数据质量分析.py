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


file1=r'E:\data\滴滴数据\数据质量评估\济南市数据总量.csv'
file2=unicode(file1,'utf-8')
q_total=pd.read_csv(file2,encoding='gbk')
q_total.columns=['year','month','day','N']
#q_total.choose
sns.boxplot(x=q_total.month,y=q_total.N,data=q_total)



import matplotlib as mpl
mpl.rc('xtick', labelsize=20) 
mpl.rc('ytick', labelsize=20) 

#mpl.rc('xlabel', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
#planets = sns.load_dataset("planets")
fig, ax = plt.subplots(figsize=(19*0.6,9*0.8))
sns.boxplot(x=q_total.month,y=q_total.N,data=q_total,linewidth = 2.5)
plt.xlabel('Month', fontsize=28)
plt.ylabel('sum', fontsize=28)
plt.savefig(r'd:/deal.jpg',dpi=200) 



a1=q_total[(q_total.iloc[:,1]==7)&(q_total.iloc[:,2]>=19)&(q_total.iloc[:,2]<=31)]
a2=q_total[(q_total.iloc[:,1]==8)&(q_total.iloc[:,2]>=1)&(q_total.iloc[:,2]<=14)]
a3=pd.concat([a1,a2])
#计算合理范围外的数据
a3.iloc[:,3].quantile(0.25)
a3.iloc[:,3].quantile(0.75)
R=1.7*(a3.iloc[:,3].quantile(0.75)-a3.iloc[:,3].quantile(0.25))
z1=a3.iloc[:,3].quantile(0.25)-R
z2=a3.iloc[:,3].quantile(0.75)+R
i=0
j=0
for z in range(226):
    if q_total.iloc[z,3]<z1:
        i=i+1
    elif q_total.iloc[z,3]>z2:
        j=j+1



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



dataPath=pathGet(path1=r'E:\data\滴滴数据\数据质量评估\job_id=2686299_dir',dataFomat='.csv')


dataAll=[]
for i in dataPath:
       test=pd.read_csv(i,header=None) 
       dataAll.append(test)
dataFinal=pd.concat(dataAll, ignore_index=True) 
dataFinal.columns=['year','month','day','car','N']   

dataFinal2=dataFinal.sort(["year","month","day","N"],ascending=False)




data01=dataFinal2[dataFinal2.iloc[:,2]==1]


data02=dataFinal2[dataFinal2.iloc[:,2]==2]

data03=dataFinal2[dataFinal2.iloc[:,2]==3]


day01Top=data01.head(30)
day02Top=data02.head(30)
day03Top=data03.head(30)





carTimeAvg=dataFinal2.groupby(['car'],as_index=False)['N'].mean()


carTimes=carTimeAvg.sort(["N"],ascending=False)





c=carTimes.head(30)







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



dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\评估新表的数据\2017年每天分车道流量',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
dataFinal=pd.concat(dataAll, ignore_index=True)


dataFinal.columns=['city','time','kakou_no','direct','flow','lane','year','month','day']

#dataFinal2=dataFinal.sort_values(by=['kakou_no','time','direct','lane'])

dataFinal2

dataFinal.time=pd.to_datetime(dataFinal.time)


dataFinal['sj']=dataFinal.time.apply(lambda x:int(x.minute+60*x.hour)/5)



dataFinal2=dataFinal.sort_values(by=['sj','kakou_no','direct','lane'])



data01=dataFinal[dataFinal.iloc[:,-2]==1]

data01['30min']=data01['sj'].apply(lambda x:int(x)/6)[:]




data01_1=data01.groupby([data01['kakou_no'],data01['direct']],as_index=False)['lane'].nunique()

data3=data01_1.reset_index()


a=data3.groupby([data3['kakou_no']],as_index=False)['lane'].sum()






data2=data01.groupby([data01['kakou_no'],data01['30min']],as_index=False)['flow'].sum()
#data2.unstack()
#data3=data2.reset_index()



data4=pd.merge(data2,a,on='kakou_no')

data4['avg']=data4['flow']/data4['lane']



plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
cmap=sns.light_palette("navy",as_cmap = True)
#cmap=sns.cubehelix_palette(rot=-.0)
#cmap=sns.color_palette("Blues",as_cmap = True)
aa=data4.pivot('kakou_no', "30min", 'avg')
aa.index=range(len(aa))
f, ax = plt.subplots(figsize=(16, 9))
sns.heatmap(aa, annot=False, fmt="d", cmap='rainbow',ax=ax,vmax=400,vmin=0,yticklabels=40)
ax.set_xlabel(u'时间（单位：30分钟）')
ax.set_ylabel(u'卡口点位')


vmax=40,vmin=0,center=30






a=dataFinal2[dataFinal2.iloc[:,2]==3701022114]


a1=a.sort_values(by=['sj','direct','lane'])


