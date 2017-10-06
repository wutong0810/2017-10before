# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 16:40:36 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#车道由内至外，1到最大值
import sys
sys.path.append(r'F:\python_script\exp')
from all_func import *
#type={'挂车','军队用大型汽车','武警用大型汽车','大型汽车','教练汽车','警用汽车','军队用小型汽车','武警用小型汽车','小型汽车','未识别'};
#type={'15','28','30','01','16','23','29','31','02','41'}，多了一个27,-澳门汽车


#<1>第1步加载所有数据

#1.瑞金-新华路
rj_xh=pd.read_csv(r'F:\data_final\6-13exp_data\rj_xh1201-1231.csv',encoding='utf-8')
rj_xhData,rj_xhDayNum=dataTran(rj_xh)



#2.瑞金-兴关路
rj_xg=pd.read_csv(r'F:\data_final\6-13exp_data\rj_xg1201-1231.csv',encoding='utf-8')
rj_xgData,rj_xgDayNum=dataTran(rj_xg)



#3.瑞金-遵义路
rj_zy=pd.read_csv(r'F:\data_final\6-13exp_data\rj_zy1201-1231.csv',encoding='utf-8')
rj_zyData,rj_zyDayNum=dataTran(rj_zy)



#4.瑞金-雪涯路,注意这条路的方向标注出现错误，下游驶出方向对应的是4
rj_xy=pd.read_csv(r'F:\data_final\6-13exp_data\rj_xy1201-1231.csv',encoding='utf-8')
rj_xyData,rj_xyDayNum=dataTran(rj_xy)




#<2>第2步统计每条路段的驶入驶出，以及下游路段的流量：
q_total1=inOut(upInsec=rj_xh,downInsec=rj_xg,upDire1=1,upClane1=[2,3,4],upDire2=3,upClane2=[1,2],downDire=1,downClane1=[1,2,3,4],downClane2=[2,3,4])
q_total2=inOut(upInsec=rj_xg,downInsec=rj_zy,upDire1=1,upClane1=[2,3,4],upDire2=3,upClane2=[1,2],downDire=1,downClane1=[1,2,3,4,5,6],downClane2=[3,4,5,6])
q_total3=inOut(upInsec=rj_zy,downInsec=rj_xy,upDire1=1,upClane1=[3,4,5,6],upDire2=3,upClane2=[1,2],downDire=4,downClane1=[1,2,3],downClane2=[1,2,3])












#<3>第3步各路段行程上下游的行程时间匹配
#路径1：匹配瑞金-新华路至瑞金-兴关交叉口 东向西
match_total_tt1,match_total_final1,match_total_rate1=loopMatch(downData=rj_xgData,upData=rj_xhData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=1)


#路径2：匹配瑞金-兴关交叉口至遵义-瑞金交叉口 东向西
match_total_tt2,match_total_final2,match_total_rate2=loopMatch(downData=rj_zyData,upData=rj_xgData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=1)

#路径3：匹配遵义-瑞金路至瑞金-雪涯路交叉口 东向西
match_total_tt3,match_total_final3,match_total_rate3=loopMatch(downData=rj_xyData,upData=rj_zyData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=4)







#<4>第4步行程时间预处理，这里分车道处理，形成相关行驶方向的运行状态
#预处理,分车道
dataDeal1=loopDeal(match_total_final1,claneNum=[2,3,4])
dataDeal2=loopDeal(match_total_final2,claneNum=[3,4,5,6])
dataDeal3=loopDeal(match_total_final3,claneNum=[1,2,3])







#第5步处理得到15min的平均行程时间
#处理成15min的平均行程时间
data_15min1,freeV1=loop_15min(dataDeal1,q_total1)


data_15min2,freeV2=loop_15min(dataDeal2,q_total2)


data_15min3,freeV3=loop_15min(dataDeal3,q_total3)

#绘制处理过后的实验路段2的平均行程时间
import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.subplot(5,7,i+1)
    a1=plt.plot(data_15min2[i][:,0],data_15min2[i][:,5])
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,900)
plt.savefig('F:\python_script\data_deal/link2.png',dpi=200) 


#绘制路段1的路段行程时间
import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.subplot(5,7,i+1)
    a1=plt.plot(data_15min1[i][:,0],data_15min1[i][:,5])
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,900)

#绘制路段3的路段行程时间
import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.subplot(5,7,i+1)
    a1=plt.plot(data_15min3[i][:,0],data_15min3[i][:,5])
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,900)


















