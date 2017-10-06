# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 13:09:15 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *


        



#获得15min信息发布的匹配率
rateMat1= matchRate(matchTotal=match_total_tt1,clane=[3,4,5])           
rateMat2= matchRate(matchTotal=match_total_tt2,clane=[1,2,3,4,5])             
rateMat3= matchRate(matchTotal=match_total_tt3,clane=[1,2,3,4]) 
rateMat4= matchRate(matchTotal=match_total_tt4,clane=[1,2,3,4]) 



        
#得到各分位值的相关分位数        
rateQ1=rateQuan(rateMat1)
rateQ2=rateQuan(rateMat2)
rateQ3=rateQuan(rateMat3)
rateQ4=rateQuan(rateMat4)



#绘制匹配率
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
c=np.linspace(0,24,96)
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.09, bottom=0.06, top=0.95,right=0.93,hspace=0.23,wspace=0.23) 
for i in range(34):
    plt.ylim(-0.1,0.9)
#    plt.subplot(5,7,i+1)
    a1=rateMat1[i,:]
    plt.plot(c,a1,label='link1')
    if i<31:
        a2=rateMat2[i,:]
        plt.plot(c,a2,label='link2')
    
    a3=rateMat3[i,:]
    plt.plot(c,a3,label='link3')
    a4=rateMat4[i,:]
    plt.plot(c,a4,label='link4')
    plt.legend(loc=0)
    sns.despine()   
plt.savefig('F:\python_script\data_deal/rate3.png',dpi=200) 
    
    
    
    

#绘制分位值
import matplotlib as mpl
import pylab as pl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(4,1,figsize=(11,11))
#plt.subplots_adjust(left=0.09, bottom=0.05, top=0.95,right=0.93,hspace=0.23,wspace=0.23) 

a=np.arange(34)
b=np.arange(31)
pl.ylim(0,0.85)
ax[0].plot(a,rateQ1[:,0],label='5%')
ax[0].plot(a,rateQ1[:,1],label='15%')
ax[0].plot(a,rateQ1[:,2],label='35%')
ax[0].plot(a,rateQ1[:,3],label='50%')
ax[0].plot(a,rateQ1[:,4],label='75%')
ax[0].legend(loc=0)
sns.despine() 

ax[1].plot(b,rateQ2[:,0],label='5%')
ax[1].plot(b,rateQ2[:,1],label='15%')
ax[1].plot(b,rateQ2[:,2],label='35%')
ax[1].plot(b,rateQ2[:,3],label='50%')
ax[1].plot(b,rateQ2[:,4],label='75%')
ax[1].legend(loc=0)
sns.despine() 




ax[2].plot(a,rateQ3[:,0],label='5%')
ax[2].plot(a,rateQ3[:,1],label='15%')
ax[2].plot(a,rateQ3[:,2],label='35%')
ax[2].plot(a,rateQ3[:,3],label='50%')
ax[2].plot(a,rateQ3[:,4],label='75%')
ax[2].legend(loc=0)
sns.despine() 

ax[3].plot(a,rateQ4[:,0],label='5%')
ax[3].plot(a,rateQ4[:,1],label='15%')
ax[3].plot(a,rateQ4[:,2],label='35%')
ax[3].plot(a,rateQ4[:,3],label='50%')
ax[3].plot(a,rateQ4[:,4],label='75%')
ax[3].legend(loc=0)
sns.despine() 
plt.savefig('F:\python_script\data_deal/rateQ.png',dpi=200) 


































    
    
    




 















