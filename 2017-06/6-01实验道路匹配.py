# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 13:21:53 2017

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





#1.瑞金-雪涯路
rj_xy=pd.read_csv(r'f:\data_final\rj_xy1201-1231.csv',encoding='utf-8')
rj_xyData,rj_xyDayNum=dataTran(rj_xy)



#2.瑞金-遵义路
rj_zy=pd.read_csv(r'f:\data_final\rj_zy1201-1231.csv',encoding='utf-8')
rj_zyData,rj_zyDayNum=dataTran(rj_zy)



#4.青云-遵义路
qy_zy=pd.read_csv(r'f:\data_final\qy_zy1201-1231.csv',encoding='utf-8')
qy_zyData,qy_zyDayNum=dataTran(qy_zy)



#5.中华-遵义路
zh_zy=pd.read_csv(r'f:\data_final\zh_zy1201_1231.csv',encoding='utf-8')
zh_zyData,zh_zyDayNum=dataTran(zh_zy)




#6.中华-都司路
ds_zy=pd.read_csv(r'f:\data_final\ds_zy1201_1231.csv',encoding='utf-8')
ds_zyData,ds_zyDayNum=dataTran(ds_zy)







#路径1：匹配瑞金-遵义路至遵义-青云交叉口 南向北
match_total_tt1,match_total_final1,match_total_rate1=loopMatch(downData=rj_zyData,upData=qy_zyData,dayNum=qy_zyDayNum,maxtime1=900,mintime1=35,down_direction1=3)




#路径2：匹配瑞金-雪涯路至遵义-瑞金交叉口 西向北
match_total_tt2,match_total_final2,match_total_rate2=loopMatch(downData=rj_zyData,upData=rj_xyData,dayNum=rj_xyDayNum,maxtime1=900,mintime1=35,down_direction1=2)




#路径3：匹配遵义-瑞金路至遵义-中华交叉口 南向北
match_total_tt3,match_total_final3,match_total_rate3=loopMatch(downData=zh_zyData,upData=rj_zyData,dayNum=rj_xyDayNum,maxtime1=900,mintime1=35,down_direction1=3)




#路径4：匹配至遵义-中华交叉口至中华-都司交叉口 东向西
match_total_tt4,match_total_final4,match_total_rate4=loopMatch(downData=ds_zyData,upData=zh_zyData,dayNum=zh_zyDayNum,maxtime1=900,mintime1=35,down_direction1=3)




































































