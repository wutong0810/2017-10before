# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:21:23 2017

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



#上游
inpath1=r'F:\海信\事件检测-电子警察数据\香港西路\xg_ya1026.csv'
uipath1 = unicode(inpath1 , "utf8")

#下游
inpath2=r'F:\海信\事件检测-电子警察数据\香港西路\xg_sd1026.csv'
uipath2 = unicode(inpath2 , "utf8")




xg_ya1026=pd.read_csv(uipath1,encoding='gbk')
xg_sd1026=pd.read_csv(uipath2,encoding='gbk')





    
    
    
xg_sd1026.iloc[:,0]=xg_sd1026.iloc[:,0].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_sd1026.iloc[:,1]=xg_sd1026.iloc[:,1].apply(lambda x:str(x).strip(r'/?'))
xg_sd1026.iloc[:,2]=xg_sd1026.iloc[:,2].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_sd1026.iloc[:,3]=xg_sd1026.iloc[:,3].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_sd1026.iloc[:,4]=xg_sd1026.iloc[:,4].apply(lambda x:(x.encode('utf-8').strip(r'/?')))

     
     

#规整数据
direct={'\xe8\xa5\xbf->\xe4\xb8\x9c':2}
carType={'\xe6\x9c\xaa\xe8\xaf\x86\xe5\x88\xab':41,
 '\xe5\xb0\x8f\xe5\x9e\x8b\xe6\xb1\xbd\xe8\xbd\xa6':2,
 '\xe8\xad\xa6\xe7\x94\xa8\xe6\xb1\xbd\xe8\xbd\xa6':23,
 '\xe5\xa4\xa7\xe5\x9e\x8b\xe6\xb1\xbd\xe8\xbd\xa6':1,
 '\xe5\x86\x9b\xe9\x98\x9f\xe7\x94\xa8\xe5\xb0\x8f\xe5\x9e\x8b\xe6\xb1\xbd\xe8\xbd\xa6':29,
 '\xe5\x86\x9b\xe9\x98\x9f\xe7\x94\xa8\xe5\xa4\xa7\xe5\x9e\x8b\xe6\xb1\xbd\xe8\xbd\xa6':31}
 

clane={'\xe7\xac\xac\xe4\xb8\x80\xe8\xbd\xa6\xe9\x81\x93':1,
       '\xe7\xac\xac\xe4\xba\x94\xe8\xbd\xa6\xe9\x81\x93':5,
       '\xe7\xac\xac\xe4\xb8\x89\xe8\xbd\xa6\xe9\x81\x93':3,
       '\xe7\xac\xac\xe5\x9b\x9b\xe8\xbd\xa6\xe9\x81\x93':4,
       '\xe7\xac\xac\xe4\xba\x8c\xe8\xbd\xa6\xe9\x81\x93':2}


f1=lambda x:direct.get(x,0)
f2=lambda x:carType.get(x,0)
f3=lambda x:clane.get(x,0)

xg_sd1026.iloc[:,2]=xg_sd1026.iloc[:,2].map(f3)

xg_sd1026.iloc[:,3]=xg_sd1026.iloc[:,3].map(f1)

xg_sd1026.iloc[:,-1]=xg_sd1026.iloc[:,-1].map(f2)

path1=r'F:\海信\事件检测-电子警察数据\香港西路\xg_sd1026_1.csv'
path2= unicode(path1 , "utf8")
xg_sd1026.to_csv(path2,index=False,encoding='gbk')





xg_ya1026.iloc[:,0]=xg_ya1026.iloc[:,0].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_ya1026.iloc[:,1]=xg_ya1026.iloc[:,1].apply(lambda x:str(x).strip(r'/?'))
xg_ya1026.iloc[:,2]=xg_ya1026.iloc[:,2].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_ya1026.iloc[:,3]=xg_ya1026.iloc[:,3].apply(lambda x:(x.encode('utf-8').strip(r'/?')))
xg_ya1026.iloc[:,4]=xg_ya1026.iloc[:,4].apply(lambda x:(x.encode('utf-8').strip(r'/?')))


xg_ya1026.iloc[:,2]=xg_ya1026.iloc[:,2].map(f3)

xg_ya1026.iloc[:,3]=xg_ya1026.iloc[:,3].map(f1)

xg_ya1026.iloc[:,-1]=xg_ya1026.iloc[:,-1].map(f2)

path1=r'F:\海信\事件检测-电子警察数据\香港西路\xg_ya1026_1.csv'
path2= unicode(path1 , "utf8")
xg_ya1026.to_csv(path2,index=False,encoding='gbk')




#这里解码出现问题，无车牌也是9




xg_ya1026.iloc[:,1]=pd.to_datetime(xg_ya1026.iloc[:,1]) 
xg_sd1026.iloc[:,1]=pd.to_datetime(xg_sd1026.iloc[:,1])  

    
xg_ya1026['sj']=xg_ya1026.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
xg_sd1026['sj']=xg_sd1026.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)

xg_yaData1026=xg_ya1026.iloc[:,[0,5,2,3,4]]

xg_sdData1026=xg_sd1026.iloc[:,[0,5,2,3,4]]
match_tt,match_final,match_rate=match_traveltime(up_data=xg_yaData1026,down_data=xg_sdData1026,maxtime=1200,mintime=45,down_direction=2)





match_final1=match_final[match_final.iloc[:,0]!='无车牌']

matchFinal2=match_final1.iloc[:,[0,1,2,3,4,6,7,8,9]]
matchFinal3=np.array(matchFinal2)
dealData1=data_deal(matchFinal3,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8)





ttAll=np.zeros((12,3))
ttAll[:,0]=range(12)
for i in range(12):
    medTravel=dealData1[(dealData1.iloc[:,1]>i*300+55800)&(dealData1.iloc[:,1]<((i+1)*300)+55800)]
    if len(medTravel)>0:
        ttAll[i,1]=np.median(medTravel.iloc[:,8])
        ttAll[i,2]=np.mean(medTravel.iloc[:,8])



















a1=plt.figure()
a1=plt.scatter(match_final1.iloc[:,1],match_final1.iloc[:,9],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,1200)













