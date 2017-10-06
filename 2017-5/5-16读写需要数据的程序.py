# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:14:29 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#读写交叉口信息
#青云路与兴关路
qy_xy=pd.read_csv(r'F:\data\qy_xg1201-1231.csv')
qy_xy1=qy_xy.iloc[:,[2,3,10,15,1]]
qy_xy1.to_csv(r'f:\data_final\qy_xg1201-1231.csv',index=False)

#青云与遵义路交叉口
qy_zy=pd.read_csv(r'F:\data\qy_zy1201-1231.csv')
qy_zy1=qy_zy.iloc[:,[2,3,10,15,1]]
qy_zy1.to_csv(r'f:\data_final\qy_zy1201-1231.csv',index=False)

#解放路与遵义路交叉口
jf_zy=pd.read_csv(r'F:\data\zy_jf1201-1231.csv')
jf_zy1=jf_zy.iloc[:,[2,3,10,15,1]]
jf_zy1.to_csv(r'f:\data_final\zy_jf1201-1231.csv',index=False)


#沙冲与兴关路交叉口
sc_xg=pd.read_csv(r'F:\data\sc_xg1201-1231.csv')
sc_xg1=sc_xg.iloc[:,[2,3,10,15,1]]
sc_xg1.to_csv(r'f:\data_final\sc_xg1201-1231.csv',index=False)



#瑞金路与遵义路交叉口
rj_zy=pd.read_csv(r'F:\data\rj_zy1201-1231.csv')

rj_zy1=rj_zy.iloc[:,[1,2,4,5,0]]
rj_zy1.to_csv(r'f:\data_final\rj_zy1201-1231.csv',index=False)



#瑞金路与遵义路交叉口
rj_xg=pd.read_csv(r'F:\data\rj_xg1201-1231.csv')
rj_xg1=rj_xg.iloc[:,[1,2,4,5,0]]
rj_xg1.to_csv(r'f:\data_final\rj_xg1201-1231.csv',index=False)





#读写解放路-嘉润路
jf_jr=pd.read_csv(r'F:\data\jf_jr1204-0103.csv')
jf_jr1=jf_jr.iloc[:,[1,2,6,7,0]]
jf_jr1.to_csv(r'f:\data_final\jf_jr1204-0103.csv',index=False)



#读写解放路- 南厂路
jf_nc=pd.read_csv(r'F:\data\jf_nc1204-0103.csv')
jf_nc1=jf_nc.iloc[:,[1,2,6,7,0]]
jf_nc1.to_csv(r'f:\data_final\jf_nc1204-0103.csv',index=False)



#读写中华路- 遵义路
jf_zy=pd.read_csv(r'F:\data\zh_zy1201_1231.csv')
jf_zy1=jf_zy.iloc[:,[1,2,6,7,0]]
jf_zy1.to_csv(r'f:\data_final\zh_zy1201_1231.csv',index=False)





#瑞金与雪涯交叉口
rj_xy=pd.read_csv(r'F:\data\rj_xy1201-1231.csv')
rj_xy1=rj_xy.iloc[:,[1,2,6,7,0]]
sc_xg1.to_csv(r'f:\data_final\sc_xg1201-1231.csv',index=False)





























