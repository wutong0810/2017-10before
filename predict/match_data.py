# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:34:21 2017

@author: wutongshu
"""
import sys
sys.path.append('D:\python_script\predict')
from all_func import *
#数据匹配全过程
#上游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_xg1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_xh1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt1=[]
match_total_final1=[]
match_total_rate1=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:5]
    up_data4=up_data3.iloc[:,0:5]
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=40,down_direction=1)        
    match_total_tt1.append(match_tt)
    match_total_final1.append(match_final)
    match_total_rate1.append(match_rate)

#中游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_zy1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_xg1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt2=[]
match_total_final2=[]
match_total_rate2=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=1)        
    match_total_tt2.append(match_tt)
    match_total_final2.append(match_final)
    match_total_rate2.append(match_rate)


#下游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_xy1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_zy1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt3=[]
match_total_final3=[]
match_total_rate3=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=4)        
    match_total_tt3.append(match_tt)
    match_total_final3.append(match_final)
    match_total_rate3.append(match_rate)