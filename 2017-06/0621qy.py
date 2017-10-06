# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:01:28 2017

@author: wutongshu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#车道由内至外，1到最大值
import sys
sys.path.append(r'E:\Hisense\python_script\exp')
from all_func import *




#上游
inpath1=r'E:\Hisense\qyRoad\青云路上游0316-0322电警数据.csv'
inpath2=r'E:\Hisense\qyRoad\青云路下游0316-0322电警数据.csv'



uipath1 = unicode(inpath1 , "utf8")
uipath2 = unicode(inpath2 , "utf8")



qyRoadUp=pd.read_csv(uipath1 ,encoding='gbk')
qyRoadUp1=qyRoadUp.iloc[:,[1,2,4,5,0]]
qyRoadUpData,qyRoadUpDayNum=dataTran(qyRoadUp1)



qyRoadDown=pd.read_csv(uipath2 ,encoding='gbk')
qyRoadDown1=qyRoadDown.iloc[:,[1,2,4,5,0]]
qyRoadDownData,qyRoadDownDayNum=dataTran(qyRoadDown1)


match_total_tt1,match_total_final1,match_total_rate1=loopMatch(downData=qyRoadDownData,upData=qyRoadUpData,dayNum=qyRoadDownDayNum,maxtime1=900,mintime1=35,down_direction1=3)



#预处理,分车道
dataDeal1=loopDeal(match_total_final1,claneNum=[1,2,3,4])


T5minFinal=[]
for j in range(len(qyRoadDownDayNum)):
    dealData1=dataDeal1[j]
    Tt5min=np.zeros((288,3))
    Tt5min[:,0]=range(288)
    for i in range(288):
        medTravel=dealData1[(dealData1.iloc[:,1]>i*300)&(dealData1.iloc[:,1]<(i+1)*300)]
        if len(medTravel)>0:
            Tt5min[i,1]=np.median(medTravel.iloc[:,8])
            Tt5min[i,2]=np.mean(medTravel.iloc[:,8])
    T5minFinal.append(Tt5min)








qyRoadDown1=qyRoadDown.iloc[:,[1,2,4,5,0]]
q_total=downQ(qyRoadDown1,3,[1,2,3,4],qyRoadDownDayNum)


#驶入驶出流量统计函数，参数1为上游交叉口，参数2为下游交叉口，参数3为上游交叉口驶入方向1，参数4为上游交叉口驶入方向1的驶入车道
#参数5为上游交叉口驶入方向2，参数6为上游交叉口驶入方向2的驶入车道
#参数7为下游驶出方向1，参数8为下游交叉口的驶出方向1的驶出车道,参数9为下游交叉口的驶出方向1的驶出车道匹配统计的车道
#返回数组是第1列是时间，第2列为驶入量，第3列为驶出量，第4列为匹配车道的过车流量
def downQ(downInsec,downDire,downClane,dayNum):
    downInsec.iloc[:,1]=pd.to_datetime(downInsec.iloc[:,1])
    downInsec['day']=downInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    downInsec['sj']=downInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    q_total=[]
    for i in dayNum:
        med_data=np.zeros((288,len(downClane)+1))
        med_data[:,0]=range(288)
#       排序,按车道再按时间
#        驶出车道流量
        out_q=downInsec[downInsec.iloc[:,5]==i]
        out_q['repair']=0
        
        cache_total3=[]
        cache1=out_q[out_q.iloc[:,3]==downDire]
        for g in downClane:
            in_Q=cache1[cache1.iloc[:,2]==g]
            cache_total3.append(in_Q)
        out_q1=pd.concat(cache_total3, ignore_index=True)
		#按照车道、时间排序
        out_q1=out_q1.sort_values(by=[out_q1.columns[2],out_q1.columns[6]])
		#剔除掉重复匹配的车辆，防止一辆车被多次检测到
        out_q1Final=removeFun(out_q1)
        for j in range(288):
            medData=out_q1Final[(out_q1Final.iloc[:,-2]>j*5*60)&(out_q1Final.iloc[:,-2]<(j+1)*5*60)]
            for h in range(len(downClane)):
                med_data[j,h+1]=len(medData[medData.iloc[:,2]==h+1])
        q_total.append(med_data)    
    return q_total






import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(8):
    TT=T5minFinal[i]
    Q=q_total[i]
    a1=plt.subplot(2,4,i+1)
    a1=plt.plot(TT[:,0],TT[:,1]*0.1,label='medium')
    a1=plt.plot(Q[:,0],Q[:,1],label='Q1')
    a1=plt.plot(Q[:,0],Q[:,2],label='Q2')
    a1=plt.plot(Q[:,0],Q[:,3],label='Q3')
    a1=plt.plot(Q[:,0],Q[:,4],label='Q4')
    plt.legend()
    a1=plt.xlim(0,288)
#    a1=plt.ylim(0,900)



sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
TT=T5minFinal[i]
Q=q_total[i]
#a1=plt.subplot(2,4,i+1)
a1=plt.plot(TT[:,0],TT[:,1]*0.1,'-o',label='medium')
a1=plt.plot(Q[:,0],Q[:,1],'-o',label='Q1')
a1=plt.plot(Q[:,0],Q[:,2],'-o',label='Q2')
a1=plt.plot(Q[:,0],Q[:,3],'-o',label='Q3')
a1=plt.plot(Q[:,0],Q[:,4],'-o',label='Q4')
plt.legend()
a1=plt.xlim(0,288)
#a1=plt.ylim(0,900)









