# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 17:49:31 2017

@author: wutongshu
"""
import pandas as pd


path1=r'E:\huawei\huaweiDataDeal\0716carQ2.csv'
path2=unicode(path1,"utf8")
data=pd.read_csv(path2)
data['5min']=data.iloc[:,0].apply(lambda x:int(x)/5)

data2=data.groupby([data['COLLECTADDRESS'],data['5min']])['Q'].sum()
#data2.unstack()
data3=data2.reset_index()

aa=data3.unstack()



aa=data3.pivot("COLLECTADDRESS", "5min", "Q")

f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(aa, annot=False, fmt="d", ax=ax)



path1=r'E:\huaweiDataDeal\0716carQ2.csv'
path2=unicode(path1,"utf8")
data=pd.read_csv(path2)
data['30min']=data.iloc[:,0].apply(lambda x:int(x)/30)

data2=data.groupby([data['COLLECTADDRESS'],data['30min']])['Q'].sum()
#data2.unstack()
data3=data2.reset_index()




plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
cmap=sns.light_palette("navy",as_cmap = True)
#cmap=sns.cubehelix_palette(rot=-.0)
#cmap=sns.color_palette("Blues",as_cmap = True)
aa=data3.pivot("COLLECTADDRESS", "30min", "Q")
aa.index=range(len(aa))
f, ax = plt.subplots(figsize=(16, 9))
sns.heatmap(aa, annot=False, fmt="d", cmap=cmap,ax=ax,yticklabels=30)
ax.set_xlabel(u'时间（单位：30分钟）')
ax.set_ylabel(u'卡口点位')
plt.savefig('d:/workday2.png',dpi=200) 




data4=pd.read_csv(r'C:\Users\wutongshu\Desktop\sz.csv')

data5=pd.merge(data4,data3,left_on=data4.Id,right_on=data3.COLLECTADDRESS,how='left',indicator=True)




import datetime

data6=data5[data5.iloc[:,-2]>0]
import datetime
data6['time']=data6.iloc[:,4].apply(lambda x:int(x)*datetime.timedelta(minutes =30)+pd.to_datetime('2017-05-13 00:00'))


data7=data6.iloc[:,[0,1,2,5,7]]

data7.to_csv(r'C:\Users\wutongshu\Desktop\sz3.csv')











path1=r'E:\huaweiDataDeal\0716carQ2.csv'
path2=unicode(path1,"utf8")
data=pd.read_csv(path2)
data['60min']=data.iloc[:,0].apply(lambda x:int(x)/60)

data2=data.groupby([data['COLLECTADDRESS'],data['60min']])['Q'].sum()
#data2.unstack()
data3=data2.reset_index()


data4=pd.read_csv(r'C:\Users\wutongshu\Desktop\sz.csv')

data5=pd.merge(data4,data3,left_on=data4.Id,right_on=data3.COLLECTADDRESS,how='left',indicator=True)




import datetime

data6=data5[data5.iloc[:,-2]>0]
import datetime
data6['time']=data6.iloc[:,4].apply(lambda x:int(x)*datetime.timedelta(minutes =60)+pd.to_datetime('2017-05-13 00:00'))


data7=data6.iloc[:,[0,1,2,5,7]]

data7.to_csv(r'C:\Users\wutongshu\Desktop\sz4.csv')




















data4=pd.read_csv(r'C:\Users\wutongshu\Desktop\sz.csv')

from pandas.tseries.offsets import Hour,Minute
minute=Minute()


data5=pd.merge(data4,data3,left_on=data4.Id,right_on=data3.COLLECTADDRESS,how='left',indicator=True)


#data5.iloc[:,4]= data5.iloc[:,4].astype(np.int)

data6=data5[data5.iloc[:,-2]>0]
import datetime
data6['time']=data6.iloc[:,4].apply(lambda x:int(x)*datetime.timedelta(minutes =5)+pd.to_datetime('2017-05-13 00:00'))


data7=data6.iloc[:,[0,1,2,5,7]]



data7.to_csv(r'C:\Users\wutongshu\Desktop\sz2.csv')
