# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 21:40:08 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#方向：4北，3南进口道，2西进口，1东进口道
#读写交叉口信息
#青云路与兴关路
import sys
#sys.path.append(r'F:\python_script\2017-5\predict')
#from all_func import *






#2.瑞金-兴关路
rj_xg=pd.read_csv(r'C:\Users\wutongshu\Desktop\dianying\rj_xg1201-1231.csv',encoding='utf-8')
rj_xg.iloc[:,1]=pd.to_datetime(rj_xg.iloc[:,1])
rj_xg['day']=rj_xg.iloc[:,1].apply(lambda x:100*x.month+x.day)
rj_xg['sj']=rj_xg.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)

#3.瑞金-遵义路
rj_zy=pd.read_csv(r'C:\Users\wutongshu\Desktop\dianying\rj_zy1201-1231.csv',encoding='utf-8')
rj_zy=rj_zy.iloc[:,[1,2,4,5,0]]
rj_zy.iloc[:,1]=pd.to_datetime(rj_zy.iloc[:,1])
rj_zy['day']=rj_zy.iloc[:,1].apply(lambda x:100*x.month+x.day)
rj_zy['sj']=rj_zy.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)


for i in range(1204,1231):
    
    
    
    
    
    