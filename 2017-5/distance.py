# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:40:40 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
from math import *
a=pd.read_csv('f:/alldianwei.csv',encoding='gbk')
a1=a.iloc[:,2:5]
a2=np.array(a1)
a3=np.zeros((len(a2),len(a2)))
for i in range(len(a2)):
    for j in range(len(a2)):
        if (np.isnan(a2[i,0]))|(np.isnan(a2[j,0])):
            a3[i,j]=3000
        else :
            a3[i,j]=dis(a2[i,1],a2[i,0],a2[j,1],a2[j,0])
    
a4=np.zeros((len(a2)**2,3))
for i in range(len(a2)):
    for j in range(len(a2)):
        a4[i*len(a2)+j,0]=i
        a4[i*len(a2)+j,1]=j
        a4[i*len(a2)+j,2]=a3[i,j]



#a1为lat1，b1为lat2;b1为lon1,b2为long2
def dis(a1,a2,b1,b2):
    a_1=(a1-b1)*pi/180
    b_2=abs(a2-b2)*pi/180
    distance=6378137*2*asin(sqrt(sin(a_1/2)**2) + cos(a1*pi/180)*cos(b1*pi/180)*((sin(b_2/2))**2))
    return distance
    
d = EARTH_RADIUS*2*asin(sqrt(sin(a/2)^2) + cos(lat1*pi/180)*cos(lat2*pi/180)*sin(b/2)^2);    
    
np.savetxt(r'f:/dis.csv',a4,delimiter=',')
#106.70681	26.52632
#106.70695	26.5241






#
#CCOLLECTIONADDRESS  CADDRESSCODE  LONGITUDE  LATITUDE   ID
#57          北京西路与盐务街以北  7.104610e+11        NaN       NaN   58  106.7116152803,26.5989896386
#126              公安局门口           NaN        NaN       NaN  127 106.609409	26.856366
#168           虎城大道云环小学           NaN        NaN       NaN  169 106.746053	27.064062
#186        花溪至贵阳15270米  6.015610e+11        NaN       NaN  187 106.66182	26.49909
#201          甲秀南路五里冲路段           NaN        NaN       NaN  202 106.6750937852,26.5611087061
#228        金清大道6公里120米  9.100800e+11        NaN       NaN  229 106.54804	26.584542
#230        金清大道6公里720米  9.100800e+11        NaN       NaN  231 106.54804	26.58453
#238     金阳南路（广电网络公司路段）  1.500000e+01        NaN       NaN  239 106.622127	26.635022
#239   金阳南路（广电网络公司人行横道）  1.500000e+01        NaN       NaN  240 106.622127	26.635012
#268        龙泉苑街与兰州街交叉口           NaN        NaN       NaN  269 106.631744	26.611579
#428         迎春路与朝阳路交叉口           NaN        NaN       NaN  429 106.59509	26.844871
#429             永靖大道路段           NaN        NaN       NaN  430  106.724757	27.098218
#430       永靖大道与X173交叉口           NaN        NaN       NaN  431 106.7117874038 27.0888826198
#431       永靖大道与X175交叉口           NaN        NaN       NaN  432 106.7117874038 27.0888826198
#432       永靖大道与X176交叉口           NaN        NaN       NaN  433 106.7117874038 27.0888826198
#492      浣纱路与市西高架桥路交叉口  6.101210e+11        NaN       NaN  493 106.6983147060,26.5757881547
#493      浣纱路与市西路高架桥交叉口  6.101210e+11        NaN       NaN  494 106.6983147060,26.5757881547
#497                NaN  7.104010e+11        NaN       NaN  498
#498                NaN  7.104910e+11        NaN       NaN  499
#499                NaN  7.106210e+11        NaN       NaN  500
#500                NaN  7.116910e+11        NaN       NaN  501
#501                NaN  7.118310e+11        NaN       NaN  502

#补全

a.iloc[57,2]=106.7116152803
a.iloc[57,3]=26.5989896386

a.iloc[126,2]=106.609409
a.iloc[126,3]=26.856366

a.iloc[168,2]=106.746053
a.iloc[168,3]=27.064062

a.iloc[186,2]=106.66182
a.iloc[186,3]=26.49909

a.iloc[201,2]=106.6750937852
a.iloc[201,3]=26.5611087061

a.iloc[228,2]=106.54804
a.iloc[228,3]=26.584542

a.iloc[230,2]=106.54804	
a.iloc[230,3]=26.58453

a.iloc[238,2]=106.622127	
a.iloc[238,3]=26.635022

a.iloc[239,2]=106.622127	
a.iloc[239,3]=26.635012

a.iloc[268,2]=106.631744	
a.iloc[268,3]=26.611579

a.iloc[428,2]=106.59509	
a.iloc[428,3]=26.844871

a.iloc[429,2]=106.724757	
a.iloc[429,3]=27.098218

a.iloc[430,2]=106.7117874038 
a.iloc[430,3]=27.0888826198

a.iloc[431,2]=106.7117874038 
a.iloc[431,3]=27.0888826198

a.iloc[432,2]=106.7117874038 
a.iloc[432,3]=27.0888826198

a.iloc[492,2]=106.6983147060
a.iloc[492,3]=26.5757881547

a.iloc[493,2]=106.6983147060
a.iloc[493,3]=26.5757881547








