# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:04:43 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#青云路与兴关路
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *


qy_xg=pd.read_csv(r'F:\data_final\qy_xg1201-1231.csv',encoding='utf-8')
qy_xgData,qy_xgDayNum=dataTran(qy_xg)
#青云与遵义路交叉口
qy_zy=pd.read_csv(r'F:\data_final\qy_zy1201-1231.csv',encoding='utf-8')
qy_zyData,qy_zyDayNum=dataTran(qy_zy)
#解放路与遵义路交叉口
jf_zy=pd.read_csv(r'F:\data_final\zy_jf1201-1231.csv',encoding='utf-8')
jf_zyData,jf_zyDayNum=dataTran(jf_zy)
#解放路与沙冲路交叉口
sc_xg=pd.read_csv(r'F:\data_final\sc_xg1201-1231.csv',encoding='utf-8')
sc_xgData,sc_xgDayNum=dataTran(sc_xg)

#瑞金与遵义路交叉口
rj_zy=pd.read_csv(r'F:\data_final\rj_zy1201-1231.csv',encoding='utf-8')
rj_zyData,rj_zyDayNum=dataTran(rj_zy)

#瑞金与兴关路
rj_xg=pd.read_csv(r'F:\data_final\rj_xg1201-1231.csv',encoding='utf-8')
rj_xgData,rj_xgDayNum=dataTran(rj_xg)

#解放-南厂路
jf_nc=pd.read_csv(r'F:\data_final\jf_nc1204-0103.csv',encoding='gbk')
jf_ncData,jf_ncDayNum=dataTran(jf_nc)


jf_jr=pd.read_csv(r'F:\data_final\jf_jr1204-0103.csv',encoding='gbk')
jf_jrData,jf_jrDayNum=dataTran(jf_jr)



#中华与遵义路交叉口
zh_zy=pd.read_csv(r'F:\data_final\zh_zy1201_1231.csv',encoding='gbk')
zh_zyData,zh_zyDayNum=dataTran(zh_zy)

#瑞金与遵义路交叉口
rj_zy=pd.read_csv(r'F:\data_final\rj_zy1201-1231.csv',encoding='gbk')
rj_zyData,rj_zyDayNum=dataTran(rj_zy)






jf_ncDayNum1=list(jf_ncDayNum)
jf_ncDayNum1.reverse()



















#1.匹配瑞金-兴关路至瑞金-遵义路交叉口 东向西
match_total_tt1,match_total_final1,match_total_rate1=loopMatch(downData=rj_zyData,upData=rj_xgData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=1)

#2.匹配瑞金-遵义路至遵义-青云交叉口 北向南
match_total_tt2,match_total_final2,match_total_rate2=loopMatch(downData=qy_zyData,upData=rj_zyData,dayNum=qy_zyDayNum,maxtime1=900,mintime1=35,down_direction1=4)

#3.匹配青云-遵义路至青云-兴关路交叉口 西向东
match_total_tt3,match_total_final3,match_total_rate3=loopMatch(downData=qy_xgData,upData=qy_zyData,dayNum=qy_xgDayNum,maxtime1=900,mintime1=35,down_direction1=2)

#4.匹配青云-兴关路至瑞金-兴关交叉口 南向北
match_total_tt4,match_total_final4,match_total_rate4=loopMatch(downData=rj_xgData,upData=qy_xgData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=3)



#5.匹配瑞金-兴关路至瑞金-遵义路交叉口 西向东
match_total_tt5,match_total_final5,match_total_rate5=loopMatch(downData=rj_xgData,upData=rj_zyData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=2)

#6.匹配瑞金-遵义路至遵义-青云交叉口 南向北
match_total_tt6,match_total_final6,match_total_rate6=loopMatch(downData=rj_zyData,upData=qy_zyData,dayNum=qy_zyDayNum,maxtime1=900,mintime1=35,down_direction1=3)

#7.匹配青云-遵义路至青云-兴关路交叉口 东向西
match_total_tt7,match_total_final7,match_total_rate7=loopMatch(downData=qy_zyData,upData=qy_xgData,dayNum=qy_xgDayNum,maxtime1=900,mintime1=35,down_direction1=1)

#8.匹配青云-兴关路至瑞金-兴关交叉口 北向南
match_total_tt8,match_total_final8,match_total_rate8=loopMatch(downData=qy_xgData,upData=rj_xgData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=4)





match_total_tt9,match_total_final9,match_total_rate9=loopMatch(downData=jf_jrData,upData=jf_ncData,dayNum=jf_ncDayNum1,maxtime1=900,mintime1=30,down_direction1=2)

match_total_tt10,match_total_final10,match_total_rate10=loopMatch(downData=jf_zyData,upData=qy_zyData,dayNum=jf_zyDayNum,maxtime1=900,mintime1=30,down_direction1=4)


match_total_tt10,match_total_final10,match_total_rate10=loopMatch(downData=zh_zyData,upData=rj_zyData,dayNum=zh_zyDayNum,maxtime1=900,mintime1=30,down_direction1=3)












#多线程并行运算
#import threading
#t1 = threading.Thread(target=loopMatch, args=(rj_zyData,rj_xgData,rj_xgDayNum,900,35,1))
#match_total_tt1,match_total_final1,match_total_rate1=t1.start()
#
#t2 = threading.Thread(target=loopMatch, args=(qy_zyData,rj_zyData,rj_xgDayNum,900,35,4))
#match_total_tt2,match_total_final2,match_total_rate2=t2.start()
#
#t3 = threading.Thread(target=loopMatch, args=(qy_xgData,qy_zyData,rj_xgDayNum,900,35,2))
#match_total_tt3,match_total_final3,match_total_rate3=t3.start()
#
#t4 = threading.Thread(target=loopMatch, args=(rj_xgData,qy_xgData,rj_xgDayNum,900,35,3))
#match_total_tt4,match_total_final4,match_total_rate4=t4.start()
#
#
#t5 = threading.Thread(target=loopMatch, args=(rj_xgData,rj_zyData,rj_xgDayNum,900,35,2))
#match_total_tt5,match_total_final5,match_total_rate5=t5.start()
#
#t6 = threading.Thread(target=loopMatch, args=(rj_zyData,qy_zyData,rj_xgDayNum,900,35,3))
#match_total_tt6,match_total_final6,match_total_rate6=t6.start()
#
#t7 = threading.Thread(target=loopMatch, args=(qy_zyData,qy_xgData,rj_xgDayNum,900,35,1))
#match_total_tt7,match_total_final7,match_total_rate7=t7.start()
#
#t8 = threading.Thread(target=loopMatch, args=(qy_xgData,rj_xgData,rj_xgDayNum,900,35,4))
#match_total_tt8,match_total_final8,match_total_rate8=t8.start()















##匹配青云-遵义路至遵义-解放交叉口 北向南
#match_total_tt,match_total_final,match_total_rate=loopMatch(downData=jf_zyData,upData=qy_zyData,dayNum=qy_zyDayNum,maxtime1=900,mintime1=35,down_direction1=4)



ds_zyData,upData=zh_zyData


##
downData=ds_zyData
upData=zh_zyData
down_data2=downData[downData.iloc[:,-1]==1226]
up_data2=upData[upData.iloc[:,-1]==1226]
down_data3=down_data2.iloc[:,[0,5,2,3,4]]
up_data3=up_data2.iloc[:,[0,5,2,3,4]]
match_tt,match_final,match_rate=match_traveltime(up_data3,down_data3,maxtime=900,mintime=35,down_direction=3)    
#down_data=down_data3[down_data3.ix[:,3]==4]
#
#
#
#
#match_total_tt2,match_total_final2,match_total_rate2=loopMatch(downData=qy_zyData,upData=rj_zyData,dayNum=rj_xgDayNum,maxtime1=900,mintime1=35,down_direction1=4)
#
#
#
#
#
#
#
#
#
#
#
#match_total_tt2=[]
#match_total_final2=[]
#match_total_rate2=[]
##匹配车牌行程时间，按天分别匹配
#downData=qy_zyData
#upData=rj_zyData
#dayNum=rj_xgDayNum
#for i in dayNum:
#    down_data2=downData[downData.iloc[:,-1]==i]
#    up_data2=upData[upData.iloc[:,-1]==i]
#    if (len(down_data2)==0)|(len(up_data2)==0):
#        continue
#    down_data3=down_data2.iloc[:,[0,5,2,3,4]]
#    up_data3=up_data2.iloc[:,[0,5,2,3,4]]
#    match_tt,match_final,match_rate=match_traveltime(up_data3,down_data3,maxtime=900,mintime=35,down_direction=4)        
#    match_total_tt2.append(match_tt)
#    match_total_final2.append(match_final)
#    match_total_rate2.append(match_rate)

