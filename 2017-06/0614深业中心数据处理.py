# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:30:36 2017

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
inpath1=r'F:\海信\事件检测-电子警察数据\深业中心数据\sd_mj1222.csv'
uipath1 = unicode(inpath1 , "utf8")

#下游
inpath2=r'F:\海信\事件检测-电子警察数据\深业中心数据\sd_jx1222.csv'
uipath2 = unicode(inpath2 , "utf8")


sd_mj22=pd.read_csv(uipath1,encoding='gbk')
jx_sd22=pd.read_csv(uipath2,encoding='gbk')


sd_mjData22=sd_mj22.iloc[:,[0,5,2,3,4]]

jx_sdData22=jx_sd22.iloc[:,[0,5,2,3,4]]

match_tt1,match_final1,match_rate1=match_traveltime(up_data=sd_mjData22,down_data=jx_sdData22,maxtime=60*20,mintime=30,down_direction=3)


#原始数据图
a1=plt.figure()
a1=plt.scatter(match_final1.iloc[:,1],match_final1.iloc[:,9],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,1200)


matchFinal1=match_final1[(match_final1.iloc[:,2]==2)|(match_final1.iloc[:,2]==3)|(match_final1.iloc[:,2]==4)|(match_final1.iloc[:,2]==5)]
matchFinal2=matchFinal1.iloc[:,[0,1,2,3,4,6,7,8,9]]
matchFinal3=np.array(matchFinal2)
dealData1=data_deal(matchFinal3,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8)

#预处理后数据图
a1=plt.figure()
a1=plt.scatter(dealData1.iloc[:,1],dealData1.iloc[:,8],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,1200)

#得到每5分钟的行程时间中位数,第1列时刻，第2列行程时间中位数，第3列行程时间均值；

Tt5min=np.zeros((288,3))
Tt5min[:,0]=range(288)
for i in range(288):
    medTravel=dealData1[(dealData1.iloc[:,1]>i*300)&(dealData1.iloc[:,1]<(i+1)*300)]
    if len(medTravel)>0:
        Tt5min[i,1]=np.median(medTravel.iloc[:,8])
        Tt5min[i,2]=np.mean(medTravel.iloc[:,8])

#绘制中位数图        
a1=plt.figure()
a1=plt.plot(Tt5min[:,0],Tt5min[:,1],'o-',label='median')
#a1=plt.plot(Tt5min[:,0],Tt5min[:,2],'o-',label='mean')
a1=plt.xlim(0,288)
a1=plt.ylim(0,900)    
plt.legend()


def removeFun(data):
    data['moved']=0
    data1=np.array(data)
    dataFinal=[]
    for i in data.iloc[:,2].unique():
            data2=data1[data1[:,2]==i]
            indice=[]
            for j in range(1,len(data2)):
                if (cmp(data2[j,0],data2[j-1,0])==0)& (data2[j,1]-data2[j-1,1]<100&data2[j,4]!=41):
                    indice.append(j-1)
        #给行程时间付上-1来标示行程时间
            for h in indice:
                data2[h,5]=-1
            dataFinal.append(pd.DataFrame(data2[data2[:,5]>-1]))
            dataFinal1=pd.concat(dataFinal, ignore_index=True) 
    return dataFinal1



#统计流量，第1列时刻，第2列车道2流量，第3列车道3流量，第4列车道4流量，第5列车道5流量
Q5min=np.zeros((288,6))
Q5min[:,0]=range(288)
for i in range(288):
    medQ=jx_sdData22[(jx_sdData22.iloc[:,1]>i*300)&(jx_sdData22.iloc[:,1]<(i+1)*300)]
    medQ=removeFun(medQ)
    medQ2=medQ[medQ.iloc[:,2]==2]
    medQ3=medQ[medQ.iloc[:,2]==3]                 
    medQ4=medQ[medQ.iloc[:,2]==4]                    
    medQ5=medQ[medQ.iloc[:,2]==5]                    
    Q5min[i,1]=len(medQ2)
    Q5min[i,2]=len(medQ3)
    Q5min[i,3]=len(medQ4)
    Q5min[i,4]=len(medQ5)
    Q5min[i,5]=len(medQ2)+len(medQ3)+len(medQ4)+len(medQ5)
    
    
#1行程时间变化与流量图
a1=plt.figure()
a1=plt.plot(Tt5min[:,0],Tt5min[:,1],'o-',label='median')
a1=plt.plot(Q5min[:,0],Q5min[:,1],'o-',label='Q2')
a1=plt.plot(Q5min[:,0],Q5min[:,2],'o-',label='Q3')
a1=plt.plot(Q5min[:,0],Q5min[:,3],'o-',label='Q4')
a1=plt.plot(Q5min[:,0],Q5min[:,4],'o-',label='Q5')
a1=plt.plot(Q5min[:,0],Q5min[:,5],'o-',label='Qall')
a1=plt.xlim(0,288)
#a1=plt.ylim(0,900)    
plt.legend()














#未发生事件数据，23号数据
    
    
#上游
inpath1=r'F:\海信\事件检测-电子警察数据\深业中心数据\sd_mj1223.csv'
uipath1 = unicode(inpath1 , "utf8")

#下游
inpath2=r'F:\海信\事件检测-电子警察数据\深业中心数据\sd_jx1223.csv'
uipath2 = unicode(inpath2 , "utf8")


sd_mj23=pd.read_csv(uipath1,encoding='gbk')
jx_sd23=pd.read_csv(uipath2,encoding='gbk')


sd_mjData23=sd_mj23.iloc[:,[0,5,2,3,4]]

jx_sdData23=jx_sd23.iloc[:,[0,5,2,3,4]]

match_tt2,match_final2,match_rate2=match_traveltime(up_data=sd_mjData23,down_data=jx_sdData23,maxtime=60*20,mintime=30,down_direction=3)


#原始数据图
a1=plt.figure()
a1=plt.scatter(match_final2.iloc[:,1],match_final2.iloc[:,9],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,1200)


matchFinal1=match_final2[(match_final2.iloc[:,2]==2)|(match_final2.iloc[:,2]==3)|(match_final2.iloc[:,2]==4)|(match_final2.iloc[:,2]==5)]
matchFinal2=matchFinal1.iloc[:,[0,1,2,3,4,6,7,8,9]]
matchFinal3=np.array(matchFinal2)
dealData2=data_deal(matchFinal3,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8)

#预处理后数据图
a1=plt.figure()
a1=plt.scatter(dealData2.iloc[:,1],dealData2.iloc[:,8],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,1200)

#得到每5分钟的行程时间中位数,第1列时刻，第2列行程时间中位数，第3列行程时间均值；

Tt5min2=np.zeros((288,3))
Tt5min2[:,0]=range(288)
for i in range(288):
    medTravel=dealData2[(dealData2.iloc[:,1]>i*300)&(dealData2.iloc[:,1]<(i+1)*300)]
    if len(medTravel)>0:
        Tt5min2[i,1]=np.median(medTravel.iloc[:,8])
        Tt5min2[i,2]=np.mean(medTravel.iloc[:,8])

#绘制中位数图        
a1=plt.figure()
a1=plt.plot(Tt5min2[:,0],Tt5min2[:,1],'o-',label='median')
#a1=plt.plot(Tt5min[:,0],Tt5min[:,2],'o-',label='mean')
a1=plt.xlim(0,288)
a1=plt.ylim(0,900)    
plt.legend()


#统计流量，第1列时刻，第2列车道2流量，第3列车道3流量，第4列车道4流量，第5列车道5流量
Q5min2=np.zeros((288,6))
Q5min2[:,0]=range(288)
for i in range(288):
    medQ=jx_sdData23[(jx_sdData23.iloc[:,1]>i*300)&(jx_sdData23.iloc[:,1]<(i+1)*300)]
    medQ2=medQ[medQ.iloc[:,2]==2]
    medQ3=medQ[medQ.iloc[:,2]==3]                 
    medQ4=medQ[medQ.iloc[:,2]==4]                    
    medQ5=medQ[medQ.iloc[:,2]==5]                    
    Q5min2[i,1]=len(medQ2)
    Q5min2[i,2]=len(medQ3)
    Q5min2[i,3]=len(medQ4)
    Q5min2[i,4]=len(medQ5)
    Q5min2[i,5]=len(medQ2)+len(medQ3)+len(medQ4)+len(medQ5)
    
    

a1=plt.figure()
a1=plt.plot(Tt5min[:,0],Tt5min2[:,1],'o-',label='median')
a1=plt.plot(Q5min[:,0],Q5min2[:,1],'o-',label='Q2')
a1=plt.plot(Q5min[:,0],Q5min2[:,2],'o-',label='Q3')
a1=plt.plot(Q5min[:,0],Q5min2[:,3],'o-',label='Q4')
a1=plt.plot(Q5min[:,0],Q5min2[:,4],'o-',label='Q5')
a1=plt.plot(Q5min[:,0],Q5min2[:,5],'o-',label='Qall')
a1=plt.xlim(0,288)
a1=plt.ylim(0,500)    
plt.legend()    








#利用23号数据标定出阈值
Q5minPredict=np.zeros((288,16))
Q5minPredict[:,0]=range(288)
for i in range(288):
    if i<=3:
        Q5minPredict[i,1]=Q5min2[i,1]
        Q5minPredict[i,2]=Q5min2[i,1]
        Q5minPredict[i,3]=0
        Q5minPredict[i,4]=Q5min2[i,2]
        Q5minPredict[i,5]=Q5min2[i,2]
        Q5minPredict[i,6]=0
        Q5minPredict[i,7]=Q5min2[i,3]
        Q5minPredict[i,8]=Q5min2[i,3]
        Q5minPredict[i,9]=0
        Q5minPredict[i,10]=Q5min2[i,4]
        Q5minPredict[i,11]=Q5min2[i,4]
        Q5minPredict[i,12]=0
        Q5minPredict[i,13]=Q5min2[i,5]
        Q5minPredict[i,14]=Q5min2[i,5]
        Q5minPredict[i,15]=0
        
    else :
        Q5minPredict[i,1]=Q5min2[i,1]
        Q5minPredict[i,2]=np.mean(Q5min2[i-4:i,1])
        Q5minPredict[i,3]=-(Q5minPredict[i,1]-Q5minPredict[i,2])
        Q5minPredict[i,4]=Q5min2[i,2]
        Q5minPredict[i,5]=np.mean(Q5min2[i-4:i,2])
        Q5minPredict[i,6]=-(Q5minPredict[i,4]-Q5minPredict[i,5])
        Q5minPredict[i,7]=Q5min2[i,3]
        Q5minPredict[i,8]=np.mean(Q5min2[i-4:i,1])
        Q5minPredict[i,9]=-(Q5minPredict[i,7]-Q5minPredict[i,8])
        Q5minPredict[i,10]=Q5min2[i,4]
        Q5minPredict[i,11]=np.mean(Q5min2[i-4:i,4])
        Q5minPredict[i,12]=-(Q5minPredict[i,10]-Q5minPredict[i,11])
        Q5minPredict[i,13]=Q5min2[i,5]
        Q5minPredict[i,14]=np.mean(Q5min2[i-4:i,5])
        Q5minPredict[i,15]=-(Q5minPredict[i,13]-Q5minPredict[i,14])
        
        

#取各车道的阈值
K2=np.percentile(Q5minPredict[:,3],90)

K3=np.percentile(Q5minPredict[:,6],90)

K4=np.percentile(Q5minPredict[:,9],90)

K5=np.percentile(Q5minPredict[:,12],90)


K6=np.percentile(Q5minPredict[:,15],90)








def predict(Q5min2):
    Q5minPredict=np.zeros((288,16))
    Q5minPredict[:,0]=range(288)
    for i in range(288):
        if i<=3:
            Q5minPredict[i,1]=Q5min2[i,1]
            Q5minPredict[i,2]=Q5min2[i,1]
            Q5minPredict[i,3]=0
            Q5minPredict[i,4]=Q5min2[i,2]
            Q5minPredict[i,5]=Q5min2[i,2]
            Q5minPredict[i,6]=0
            Q5minPredict[i,7]=Q5min2[i,3]
            Q5minPredict[i,8]=Q5min2[i,3]
            Q5minPredict[i,9]=0
            Q5minPredict[i,10]=Q5min2[i,4]
            Q5minPredict[i,11]=Q5min2[i,4]
            Q5minPredict[i,12]=0
            Q5minPredict[i,13]=Q5min2[i,5]
            Q5minPredict[i,14]=Q5min2[i,5]
            Q5minPredict[i,15]=0
            
        else :
            Q5minPredict[i,1]=Q5min2[i,1]
            Q5minPredict[i,2]=np.mean(Q5min2[i-4:i,1])
            Q5minPredict[i,3]=-(Q5minPredict[i,1]-Q5minPredict[i,2])
            Q5minPredict[i,4]=Q5min2[i,2]
            Q5minPredict[i,5]=np.mean(Q5min2[i-4:i,2])
            Q5minPredict[i,6]=-(Q5minPredict[i,4]-Q5minPredict[i,5])
            Q5minPredict[i,7]=Q5min2[i,3]
            Q5minPredict[i,8]=np.mean(Q5min2[i-4:i,1])
            Q5minPredict[i,9]=-(Q5minPredict[i,7]-Q5minPredict[i,8])
            Q5minPredict[i,10]=Q5min2[i,4]
            Q5minPredict[i,11]=np.mean(Q5min2[i-4:i,4])
            Q5minPredict[i,12]=-(Q5minPredict[i,10]-Q5minPredict[i,11])
            Q5minPredict[i,13]=Q5min2[i,5]
            Q5minPredict[i,14]=np.mean(Q5min2[i-4:i,5])
            Q5minPredict[i,15]=-(Q5minPredict[i,13]-Q5minPredict[i,14])
    return Q5minPredict



Q5minPredict2=predict(Q5min)




#计算是否触发
#第1列时间，第2列为车道2是否触发阈值，第3列为车道3是否触发阈值，第4列为车道3是否触发阈值
Ktouch=np.zeros((288,7))
Ktouch[:,0]=range(288)
for i in range(288):
    if Q5minPredict2[i,3]>K2+5:
        Ktouch[i,1]=1
    if Q5minPredict2[i,6]>K3+5:
        Ktouch[i,2]=2
    if Q5minPredict2[i,9]>K4+5:
        Ktouch[i,3]=3
    if Q5minPredict2[i,12]>K5+5:
        Ktouch[i,4]=4
    if Q5minPredict2[i,15]>K6+5:
        Ktouch[i,5]=5
    if Tt5min[i,1]>538/5*3.6:
        Ktouch[i,6]=6



#绘制触发状态图
a1=plt.figure()
a1=plt.plot(Ktouch[:,0],Ktouch[:,1],'o-',label='clane2')
a1=plt.plot(Ktouch[:,0],Ktouch[:,2],'o-',label='clane3')
a1=plt.plot(Ktouch[:,0],Ktouch[:,3],'o-',label='clane4')
a1=plt.plot(Ktouch[:,0],Ktouch[:,4],'o-',label='clane5')
a1=plt.plot(Ktouch[:,0],Ktouch[:,5],'o-',label='claneAll')
a1=plt.plot(Ktouch[:,0],Ktouch[:,6],'o-',label='TT')
a1=plt.xlim(0,288)
#a1=plt.ylim(0,900)    
plt.legend()   























































