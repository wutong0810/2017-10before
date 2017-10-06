# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:35:15 2017

@author: wutongshu
"""
import tt_match0202
import tt_deal0202
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def openfile(inpath1 = r"C:\Users\wutongshu\Desktop\贵阳数据\zh_zy1201-1215.csv", inpath2 = r"C:\Users\wutongshu\Desktop\贵阳数据\rj_zy1201-1215.csv"):
    uipath1 = unicode(inpath1 , "utf8")
    uipath2 = unicode(inpath2 , "utf8")
    down_data=pd.read_csv(uipath1,encoding='gbk')
    up_data=pd.read_csv(uipath2,encoding='gbk')
    down_data.iloc[:,1]=pd.to_datetime(down_data.iloc[:,1])
    up_data.iloc[:,1]=pd.to_datetime(up_data.iloc[:,1])
    down_data['day']=down_data.iloc[:,1].apply(lambda x:100*x.month+x.day)
    up_data['day']=up_data.iloc[:,1].apply(lambda x:100*x.month+x.day)
    down_data['sj']=down_data.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    up_data['sj']=up_data.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    day_num=down_data.day.unique()
    return down_data,up_data,day_num



#将数据中需要的属性提取出来并且排序
#加载文件
down_data1,up_data1,day_num1=openfile()
down_data2=down_data1.iloc[:,[0,7,4,5,6]]
up_data2=up_data1.iloc[:,[0,7,4,5,6]]
match_total_tt=[]
match_total_final=[]
match_total_rate=[]
#匹配车牌行程时间，按天分别匹配
for i in day_num1:
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=tt_match0202.match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=3)        
    match_total_tt.append(match_tt)
    match_total_final.append(match_final)
    match_total_rate.append(match_rate)

#绘制数据图
a0=plt.figure()
for i in range(15):
    a0=plt.subplot(5,3,i+1)
#    a0=plt.scatter(match_total_final[i].iloc[:,1],match_total_final[i].iloc[:,9],s=15)
    a0=plt.scatter(tt_deal[i].iloc[:,1],tt_deal[i].iloc[:,8],s=15)
    a0=plt.xlim(0,86400)

tt_deal=[]
for i in range(15):
    test=match_total_final[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
    med_data=np.array(test)
    match_du=med_data
    med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8)
    tt_deal.append(med_deal)
a0=plt.figure()
for i in range(15):
    a0=plt.subplot(5,3,i+1)
#    a0=plt.scatter(match_total_final[i].iloc[:,1],match_total_final[i].iloc[:,9],s=15)
    a0=plt.scatter(tt_deal[i].iloc[:,1],tt_deal[i].iloc[:,8],s=15)
    a0=plt.xlim(0,86400)    

    