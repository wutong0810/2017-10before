# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 13:11:14 2017

@author: 梧桐叔
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def openfile(inpath1 = r"D:\qq下载\2267974368\FileRecv\青云路数据\青云路下游0316-0322电警数据.csv", inpath2 = r"D:\qq下载\2267974368\FileRecv\青云路数据\青云路上游0316-0322电警数据.csv"):
    uipath1 = unicode(inpath1 , "utf8")
    uipath2 = unicode(inpath2 , "utf8")
    down_data=pd.read_csv(uipath1,encoding='gbk')
    up_data=pd.read_csv(uipath2,encoding='gbk')
    down_data.iloc[:,2]=pd.to_datetime(down_data.iloc[:,2])
    up_data.iloc[:,2]=pd.to_datetime(up_data.iloc[:,2])
    down_data['day']=down_data.iloc[:,2].apply(lambda x:100*x.month+x.day)
    up_data['day']=up_data.iloc[:,2].apply(lambda x:100*x.month+x.day)
    down_data['sj']=down_data.iloc[:,2].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    up_data['sj']=up_data.iloc[:,2].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    day_num=down_data.day.unique()
    return down_data,up_data
    
    
down_data3,up_data3=openfile()
down_data1=down_data3[down_data3.day==316]
up_data1=up_data3[up_data3.day==316]
down_data2=down_data1.iloc[:,[1,7,4,5]]
up_data2=up_data1.iloc[:,[1,7,4,5]]
down_data2.loc[:,'car_type']=0
up_data2.loc[:,'car_type']=0
down_data2.columns=range(5)
up_data2.columns=range(5)
down_data=down_data2
up_data=up_data2


def match_traveltime(up_data,down_data,maxtime,mintime,down_direction):
    down_data=down_data[down_data.iloc[:,3]==down_direction]
    down_data.index=range(len(down_data))
#筛选正常数据，异常数据主要为未识别和无牌，因此数据位数都不为7
    down_data['car_length']=down_data.iloc[:,0].apply(lambda x:len(x))
    down_true=down_data[down_data.iloc[:,5]==7]
    down_true.index=range(len(down_true))
#计算下游识别率
    plate_identify_rate1=float(len(down_true))/len(down_data)
#同理筛选上游正常数据，异常数据主要为未识别和无牌，因此数据位数都不为7
    up_data['car_length']=up_data.iloc[:,0].apply(lambda x:len(x))
    up_true=up_data[up_data.iloc[:,5]==7]
    up_true.index=range(len(up_true))
#计算上游识别率
    plate_identify_rate2=float(len(up_true))/len(up_data)
#初始化最终的大矩阵match_du，上游的车牌先进行排序
    up_true1=np.array(up_true)
    up_true.loc[:,'down_t']=np.nan
    up_true.loc[:,'down_clane']=np.nan
    up_true.loc[:,'down_direct']=np.nan
    up_true.loc[:,'down']=0
    match_du=np.array(up_true)
    down_true=down_true.sort_values(by=1)
    down_true1=np.array(down_true)
#    搜索上游在合理时间范围内的车牌数据
    for i in range(len(up_true)):
        t_min=up_true1[i,1]+mintime
        t_max=up_true1[i,1]+maxtime
        down_medium=down_true1[(down_true1[:,1]>t_min)&(down_true1[:,1]<t_max)]
        m=len(down_medium)
#       如果存在，则匹配车牌信息，并计算行程时间，一旦匹配上则跳出循环
        if m>0:           
            for j in range(m-1,-1,-1):
                if (cmp(match_du[i,0],down_medium[j,0])==0):
                    match_du[i,6]=down_medium[j,1]
                    match_du[i,7]=down_medium[j,2]
                    match_du[i,8]=down_medium[j,3]
                    match_du[i,9]=-(match_du[i,1]-down_medium[j,1])
                    break
#    将匹配好的大矩阵按车牌，和下游过程时刻排序，去掉重复匹配的车牌
    match_time=pd.DataFrame(match_du)
    match_time=match_time.sort_values(by=[0,1])
    match_time.index=range(len(match_time))
    match_time1=np.array(match_time)
    indice=[]
#阈值设置为100s
    for h in range(2,len(match_time1)):
        if (cmp(match_time1[h,0],match_time1[h-1,0])==0)& (match_time1[h,1]-match_time1[h-1,1]<100):
            indice.append(h-1)
#给行程时间付上-1来标示行程时间
    for i in indice:
        match_time1[i,9]=-1
#筛选出正常的数据
    match_time2=match_time1[match_time1[:,9]>-1]
    match_tt=pd.DataFrame(match_time2)
#重新按下游过车时刻来排序
    match_tt=match_tt.sort_values(by=[1,0])
#修改索引
    match_tt.index=range(len(match_tt))
#    计算下匹配率
    match_final=match_tt[match_tt.iloc[:,9]>0]
    match_final.columns=['car_num','d_time','d_clane','d_direction','car_type','num_length','u_time','u_clane','u_direction','tt']
    match_rate=float(len(match_final))/len(match_du)
    return match_tt,match_final,match_rate


match_1=match_tt[((match_tt.iloc[:,3]==3)&((match_tt.iloc[:,2]==3)|(match_tt.iloc[:,2]==4)|(match_tt.iloc[:,2]==5)))|((match_tt.iloc[:,3]==2)&(match_tt.iloc[:,2]==1))]

def match_rate_function(match_tt):                 
    a=match_tt[((match_tt.iloc[:,3]==3)&((match_tt.iloc[:,2]==3)|(match_tt.iloc[:,2]==4)|(match_tt.iloc[:,2]==5)))] 
    b=match_tt[((match_tt.iloc[:,3]==2)&(match_tt.iloc[:,2]==1))]              
    match_f= pd.concat([a,b],ignore_index=True)
    count=0
    for i in range(0,len(match_f),30):
        count=count+1
    match_rate2=np.zeros((count,2)) 
    count=0
    for i in range(0,len(match_f),30):
        medium=match_f.iloc[i:(i+30),:]
        match_m=medium[medium.iloc[:,9]>0]
        num=len(match_m)
        match_rate2[count,0]=num/30.
        match_rate2[count,1]=num
        count=count+1
    return match_rate2,match_f
    





down_data3,up_data3=openfile()
day_num=down_data3.day.unique()
match_rate_total=[]
match_total=[]
for i in day_num:
    down_data1=down_data3[down_data3.day==i]
    up_data1=up_data3[up_data3.day==i]
    down_data2=down_data1.iloc[:,[1,7,4,5]]
    up_data2=up_data1.iloc[:,[1,7,4,5]]
    down_data2['car_type']=0
    up_data2['car_type']=0
    down_data2.columns=range(5)
    up_data2.columns=range(5)
    match_tt,match_final,match_rate=match_traveltime(up_data2,down_data2,maxtime=900,mintime=50,down_direction=3)
    match_total.append(match_tt)
    match_rate2,match_f=match_rate_function(match_tt)
    match_rate_total.append(match_rate2)
    

match_rate_total=[]
for i in range(8):
    match_tt=match_total[i]
    match_rate2,match_f=match_rate_function(match_tt)
    match_rate_total.append(match_rate2)
    
ax=plt.figure()
for i in range(8):
    plt.plot(match_rate_total[i][:,1],marker='o')
    plt.legend(['316','317','318','319','320','321','322'])
    plt.plot(match_rate_total[0][:,1])
    plt.plot(match_rate_total[1][:,1],marker='o')
    plt.plot(match_rate_total[2][:,1],marker='o')
    plt.plot(match_rate_total[3][:,1],marker='o')
#    plt.plot(match_rate_total[4][:,1],marker='o')
#    plt.plot(match_rate_total[5][:,1],marker='o')
#    plt.plot(match_rate_total[6][:,1],marker='o')
#    plt.plot(match_rate_total[7][:,1],marker='o')
    
    

        
    
    
    

    
    
    
    
    
    
    
    
    
    