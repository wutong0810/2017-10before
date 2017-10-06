# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:08:30 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
#方向：1北，3南进口道，2西进口，4东进口道
#读写交叉口信息
#青云路与兴关路
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *





#CCARNUMBER,DCOLLECTIONDATE,CLANENUMBER,NDERICTRION,CLICENSETYPE

#读写数据，将数据先写入data_final


#1.瑞金与雪涯交叉口
rj_xy=pd.read_csv(r'F:\data\rj_xy1201-1231.csv')
rj_xy1=rj_xy.iloc[:,[1,2,4,5,0]]
rj_xy1.to_csv(r'f:\data_final\rj_xy1201-1231.csv',index=False)




#2.瑞金路与遵义路交叉口
rj_zy=pd.read_csv(r'F:\data\rj_zy1201-1231.csv')
rj_zy1=rj_zy.iloc[:,[1,2,4,5,0]]
rj_zy1.to_csv(r'f:\data_final\rj_zy1201-1231.csv',index=False)

#4.青云与遵义路交叉口
qy_zy=pd.read_csv(r'F:\data\qy_zy1201-1231.csv')
qy_zy1=qy_zy.iloc[:,[2,3,10,15,1]]
qy_zy1.to_csv(r'f:\data_final\qy_zy1201-1231.csv',index=False)



#5.中华南路与遵义路交叉口
zh_zy=pd.read_csv(r'F:\data\zh_zy1201_1231.csv')
zh_zy1=jf_zy.iloc[:,[1,2,6,7,0]]
zh_zy1.to_csv(r'f:\data_final\zh_zy1201_1231.csv',index=False)





































qy_zy=pd.read_csv(r'F:\data_final\qy_zy1201-1231.csv',encoding='utf-8')
qy_zyData,qy_zyDayNum=dataTran(qy_zy)



