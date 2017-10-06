# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:28:33 2017

@author: wutongshu
"""
import sys
sys.path.append('D:\python_script\predict')
from all_func import *
tt_deal_5min=[]
for i in range(28):
    med_data=tt_deal[i]
    med_deal=deal_5min(med_data,num=2,day=i,data_full=61.3)
    med_deal2=pd.DataFrame(med_deal)
    tt_deal_5min.append(med_deal2)
#以下几步只是为了获取夜间自由流速度，取15%分位值
match_final_1 = pd.concat(tt_deal_5min, ignore_index=True)    
match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
np.percentile(c.iloc[:,1],15) 
#补全数据    
    tt_deal_5min2=[]
    for i in range(28): 
        med_data=np.array(tt_deal_5min[i])
        for j in range(288):
            if med_data[j,5]==1:
                c=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data[j,4])]
                if len(c)>0:
                   med_data[j,5]=np.mean(c.iloc[:,1])
                elif len(c)==0:
                   med_data[j,5]= med_data[j-1,5]
        tt_deal_5min2.append(med_data)        
#平滑数据           
    tt_deal_5min3=[]
    for i in range(28): 
        med_data=np.array(tt_deal_5min2[i])
        for j in range(1,288):
            med_data[j,5]=math.exp(0.8*math.log(med_data[j,5])+0.2*math.log(med_data[j-1,5]))
        tt_deal_5min3.append(med_data)     
        
        
        
        
    tt_deall_5min=[]
    for i in range(28):
        med_data=tt_deall[i]
        med_deal=deal_5min(med_data,num=2,day=i,data_full=76.3)
        med_deal2=pd.DataFrame(med_deal)
        tt_deall_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deall_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
    np.percentile(c.iloc[:,1],15) 
#补全数据    
    tt_deall_5min2=[]
    for i in range(28): 
        med_data=np.array(tt_deall_5min[i])
        for j in range(288):
            if med_data[j,5]==1:
                c=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data[j,4])]
                if len(c)>0:
                   med_data[j,5]=np.mean(c.iloc[:,1])
                elif len(c)==0:
                   med_data[j,5]= med_data[j-1,5]
        tt_deall_5min2.append(med_data)        
#平滑数据           
    tt_deall_5min3=[]
    for i in range(28): 
        med_data=np.array(tt_deall_5min2[i])
        for j in range(1,288):
            med_data[j,5]=math.exp(0.8*math.log(med_data[j,5])+0.2*math.log(med_data[j-1,5]))
        tt_deall_5min3.append(med_data)             
        
        
    tt_deal3_5min=[]
    for i in range(28):
        med_data=tt_deal3[i]
        med_deal=deal_5min(med_data,num=2,day=i,data_full=76.3)
        med_deal2=pd.DataFrame(med_deal)
        tt_deal3_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deal3_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
    np.percentile(c.iloc[:,1],15) 
#补全数据    
    tt_deal3_5min2=[]
    for i in range(28): 
        med_data=np.array(tt_deal3_5min[i])
        for j in range(288):
            if med_data[j,5]==1:
                c=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data[j,4])]
                if len(c)>0:
                   med_data[j,5]=np.mean(c.iloc[:,1])
                elif len(c)==0:
                   med_data[j,5]= med_data[j-1,5]
        tt_deal3_5min2.append(med_data)        
#平滑数据           
    tt_deal3_5min3=[]
    for i in range(28): 
        med_data=np.array(tt_deal3_5min2[i])
        for j in range(1,288):
            med_data[j,5]=math.exp(0.8*math.log(med_data[j,5])+0.2*math.log(med_data[j-1,5]))
        tt_deal3_5min3.append(med_data)             