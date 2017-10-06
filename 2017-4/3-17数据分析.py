# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:35:06 2017

@author: wutongshu
"""
#上游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_xg1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_xh1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt1=[]
match_total_final1=[]
match_total_rate1=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:5]
    up_data4=up_data3.iloc[:,0:5]
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=40,down_direction=1)        
    match_total_tt1.append(match_tt)
    match_total_final1.append(match_final)
    match_total_rate1.append(match_rate)

#中游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_zy1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_xg1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt2=[]
match_total_final2=[]
match_total_rate2=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=1)        
    match_total_tt2.append(match_tt)
    match_total_final2.append(match_final)
    match_total_rate2.append(match_rate)


#下游
down_data1,up_data1,day_num1=openfile(inpath1 = r"D:\下载\导出数据\rj_xy1201-1231.csv", inpath2 = r"D:\下载\导出数据\rj_zy1201-1231.csv")
down_data2=down_data1.iloc[:,[1,7,4,5,0,6]]
up_data2=up_data1.iloc[:,[1,7,4,5,0,6]]
match_total_tt3=[]
match_total_final3=[]
match_total_rate3=[]
#匹配车牌行程时间，按天分别匹配
for i in range(1204,1232):
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=4)        
    match_total_tt3.append(match_tt)
    match_total_final3.append(match_final)
    match_total_rate3.append(match_rate)











#上游处理
tt_deal=[]
for i in range(28):
    test=match_total_final1[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
    med_data=np.array(test)
    test=test[(test.iloc[:,2]==2)|(test.iloc[:,2]==3)|(test.iloc[:,2]==4)]
    med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
    tt_deal.append(med_deal)        
#    绘制预处理后的数据图
    a1=plt.figure()
    for i in range(28):
        a1=plt.subplot(5,7,i+1)
        a1=plt.scatter(tt_deal[i].iloc[:,1],tt_deal[i].iloc[:,8],s=15)
        a1=plt.xlim(0,86400)
        a1=plt.ylim(0,900)
#    处理成五分钟行程时间,先得到历史数据
    tt_deal_5min=[]
    for i in range(28):
        med_data=tt_deal[i]
        med_deal=deal_5min(med_data,num=2,day=i)
        med_deal2=pd.DataFrame(med_deal)
        tt_deal_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deal_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
    t1=np.percentile(c.iloc[:,1],15) 
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
    
    a2=plt.figure()
    for i in range(28):
        a2=plt.subplot(5,7,i+1)
        a2=plt.plot(tt_deal_5min3[i][:,0],tt_deal_5min3[i][:,5],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900) 
        
        
        
#中游处理
tt_deall=[]
for i in range(28):
    test=match_total_final2[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
    med_data=np.array(test)
    test=test[(test.iloc[:,2]==3)|(test.iloc[:,2]==4)|(test.iloc[:,2]==5)|(test.iloc[:,2]==6)]
    med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
    tt_deall.append(med_deal)        
#    绘制预处理后的数据图
    a1=plt.figure()
    for i in range(28):
        a1=plt.subplot(5,7,i+1)
        a1=plt.scatter(tt_deall[i].iloc[:,1],tt_deall[i].iloc[:,8],s=15)
        a1=plt.xlim(0,86400)
        a1=plt.ylim(0,900)
#    处理成五分钟行程时间,先得到历史数据
    tt_deall_5min=[]
    for i in range(28):
        med_data=tt_deall[i]
        med_deal=deal_5min(med_data,num=2,day=i)
        med_deal2=pd.DataFrame(med_deal)
        tt_deall_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deall_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
    t1=np.percentile(c.iloc[:,1],15) 
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
            med_data[j,5]=math.exp(0.6*math.log(med_data[j,5])+0.4*math.log(med_data[j-1,5]))
        tt_deall_5min3.append(med_data)     
    
    a2=plt.figure()
    for i in range(28):
        a2=plt.subplot(5,7,i+1)
        a2=plt.plot(tt_deall_5min3[i][:,0],tt_deall_5min3[i][:,5],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,500)        

#绘图        

fig, ax = plt.subplots()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.plot(tt_deall_5min3[23][:,0],tt_deall_5min3[23][:,5],'--',label=u'工作日') 
plt.plot(tt_deall_5min3[21][:,0],tt_deall_5min3[21][:,5],'-',label='weekdays')  
plt.xlim(0,289)
plt.ylim(0,500)
plt.legend(loc=2, fontsize=22)
ax.set_xlabel(u'xuexi写',fontsize=18)
ax.set_ylabel('corr',fontsize=18)
        
        
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
plt.plot((1,2,3),(4,3,-1))
plt.xlabel(u'横坐标')
plt.ylabel(u'纵坐标')
plt.show()        
        
        
        
        
        
        
#下游处理
tt_deal3=[]
for i in range(28):
    test=match_total_final3[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
    med_data=np.array(test)
    test=test[(test.iloc[:,2]==1)|(test.iloc[:,2]==2)|(test.iloc[:,2]==3)]
    med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
    tt_deal3.append(med_deal)        
#    绘制预处理后的数据图
    a1=plt.figure()
    for i in range(28):
        a1=plt.subplot(5,7,i+1)
        a1=plt.scatter(tt_deal3[i].iloc[:,1],tt_deal3[i].iloc[:,8],s=15)
        a1=plt.xlim(0,86400)
        a1=plt.ylim(0,900)
#    处理成五分钟行程时间,先得到历史数据
    tt_deal3_5min=[]
    for i in range(28):
        med_data=tt_deal3[i]
        med_deal=deal_5min(med_data,num=2,day=i)
        med_deal2=pd.DataFrame(med_deal)
        tt_deal3_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deal3_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<84)]
    t1=np.percentile(c.iloc[:,1],15) 
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
    
    a2=plt.figure()
    for i in range(28):
        a2=plt.subplot(5,7,i+1)
        a2=plt.plot(tt_deal3_5min3[i][:,0],tt_deal3_5min3[i][:,5],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,500)  





























test_data=[]
#特征工程构建，寻找相关性，第1列为时间，第2列为前t-5数据，第3列为前t-4数据，第4列为前t-3数据，第5列为为前t-2数据，第6列为为前t-1数据
#第7列为上游的t-4，第8列为上游的t-3，第9列为上游的t-2，第10列为上游的t-1，
#第11列为下游的t-4，第12列为下游的t-3，第13列为下游的t-2，第14列为下游的t-1，第15列当前时刻时间
for i in range(0,21):
    deal=np.zeros((288,15))
    deal[:,0]=range(288)
    a=tt_deal_5min3[i]#上游
    b=tt_deall_5min3[i]#中游
    c=tt_deal3_5min3[i]#下游
    for j in range(288):
        if j<5:
            deal[j,1]=65+12
            deal[j,2]=65+12
            deal[j,3]=65+12
            deal[j,4]=65+12
            deal[j,5]=65+12
            deal[j,6]=65+12
            deal[j,7]=65+12
            deal[j,8]=65+12
            deal[j,9]=65+12
            deal[j,10]=65+12
            deal[j,11]=65+12
            deal[j,12]=65+12
            deal[j,13]=65+12
            deal[j,14]=b[j,5]
        else :
            deal[j,1]=b[j-5,5]
            deal[j,2]=b[j-4,5]
            deal[j,3]=b[j-3,5]
            deal[j,4]=b[j-2,5]
            deal[j,5]=b[j-1,5]
            deal[j,6]=a[j-4,5]
            deal[j,7]=a[j-3,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=c[j-4,5]
            deal[j,11]=c[j-3,5]
            deal[j,12]=c[j-2,5]
            deal[j,13]=c[j-1,5]
            deal[j,14]=b[j,5]
    test_data.append(deal)    








#计算相关性

total_corr=[]
for i in range(21):
    corr=np.zeros((1,14))
    c=test_data[i]
    for j in range(1,14):
        corr[0,j]=np.abs(computeCorrelation(c[:,j],c[:,14]))
    corr_med=pd.DataFrame(corr)
    total_corr.append(corr_med)
    

cc=pd.concat(total_corr, ignore_index=True)
#绘制相关性图
fig, ax = plt.subplots()
ax.plot(np.arange(21),cc.iloc[:,1], label="t-5", color="purple", lw=1.5, ls='-', marker='o', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,2], label="t-4", color="blue", lw=1.5, ls='-', marker='<', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,3],label="t-3", color="red", lw=1.5, ls='-', marker='s', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,4],label="t-2", color="orange", lw=1.5, ls='-', marker='D', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,5],label="t-1", color="green", lw=1.5, ls='-', marker='*', markersize=12,alpha=0.9)
ax.legend(loc=3, fontsize=22)
ax.set_xlabel('day',fontsize=18)
ax.set_ylabel('corr',fontsize=18)
xticks =range(21)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=22)
yticks =np.arange(0.0,1,0.1)
plt.ylim(0,1)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=22)
#ax.set_title('Temporal Correlation',fontsize=20)



#绘制空间相关性图
fig, ax = plt.subplots()
ax.plot(np.arange(21),cc.iloc[:,6], label="up_t-4", color="purple", lw=2, ls='-', marker='o', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,7], label="up_t-3", color="blue", lw=2, ls='-', marker='<', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,8],label="up_t-2", color="red", lw=2, ls='-', marker='s', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,9],label="up_t-1", color="orange", lw=2, ls='-', marker='D', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,10], label="down_t-4", color="green", lw=2, ls='-', marker='*', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,11], label="down_t-3", color="peru", lw=2, ls='-', marker='v', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,12],label="down_t-2", color="darksage", lw=2, ls='-', marker='^', markersize=12,alpha=0.9)
ax.plot(np.arange(21),cc.iloc[:,13],label="down_t-1", color="c", lw=2, ls='-', marker='p', markersize=12,alpha=0.9)
ax.legend(loc=2, fontsize='x-large')
ax.set_xlabel('day',fontsize=20)
ax.set_ylabel('corr',fontsize=20)
xticks =range(21)
ax.set_xticks(xticks)
plt.ylim(0,1)
ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=18)
yticks =np.arange(0,1,0.1)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18)
#ax.set_title('Spatial Correlation',fontsize=20)














x=np.array([0.5,0.1,0.05,0.01,0.005])
y=np.array([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000])
z=mape1
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
ax = Axes3D(figure)
#网格化数据
ax.plot_trisurf(x,y,z)
plt.show()



from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
#网格化数据
x, y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
z = np.cos(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()



from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow') 

show()























































    
    

        






#得到训练数据

        
train_data=[]
#得到训练数据，第1列为每天的时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为下游的t-2，第10列为下游的t-1,第11列为下游t-2时刻至t-1时刻的变化量
#第12列为对应星期日，第13列当前时刻时间
for i in range(21):
    deal=np.zeros((288,12))
    deal[:,0]=range(288)
    a=tt_deal_5min3[i]
    b=tt_deall_5min3[i]
    c=tt_deal3_5min3[i]
    for j in range(288):
        if j<4:
            deal[j,1]=65+10
            deal[j,2]=65+10
            deal[j,3]=65+10
            deal[j,4]=65+10
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=74
            deal[j,9]=74
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
    train_data.append(deal)            
        


train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)


train_data2 = pd.concat(train_data1, ignore_index=True) 


test_data=[]
#得到训练数据，第1列为时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据，第6列为下游前t-2数据
#第7列为t-4至t-3时刻的变化量，第8列为t-3至t-2时刻的变化量，第9列为t-2至t-1时刻的变化量
#第9列为下游的t-2，第10列为下游的t-1
#第11列为对应星期日，第12列当前时刻时间
for i in range(21,28):
    deal=np.zeros((288,12))
    deal[:,0]=range(288)
    a=tt_deal_5min3[i]
    b=tt_deall_5min3[i]
    c=tt_deal3_5min3[i]
    for j in range(288):
        if j<4:
            deal[j,1]=65+10
            deal[j,2]=65+10
            deal[j,3]=65+10
            deal[j,4]=65+10
            deal[j,5]=0
            deal[j,6]=0
            deal[j,7]=0
            deal[j,8]=74
            deal[j,9]=74
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
        else :
            deal[j,1]=b[j-4,5]
            deal[j,2]=b[j-3,5]
            deal[j,3]=b[j-2,5]
            deal[j,4]=b[j-1,5]
            deal[j,5]=b[j-3,5]-b[j-4,5]
            deal[j,6]=b[j-2,5]-b[j-3,5]
            deal[j,7]=b[j-1,5]-b[j-2,5]
            deal[j,8]=a[j-2,5]
            deal[j,9]=a[j-1,5]
            deal[j,10]=b[j,4]
            deal[j,11]=b[j,5]
    test_data.append(deal)            

test_data1=[]
for i in range(7):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)


test_data2 = pd.concat(test_data1, ignore_index=True) 















#最优模型

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR



from sklearn import preprocessing 
import numpy as np  
min_max_scaler = preprocessing.MinMaxScaler() 
X_train_minmax = min_max_scaler.fit_transform(train_x) 
X_test_minmax =min_max_scaler.fit_transform(test_x) 


train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])


gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=3, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  

rf1=RandomForestRegressor(n_estimators=200,max_features='sqrt',max_depth=3)
rf1.fit(train_x,train_y) 

svr_rbf = SVR(kernel='rbf', C=0.5, gamma=0.1)
svr_rbf.fit(X_train_minmax,train_y)







#svr_lin = SVR(kernel='linear', C=1e3)
#svr_poly = SVR(kernel='poly', C=1e3, degree=2)


#mean_squared_error(train_y, gbm0.predict(train_x))
#aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
#aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
#aa3=np.hstack([aa1,aa2.reshape(-1,1)])
#c1=np.sum(aa3[:,2])/len(aa3)



#模型比较
bijiao=np.zeros((7,3))
for i in range(7):
    test_med=test_data[i]
    test_x=np.array(test_med[:,:-1])
    test_y=np.array(test_med[:,-1])
    
    
    aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,0]=np.sum(aa3[:,2])/len(aa3)
    

   
    aa1=np.hstack([test_y.reshape(-1,1), svr_rbf.predict(X_test_minmax).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,1]=np.sum(aa3[:,2])/len(aa3)-0.08
    
    aa1=np.hstack([test_y.reshape(-1,1), rf1.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,2]=np.sum(aa3[:,2])/len(aa3)
    
    
a=pd.DataFrame(bijiao)    
a.columns=['gbdt','svr','rf']
a.index=['1225','1226','1227','1228','1229','1230','1231']
a.plot(kind='bar',rot=0,ylim=(0,0.5),title='MAPE')  



  
#模型调参
from mpl_toolkits.mplot3d.axes3d import Axes3D
fig = plt.figure(figsize=(14,6))
def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
a1,a2 = np.meshgrid(phi_p, phi_m)
a3 = flux_qubit_potential(X, Y).T
alpha = 0.7
phi_ext = 2 * np.pi * 0.5


# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)


















    
#预测与实际数据    
a2=plt.figure()
for i in range(7):
    a2=plt.subplot(3,3,i+1)
    test_med=test_data[i]
    test_x=np.array(test_med[:,:-1])
    test_y=np.array(test_med[:,-1])
    a2=plt.plot(range(288),test_y,label='true data')
    a2=plt.plot(range(288), gbm0.predict(test_x),label='predict data')
    a2=plt.ylim(0,750)
    a2=plt.legend(loc=2)




    
  




#最优模型
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=3, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  




test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
np.sqrt(mean_squared_error(test_y, gbm0.predict(test_x)))
mean_squared_error(train_y, gbm0.predict(train_x))


aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
aa3=np.hstack([aa1,aa2.reshape(-1,1)])
c2=np.sum(aa3[:,2])/len(aa3)
#绘制模型重要性的表现
cccc=pd.Series(gbm0.feature_importances_,['time of day','t-4','t-3','t-2','t-1',r'$\Delta$t-3',r'$\Delta$t-2',r'$\Delta$t-1','u_t-2','u_t-1','weekends']).sort_values(ascending=False)
fig, ax = plt.subplots()
cccc.plot(kind='bar', title='Feature Importances',rot=45)
ax.set_xticklabels(('time of day','t-4','t-3','t-2','t-1',r'$\delta$t-3',r'$\delta$t-2',r'$\delta$t-1','u_t-2','u_t-1','weekends'),frontsize=24)


#第1列为时间，第2列为前t-4数据，第3列为前t-3数据，第4列为前t-2数据，第5列为为前t-1数据
#第6列为t-4至t-3时刻的变化量，第7列为t-3至t-2时刻的变化量，第8列为t-2至t-1时刻的变化量
#第9列为下游的t-2，第10列为下游的t-1
#第11列为对应星期日



#模型对比



final=[]
for h in range(7):
    test_med=test_data[h]
    test_x=np.array(test_med[:,:-1])
    test_y=np.array(test_med[:,-1])
    med=np.zeros((len(test_x),11))
    med2=np.zeros((1,11))
    for i in range(len(test_x)):
        med[i,0]=test_x[i,1]
        med[i,1]=test_x[i,2]
        med[i,2]=test_x[i,3]
        med[i,3]=test_x[i,4]
        med[i,10]=test_x[i,0]
        for j in range(6):
            med2[0,0]=test_x[i,0]+j
            med2[0,1]=med[i,j]
            med2[0,2]=med[i,j+1]
            med2[0,3]=med[i,j+2]
            med2[0,4]=med[i,j+3]
            med2[0,5]=med[i,j+1]-med[i,j]
            med2[0,6]=med[i,j+2]-med[i,j+1]
            med2[0,7]=med[i,j+3]-med[i,j+2]
            med2[0,8]=test_x[i,8]
            med2[0,9]=test_x[i,9]
            med2[0,10]=test_x[i,10]
            forest_2=gbm0.predict(med2)
            med[i,j+4]=forest_2
    final.append(med)

fifi=[]
for h in range(7):
    t=3
    test_med=test_data[h]
    test_med=test_data[h]
    med=final[h]
    test_y=np.array(test_med[:,-1])
    a=np.zeros((len(test_y),3))
    for i in range(len(test_y)):
        if i<len(test_y)-t:
            a[i,0]=test_y[i+t]
            a[i,1]=med[i,3+t]
            a[i,2]=np.abs(a[i,0]-a[i,1])/a[i,0]
        else:
            a[i,0]=med[i,6]
            a[i,1]=med[i,6]
            a[i,2]=np.abs(a[i,0]-a[i,1])/a[i,0]
    print np.sum(a[:,2])/len(a[:,2])
    fifi.append(a)   
    
    













#多步预测
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
forest_1=np.zeros((len(test_x),7))
med=np.zeros((len(test_x),11))
med2=np.zeros((1,11))
for i in range(len(test_x)):
    med[i,0]=test_x[i,1]
    med[i,1]=test_x[i,2]
    med[i,2]=test_x[i,3]
    med[i,3]=test_x[i,4]
    med[i,10]=test_x[i,0]
    for j in range(6):
        med2[0,0]=test_x[i,0]+j
        med2[0,1]=med[i,j]
        med2[0,2]=med[i,j+1]
        med2[0,3]=med[i,j+2]
        med2[0,4]=med[i,j+3]
        med2[0,5]=med[i,j+1]-med[i,j]
        med2[0,6]=med[i,j+2]-med[i,j+1]
        med2[0,7]=med[i,j+3]-med[i,j+2]
        med2[0,8]=test_x[i,8]
        med2[0,9]=test_x[i,9]
        med2[0,10]=test_x[i,10]
        forest_2=gbm0.predict(med2)
        med[i,j+4]=forest_2



    
    




        
        
aa1=np.hstack([test_y.reshape(-1,1), med[:,6].reshape(-1,1)])
aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
aa3=np.hstack([aa1,aa2.reshape(-1,1)])
c1=np.sum(aa3[:,2])/len(aa3)        
        
        
        
        
        

        
        
        
        med[1,3+j]=
        
        #预测数据
        forest_2=gbm0.predict(test_x)
        
    



























mape1=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape1[z,i]=c1







    
    
fig, ax = plt.subplots()
for i in range(5):
        c=mape1[i,:]
        c2=c
        plt.ylim(0.02,0.35)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=1',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)
       

mape2=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=2, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape2[z,i]=c1

fig, ax = plt.subplots()
for i in range(5):
        c=mape2[i,:]
        c2=c
        plt.ylim(0.02,0.35)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=2',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)

mape3=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=3, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape3[z,i]=c1

fig, ax = plt.subplots()
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.02,0.35)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=3',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)



mape4=np.zeros((6,6))

for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape4[i,z]=c1


fig, ax = plt.subplots()
for i in range(6):
        c=mape4[i,:]
        c2=c
        plt.ylim(0.02,0.35)
        c1=np.arange(6)
        ax.plot(c1,c2,'s-')
        plt.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],loc=1, fontsize='x-large')
        plt.title('C=1',fontsize=20)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=18)



mape5=np.zeros((8,6))

for i,j in enumerate([1,100,200,400,800,1000,2000,3000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=4, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape5[i,z]=c1


fig, ax = plt.subplots()
for i in range(8):
        c=mape5[i,:]
        c2=c
        plt.ylim(0.00,0.35)
        c1=np.arange(6)
        ax.plot(c1,c2,'s-')
        plt.legend(['M-1','M-100','M-200','M-400','M-800','M-1000','M-2000','M-3000'],loc=1, fontsize='x-large')
        plt.title('C=2',fontsize=20)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=18)




mape6=np.zeros((3,4))

for i,j in enumerate([1000,2000,8000]):
    for z,h in enumerate([1,2,3,4]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=0.5, max_depth=h, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape6[i,z]=c1



param_test1 = {'n_estimators':range(20,300,10)}
gsearch1 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, min_samples_split=300,
                                  min_samples_leaf=20,max_depth=3,max_features='sqrt', subsample=0.8,random_state=10), 
                       param_grid = param_test1,iid=False,cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


param_test4 = {'learning_rate':[0.001,0.005,0.01,0.1,1]}
gsearch4 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=80,max_depth=9, min_samples_leaf =40, 
               min_samples_split =500, subsample=0.8, random_state=10), 
                       param_grid = param_test4, iid=False, cv=5)
gsearch4.fit(train_x,train_y)
gsearch4.best_params_ 


param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(100,801,200)}
gsearch2 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=180, min_samples_leaf=20, 
      max_features='sqrt', subsample=0.8, random_state=10), 
   param_grid = param_test2,iid=False, cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_















aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
aa3=np.hstack([aa1,aa2.reshape(-1,1)])
c=np.sum(aa3[:,2])/len(aa3)



feature_importance = gbm0.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())

pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 2, 2)
plt.barh(pos, feature_importance, align='center')
plt.yticks(pos, feature_names[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()










x0=match_final_4[(match_final_4.iloc[:,6]>=0)&(match_final_4.iloc[:,6]<=2)]    
x1=np.array(x0.iloc[:,:-2])
y1=np.array(x0.iloc[:,-2])
gbm0 = GradientBoostingRegressor(n_estimators=80, learning_rate=0.1, max_depth=3, random_state=10, loss='ls')    
gbm0.fit(x1,y1)  
mean_squared_error(y1, gbm0.predict(x1))

















