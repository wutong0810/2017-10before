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

#车牌统计车辆数
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



dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\0817数据清洗后2.0\0801-0810车牌每天被检测到次数',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
dataFinal=pd.concat(dataAll, ignore_index=True)
dataFinal.columns=['year','month','day','car','N']   
dataFinal=dataFinal[(dataFinal.iloc[:,2]>=1)&(dataFinal.iloc[:,2]<=9)&(dataFinal.iloc[:,1]<=8)&(dataFinal.iloc[:,0]<=2017)]


dataFinal2=dataFinal.sort_values(by=["year","month","day","N"],ascending=False)

carTimeAvg=dataFinal2.groupby(['car'],as_index=False)['N'].mean()

carTimes=carTimeAvg.sort_values(by=["N"],ascending=False)

timesTop=carTimes.head(30)


data01=dataFinal2[(dataFinal2.iloc[:,2]==1)]



calNum=np.zeros((600,2))
data01_1=np.array(data01)
total=0
for i in range(600):
    calNum[i,0]=i
    t=len(data01_1[data01_1[:,4]==i])
    total=t+total
    calNum[i,1]=total
    
    
    
    
#绘制各个月的变化图
import matplotlib as mpl
mpl.rc('xtick', labelsize=20) 
mpl.rc('ytick', labelsize=20) 

sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(19*0.6,9*0.8))
plt.plot(calNum[:,0],calNum[:,1])
plt.xlabel(u'检测次数', fontsize=28)
plt.ylabel(u'累积车辆数', fontsize=28)
ax.set_xscale("log")
plt.savefig(r'd:/deal.jpg',dpi=200)     
    



wrongNum=carTimes[carTimes.N>600]





#统计每天的错误识别率
rate=np.zeros((9,3))
for i in range(1,10):
    testMedium=dataFinal2[dataFinal2.iloc[:,2]==i]
    rate[i-1,0]=i
    rate[i-1,1]=len(testMedium)
    num=0
    for j in wrongNum:
        tt=testMedium[testMedium.iloc[:,3]==j]['N']
        if len(tt)>0:
            num=num+tt.iloc[0]
    rate[i-1,2]=num





#处理各卡口数据质量

dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\滴滴数据质量评估\0817数据清洗后2.0\每天流量数据',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
dataFinal=pd.concat(dataAll, ignore_index=True)


dataFinal.columns=['city','time','kakou_no','direct','flow','lane','year','month','day']


dataFinal.time=pd.to_datetime(dataFinal.time)


dataFinal['sj']=dataFinal.time.apply(lambda x:int(x.minute+60*x.hour)/5)


data01=dataFinal[dataFinal.iloc[:,-2]==1]

data01.ix[:,'30min']=data01['sj'].apply(lambda x:int(x)/6)

data01_1=data01.groupby([data01['kakou_no'],data01['direct']])['lane'].nunique()

data3=data01_1.reset_index()


a=data3.groupby([data3['kakou_no']],as_index=False)['lane'].sum()


data2=data01.groupby([data01['kakou_no'],data01['30min']],as_index=False)['flow'].sum()


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









test=data4[data4.kakou_no==3701033057]
test=dataFinal[(dataFinal.kakou_no==3701033057)&(dataFinal.direct==2)]
test=test.sort_values(by=['sj','day'])
test.ix[:,'30min']=test['sj'].apply(lambda x:int(x)/6)

test2=test.groupby([test['kakou_no'],test['day'],test['30min']],as_index=False)['flow'].sum()

test2=test2.sort_values(by=['30min','day'])
















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












#车身颜色

dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\最新数据质量评估报告\0801车身颜色',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
carColor=pd.concat(dataAll, ignore_index=True)

carColor.columns=['year','month','day','car','color','N']

carTotal=carColor.groupby(['car'],as_index=False)['N'].sum()

carMax=carColor.groupby(['car'],as_index=False)['N'].max()


carFinal=pd.merge(carTotal,carMax,on='car')
float(np.sum(carFinal.N_y))/np.sum(carFinal.N_x)





dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\最新数据质量评估报告\0801车牌颜色识别',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
carColor=pd.concat(dataAll, ignore_index=True)

carColor.columns=['year','month','day','car','color','N']

carTotal=carColor.groupby(['car'],as_index=False)['N'].sum()

carMax=carColor.groupby(['car'],as_index=False)['N'].max()


carFinal=pd.merge(carTotal,carMax,on='car')
float(np.sum(carFinal.N_y))/np.sum(carFinal.N_x)






dataPath=pathGet(path1=r'C:\Users\wutongshu\Desktop\最新数据质量评估报告\0801检测到车辆品牌',dataFomat='.csv')
dataAll=[]
for i in dataPath:
    a=pd.read_csv(i,header=None)
    dataAll.append(a)
carColor=pd.concat(dataAll, ignore_index=True)

carColor.columns=['year','month','day','car','color','N']

carTotal=carColor.groupby(['car'],as_index=False)['N'].sum()

carMax=carColor.groupby(['car'],as_index=False)['N'].max()


carFinal=pd.merge(carTotal,carMax,on='car')
float(np.sum(carFinal.N_y))/np.sum(carFinal.N_x)
















