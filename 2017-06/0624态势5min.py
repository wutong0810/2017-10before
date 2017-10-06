# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:27:54 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
def inOut(upInsec,downInsec,upDire1,upClane1,upDire2,upClane2,downDire,downClane1,downClane2):
    upInsec.iloc[:,1]=pd.to_datetime(upInsec.iloc[:,1])
    downInsec.iloc[:,1]=pd.to_datetime(downInsec.iloc[:,1])
    upInsec['day']=upInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    upInsec['sj']=upInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    downInsec['day']=downInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    downInsec['sj']=downInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    q_total=[]
    for i in range(1204,1232):
        med_data=np.zeros((288,5))
        med_data[:,0]=range(288)
    #   取出每天的驶入量
        in_q=upInsec[upInsec.iloc[:,5]==i]
        in_q['repair']=0
#        进口道1
        cache_total1=[]
        cache1=in_q[in_q.iloc[:,3]==upDire1]
        for g in upClane1:
            in_Q=cache1[cache1.iloc[:,2]==g]
            cache_total1.append(in_Q)
        in_q1=pd.concat(cache_total1, ignore_index=True) 
#        进口道2       
        cache_total2=[]
        cache1=in_q[in_q.iloc[:,3]==upDire2]
        for g in upClane2:
            in_Q=cache1[cache1.iloc[:,2]==g]
            cache_total2.append(in_Q)
        in_q2=pd.concat(cache_total2, ignore_index=True) 
#       排序,按车道再按时间
        in_q1=in_q1.sort_values(by=[in_q1.columns[2],in_q1.columns[6]])
        in_q2=in_q2.sort_values(by=[in_q2.columns[2],in_q2.columns[6]])
        in_q1Final= removeFun(in_q1) 
        in_q2Final= removeFun(in_q2)
#        驶出车道流量
        out_q=downInsec[downInsec.iloc[:,5]==i]
        out_q['repair']=0
        
        cache_total3=[]
        cache1=out_q[out_q.iloc[:,3]==downDire]
        for g in downClane1:
            in_Q=cache1[cache1.iloc[:,2]==g]
            cache_total3.append(in_Q)
        out_q1=pd.concat(cache_total3, ignore_index=True)
		#按照车道、时间排序
        out_q1=out_q1.sort_values(by=[out_q1.columns[2],out_q1.columns[6]])
		#剔除掉重复匹配的车辆，防止一辆车被多次检测到
        out_q1Final=removeFun(out_q1)
        for j in range(288):
            med_data[j,1]=len(in_q1Final[(in_q1Final.iloc[:,-2]>j*5*60)&(in_q1Final.iloc[:,-2]<(j+1)*5*60)])+len(in_q2Final[(in_q2Final.iloc[:,-2]>j*5*60)&(in_q2Final.iloc[:,-2]<(j+1)*5*60)])
            med_data[j,2]=len(out_q1Final[(out_q1Final.iloc[:,-2]>j*5*60)&(out_q1Final.iloc[:,-2]<(j+1)*5*60)])
            med=out_q1Final[(out_q1Final.iloc[:,-2]>j*5*60)&(out_q1Final.iloc[:,-2]<(j+1)*5*60)]
            med_final1=[]
            for y in downClane2:
                cach=med[(med.iloc[:,2]==y)]
                med_final1.append(cach)
            medFinal=pd.concat(med_final1, ignore_index=True)
            med_data[j,3]=len(medFinal)
        q_total.append(med_data)    
    return q_total





def deal_5min(match_time,q,day=0,data_full=60,K=0.1,L=400):
#   定义拥堵速度为5km/h
    Vb=5
    match_time1=np.array(match_time)
    time_5min=np.zeros((288,7))
    time_5min[:,0]=range(288)
    time_5min[:,4]=(day+2)%7
    for i in range(288):
        num=q[i,3]*K
        data_m=match_time1[(match_time1[:,1]>i*1*300)&(match_time1[:,1]<(i+1)*1*300)]
        if len(data_m)>num:
            time_5min[i,1]=np.mean(data_m[:,8])
            time_5min[i,3]=np.median(data_m[:,8])
#       样本数量较小，进行补全数据
        elif len(data_m)<=num:
#           当处于夜间低峰期时
            time_5min[i,1]=-1
            if i<=4*6*3 :
#               i从第2个开始
                if i>=1:
#               判断前1个周期是否存在数据
                    if np.sum(time_5min[i-1,1])>0:
#                        判断前一个状态是否处于拥堵状态
                        if  time_5min[i-1,1]>float(L/Vb*3.6):
                            time_5min[i,2]=time_5min[i-1,1]
                        else :
                            time_5min[i,2]=data_full
                    elif np.sum(time_5min[i-1,1])<0 :
#                       前一个时，用信号控制下的自由流行程时间补全
                        time_5min[i,2]=data_full
#                初始时给第一个时刻如果没有数据，给数据赋自有流的行程时间
                elif i==0 :
                        time_5min[i,2]=data_full
#           当非低峰期时六点以后，使用前3个周期的数据的特征值进行补全
            if i>4*6*3:
#               判断前N=3个周期是否存在数据
                if np.sum(time_5min[i-3:i,1])>0:
#                   判断前一个周期是否有数据
                    if np.sum(time_5min[i-1,1])>0:
#                        判断是否处于拥堵状态
                        if  time_5min[i-1,1]>float(L/Vb*3.6):
                            time_5min[i,2]=time_5min[i-1,1]
                        else :
                            a=time_5min[i-3:i,1]
                            b=a[a>0]
                            c=np.mean(b)
                            time_5min[i,2]=c
                    else :
#                        前一个周期没有数据，则使用前3个区间的均值补全
                            a=time_5min[i-3:i,1]
                            b=a[a>0]
                            c=np.mean(b)
                            time_5min[i,2]=c
                else :
#                   当前3个周期没有数据时，用历史同期（同周日同时刻）的数据补全，这里还没有补全，在循环处理时，会用历史数据补全
                    time_5min[i,2]=1
        if time_5min[i,1]>0:
            time_5min[i,5]=time_5min[i,1]
        if time_5min[i,2]>0:
#           第6列为补全数据，第7列为是否为补全标识
            time_5min[i,5]=time_5min[i,2]
            time_5min[i,6]=1
    return time_5min    



def loop_15min(dataDeal,q_total):
    deal_15min_1=[]
    for i in range(len(dataDeal)):
        med_data=dataDeal[i]
        q1=q_total[i]
        med_deal=deal_5min(med_data,q1,day=i,data_full=-1,K=0.1,L=400)
        med_deal2=pd.DataFrame(med_deal)
        deal_15min_1.append(med_deal2)
    match_final_1 = pd.concat(deal_15min_1, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<24*3)]
#    取自由流速度
    data_full1=np.percentile(c.iloc[:,1],15)
    deal_15min_2=[]
    for z in range(len(dataDeal)):
        med_data=dataDeal[z]
        q1=q_total[i]
        med_deal=deal_5min(med_data,q1,day=i,data_full=data_full1,K=0.1,L=400)
        med_data1=np.array(med_deal)
        for j in range(288):
		#这里针对前3个周期都没有数据的情况，进行补全，考虑使用历史同星期，同时刻的均值进行补全；
            if med_data1[j,5]==1:
                d=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data1[j,4])]
                if len(d)>0:
                   med_data1[j,5]=np.mean(d.iloc[:,1])
                elif len(d)==0:
                   med_data1[j,5]= med_data1[j-1,5]
        deal_15min_2.append(med_data1)
    return deal_15min_2,data_full1

#剔除掉重复匹配的车辆，防止一辆车被多次检测到函数
def removeFun(data):
    data1=np.array(data)
    dataFinal=[]
    for i in data.iloc[:,2].unique():
            data2=data1[data1[:,2]==i]
            indice=[]
            for j in range(1,len(data2)):
                if (cmp(data2[j,0],data2[j-1,0])==0)& (data2[j,6]-data2[j-1,6]<100&len(data2[j,0])>5):
                    indice.append(j-1)
        #给行程时间付上-1来标示行程时间
            for h in indice:
                data2[h,7]=-1
            dataFinal.append(pd.DataFrame(data2[data2[:,7]>-1]))
            dataFinal1=pd.concat(dataFinal, ignore_index=True) 
    return dataFinal1


q_total1=inOut(upInsec=rj_xh,downInsec=rj_xg,upDire1=1,upClane1=[2,3,4],upDire2=3,upClane2=[1,2],downDire=1,downClane1=[1,2,3,4],downClane2=[2,3,4])
q_total2=inOut(upInsec=rj_xg,downInsec=rj_zy,upDire1=1,upClane1=[2,3,4],upDire2=3,upClane2=[1,2],downDire=1,downClane1=[1,2,3,4,5,6],downClane2=[3,4,5,6])
q_total3=inOut(upInsec=rj_zy,downInsec=rj_xy,upDire1=1,upClane1=[3,4,5,6],upDire2=3,upClane2=[1,2],downDire=4,downClane1=[1,2,3],downClane2=[1,2,3])



data_15min1,freeV1=loop_15min(dataDeal1,q_total1)


data_15min2,freeV2=loop_15min(dataDeal2,q_total2)


data_15min3,freeV3=loop_15min(dataDeal3,q_total3)



import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
#mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(22,11))
plt.subplots_adjust(left=0.12, bottom=0.05, top=0.95,right=0.92,hspace=0.24,wspace=0.24) 
for i in range(28):
    a1=plt.subplot(5,7,i+1)
    a1=plt.plot(data_15min2[i][:,0],data_15min2[i][:,5])
    a1=plt.xlim(0,288)
    a1=plt.ylim(0,900)





import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
#sys.path.append(r'F:\python_script\2017-5\predict')
#from all_func import *
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation, metrics
from sklearn.ensemble import RandomForestRegressor

#数据集主要包括其1.每天所处的时刻，2.星期，3.历史前3个的行程时间，4.历史前2个的行程时间，5.历史前1个的行程时间
#6.上游路段1的前1个的行程时间，
#7.历史前3个时间窗至前2个时间窗的行程时间变化量；
#8.历史前2个时间窗至前1个时间窗的行程时间变化量；
#9.历史前2个时间窗的驶入量
#10.历史前1个时间窗的驶入量
#11.历史前2个时间窗的驶出量
#12.历史前1个时间窗的驶出量
#13.对应的行程时间


train_data=[]
for i in range(0,21):
    deal=np.zeros((288,13))
    deal[:,0]=range(288)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    q=q_total2[i]
    deal[:,1]=(i+2)%7
    for j in range(288):
        if j<4:
            deal[j,2]=freeV2
            deal[j,3]=freeV2
            deal[j,4]=freeV2
            deal[j,5]=freeV1
            deal[j,6]=0
            deal[j,7]=0
            if j<=1:
                deal[j,8]=0
                deal[j,9]=0
                deal[j,10]=0
                deal[j,11]=0
            else :
                deal[j,8]=q[j-2,2]
                deal[j,9]=q[j-1,2]
                deal[j,10]=q[j-2,3]
                deal[j,11]=q[j-1,3]
            deal[j,12]=link2[j,5]
        else :
            deal[j,2]=link2[j-3,5]
            deal[j,3]=link2[j-2,5]
            deal[j,4]=link2[j-1,5]
            deal[j,5]=link1[j-1,5]
            deal[j,6]=link2[j-2,5]-link2[j-3,5]
            deal[j,7]=link2[j-1,5]-link2[j-2,5]
            deal[j,8]=q[j-2,2]
            deal[j,9]=q[j-1,2]
            deal[j,10]=q[j-2,3]
            deal[j,11]=q[j-2,3]
            deal[j,12]=link2[j,5]
    train_data.append(deal)


train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)

train_data2 = pd.concat(train_data1, ignore_index=True) 




#获得测试集  
test_data=[]
for i in range(21,28):
    deal=np.zeros((288,13))
    deal[:,0]=range(288)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    q=q_total2[i]
    deal[:,1]=(i+2)%7
    for j in range(288):
        if j<4:
            deal[j,2]=freeV2
            deal[j,3]=freeV2
            deal[j,4]=freeV2
            deal[j,5]=freeV1
            deal[j,6]=0
            deal[j,7]=0
            if j<=1:
                deal[j,8]=0
                deal[j,9]=0
                deal[j,10]=0
                deal[j,11]=0
            else :
                deal[j,8]=q[j-2,2]
                deal[j,9]=q[j-1,2]
                deal[j,10]=q[j-2,3]
                deal[j,11]=q[j-1,3]
            deal[j,12]=link2[j,5]
        else :
            deal[j,2]=link2[j-3,5]
            deal[j,3]=link2[j-2,5]
            deal[j,4]=link2[j-1,5]
            deal[j,5]=link1[j-1,5]
            deal[j,6]=link2[j-2,5]-link2[j-3,5]
            deal[j,7]=link2[j-1,5]-link2[j-2,5]
            deal[j,8]=q[j-2,2]
            deal[j,9]=q[j-1,2]
            deal[j,10]=q[j-2,3]
            deal[j,11]=q[j-2,3]
            deal[j,12]=link2[j,5]
    test_data.append(deal) 


test_data1=[]
for i in range(7):
    a=pd.DataFrame(test_data[i])
    test_data1.append(a)
test_data2 = pd.concat(test_data1, ignore_index=True)   





train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])

param_test1 = {'n_estimators':range(20,300,10)}
gsearch1 = GridSearchCV(estimator =RandomForestRegressor( min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=4,max_features='sqrt',random_state=10) , 
                       param_grid = param_test1,iid=False,scoring='neg_mean_squared_error',cv=5)
gsearch1.fit(train_x,train_y)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


#得到最优的树的棵树为130







param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(50,120,20)}
gsearch2 =  GridSearchCV(estimator =RandomForestRegressor( n_estimators= 210\
                                      ,min_samples_leaf=20,max_features='sqrt',random_state=10) , 
                       param_grid = param_test2,iid=False,scoring='neg_mean_squared_error',cv=5)
gsearch2.fit(train_x,train_y)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_

# 最优参数{'max_depth':11, 'min_samples_split': 50},


train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])









#分别计算MAPE
mape=np.zeros((1,7))
rmse=np.zeros((1,7))
gbm0 = RandomForestRegressor(n_estimators=130, min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=11,max_features='sqrt',random_state=0)  
gbm0.fit(train_x,train_y)
for i in range(7):
    test_x=np.array(test_data2.iloc[288*i:288*(i+1),:-1])
    test_y=np.array(test_data2.iloc[288*i:288*(i+1),-1])
    aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    aa4=(aa1[:,0]-aa1[:,1])**2
    c1=np.sum(aa3[:,2])/len(aa3)
#    print aa4
    mape[0,i]=c1
    rmse[0,i]=np.sqrt(np.sum(aa4)/len(aa3))















fig, ax = plt.subplots(2,4,figsize=(18,10))
for i in range(7):
    plt.subplot(2,4,i+1)
    plt.plot(np.linspace(0,24,288),state.iloc[i*288:(i+1)*288,0],'o-',markersize=3,label='true') 
    plt.plot(np.linspace(0,24,288),state.iloc[i*288:(i+1)*288,1],'o-',markersize=3,label='predict')
    plt.legend()
    plt.ylim(0,700)































