# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:23:03 2017

@author: Administrator
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *




#预处理分车道
dataDeal1=loopDeal(match_total_final1,claneNum=[3,4,5,6])
dataDeal2=loopDeal(match_total_final2,claneNum=[1,2,3])
dataDeal3=loopDeal(match_total_final3,claneNum=[1,2])
dataDeal4=loopDeal(match_total_final4,claneNum=[1,2])


dataDeal5=loopDeal(match_total_final5,claneNum=[1,2,3])
dataDeal6=loopDeal(match_total_final6,claneNum=[3,4,5])
dataDeal7=loopDeal(match_total_final7,claneNum=[1,2])
dataDeal8=loopDeal(match_total_final8,claneNum=[1,2])
dataDeal9=loopDeal(match_total_final9,claneNum=[1,2,3,4])
dataDeal10=loopDeal(match_total_final10,claneNum=[1,2,3,4])




#实验道路，重点道路，初步得到15min平均行程时间
tt_deal_5min9=[]
for i in range(len(dataDeal10)):
    med_data=dataDeal10[i]
    med_deal=deal_5min(med_data,num=3,day=i,data_full=85.9)
    med_deal2=pd.DataFrame(med_deal)
    tt_deal_5min9.append(med_deal2)
#以下几步只是为了获取夜间自由流速度，取15%分位值
match_final_1 = pd.concat(tt_deal_5min9, ignore_index=True)    
match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<28)]
np.percentile(c.iloc[:,1],15) #获得自由流速度为68.3

def loop_15min(dataDeal,num1=3):
    deal_15min_1=[]
    for i in range(len(dataDeal)):
        med_data=dataDeal[i]
        med_deal=deal_5min(med_data,num=num1,day=i,data_full=-1)
        med_deal2=pd.DataFrame(med_deal)
        deal_15min_1.append(med_deal2)
    match_final_1 = pd.concat(tt_deal_5min9, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<28)]
    data_full1=np.percentile(c.iloc[:,1],15)
    deal_15min_2=[]
    for z in range(len(dataDeal)):
        med_data=dataDeal[z]
        med_deal=deal_5min(med_data,num=num1,day=i,data_full=data_full1)
        med_data1=np.array(med_deal)
        for j in range(96):
            if med_data1[j,5]==1:
                d=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data1[j,4])]
                if len(d)>0:
                   med_data1[j,5]=np.mean(c.iloc[:,1])
                elif len(d)==0:
                   med_data1[j,5]= med_data1[j-1,5]
        deal_15min_2.append(med_data1)
        
        
    





#补全数据，完全没有数据的情况进行补全
tt_deal_5min9_1=[]
for i in range(len(dataDeal10)):
    med_data=np.array(tt_deal_5min9[i])
    for j in range(96):
        if med_data[j,5]==1:
            c=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data[j,4])]
            if len(c)>0:
               med_data[j,5]=np.mean(c.iloc[:,1])
            elif len(c)==0:
               med_data[j,5]= med_data[j-1,5]
    tt_deal_5min9_1.append(med_data)  


    
    
    tt_deal3_5min3=[]
    for i in range(len(dataDeal10)): 
        med_data=np.array(tt_deal_5min9_1[i])
        for j in range(1,96):
            med_data[j,5]=math.exp(0.8*math.log(med_data[j,5])+0.2*math.log(med_data[j-1,5]))
        tt_deal3_5min3.append(med_data)       
    
    
    
    
    
    
    
    
    
#绘制数据预处理图
    a1=plt.figure()
    for i in range(34):
        a1=plt.subplot(5,7,i+1)
        a1=plt.scatter(dataDeal3[i].iloc[:,1],dataDeal3[i].iloc[:,8],s=15)
        a1=plt.xlim(0,86400)
        a1=plt.ylim(0,900)


        
        
        
#绘制补全数据过后的图
    fig, ax = plt.subplots(5,7,figsize=(6,5))
    for i in range(len(dataDeal10)):
        plt.subplot(5,7,i+1)
        plt.plot(tt_deal_5min9_1[i][:,0],pd.Series(tt_deal_5min9_1[i][:,5]).map(stateMap),'o-',markersize=3) 
        plt.plot( tt_deal3_5min3[i][:,0], pd.Series(tt_deal3_5min3[i][:,5]).map(stateMap),'o-',markersize=3) 
#        xticks =range(0,25)
#        ax[i].set_xticks(xticks)
#        ax[i].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
        plt.xlim(0,24.1)
#        plt.ylim(0,900) 

 
    fig, ax = plt.subplots(5,7,figsize=(6,5))
    for i in range(len(dataDeal10)):
        plt.subplot(5,7,i+1)
        plt.plot(tt_deal_5min9_1[i][:,0],pd.Series(tt_deal_5min9_1[i][:,5]),'o-',markersize=3) 
        plt.plot( tt_deal3_5min3[i][:,0], pd.Series(tt_deal3_5min3[i][:,5]),'o-',markersize=3) 
#        xticks =range(0,25)
#        ax[i].set_xticks(xticks)
#        ax[i].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
        plt.xlim(0,24.1)
        plt.ylim(0,900) 


        
        
        
        
        
        
        
        
        
        

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
gbm0 = GradientBoostingRegressor(n_estimators=360,min_samples_split=50,
                                  min_samples_leaf=20,max_depth=13,max_features='sqrt')    
gbm0.fit(train_x,train_y)  





























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
