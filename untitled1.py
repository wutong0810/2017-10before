# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 20:16:36 2017

@author: wutongshu
"""


        
match_du=match_total_final1[6] 
match_du1=match_du[match_du.iloc[:,2]!=1]       
a0=plt.scatter(match_du1.iloc[:,1],match_du1.iloc[:,9],s=15)
 
match_du2=match_total_final[6]  
match_du3=match_du2[(match_du2.iloc[:,2]==3)|(match_du2.iloc[:,2]==4)|(match_du2.iloc[:,2]==5)|(match_du2.iloc[:,2]==6)] 
a0=plt.scatter(match_du1.iloc[:,1],match_du1.iloc[:,9],s=15)
a0=plt.scatter(match_du3.iloc[:,1],match_du3.iloc[:,9],s=15)
 
 
test=match_du3.iloc[:,[0,1,2,3,4,6,7,8,9]]
med_data=np.array(test)
med_deal1=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1) 
a0=plt.scatter(med_deal1.iloc[:,1],med_deal1.iloc[:,8],s=15)
 
 
test=match_du1.iloc[:,[0,1,2,3,4,6,7,8,9]]
med_data=np.array(test)
med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
a0=plt.scatter(med_deal.iloc[:,1],med_deal.iloc[:,8],s=15) 
#上游

aa=deal_5min(med_deal,num=1,length=575,day=0)
aa1=deal_5min(med_deal1,num=1,length=575,day=0)
plt.plot(aa[:,0],aa[:,5],'o-')
plt.plot(aa1[:,0],aa1[:,5],'o-')
np.corrcoef(aa[:,5],aa1[:,5])




















11,25