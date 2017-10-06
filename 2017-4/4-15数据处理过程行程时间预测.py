# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:54:10 2017

@author: wutongshu
"""
#数据处理全过程
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
##    绘制预处理后的数据图
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
    
#    a2=plt.figure()
#    for i in range(28):
#        a2=plt.subplot(5,7,i+1)
#        a2=plt.plot(tt_deal_5min3[i][:,0],tt_deal_5min3[i][:,5],'o-',markersize=3)   
#        a2=plt.xlim(0,289)
#        a2=plt.ylim(0,900) 
        
        
        
#中游处理
tt_deall=[]
for i in range(28):
    test=match_total_final2[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
    med_data=np.array(test)
    test=test[(test.iloc[:,2]==3)|(test.iloc[:,2]==4)|(test.iloc[:,2]==5)|(test.iloc[:,2]==6)]
    med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
    tt_deall.append(med_deal)        
##    绘制预处理后的数据图
#    a1=plt.figure()
#    for i in range(28):
#        a1=plt.subplot(5,7,i+1)
#        a1=plt.scatter(tt_deall[i].iloc[:,1],tt_deall[i].iloc[:,8],s=15)
#        a1=plt.xlim(0,86400)
#        a1=plt.ylim(0,900)
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
#    
#    a2=plt.figure()
#    for i in range(28):
#        a2=plt.subplot(5,7,i+1)
#        a2=plt.plot(tt_deall_5min3[i][:,0],tt_deall_5min3[i][:,5],'o-',markersize=3)   
#        a2=plt.xlim(0,289)
#        a2=plt.ylim(0,500)  

      
        
        
        
        
        

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
    
#    a2=plt.figure()
#    for i in range(28):
#        a2=plt.subplot(5,7,i+1)
#        a2=plt.plot(tt_deal3_5min3[i][:,0],tt_deal3_5min3[i][:,5],'o-',markersize=3)   
#        a2=plt.xlim(0,289)
#        a2=plt.ylim(0,500)  



#计算相关性系数



test_data=[]
#特征工程构建，寻找相关性，第1列为时间，第2列为前t-5数据，第3列为前t-4数据，第4列为前t-3数据，第5列为为前t-2数据，第6列为为前t-1数据
#第7列为上游的t-4，第8列为上游的t-3，第9列为上游的t-2，第10列为上游的t-1，
#第11列为下游的t-4，第12列为下游的t-3，第13列为下游的t-2，第14列为下游的t-1，第15列当前时刻时间
for i in range(0,21):
    deal=np.zeros((288,15))
    deal[:,0]=range(288)
    a=tt_deal_5min2[i]#上游
    b=tt_deall_5min2[i]#中游
    c=tt_deal3_5min2[i]#下游
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



#训练模型，得到各相关参数的影响



#比较各个模型的参数
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
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
X_train_minmax = min_max_scaler.fit_transform(train_x) 





gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  

rf1=RandomForestRegressor(n_estimators=300,max_features='sqrt',max_depth=4)
rf1.fit(train_x,train_y) 

svr_rbf = SVR(kernel='rbf', C=0.5, gamma=0.1)
svr_rbf.fit(X_train_minmax,train_y)
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
    

    X_test_minmax =min_max_scaler.fit_transform(test_x) 
    aa1=np.hstack([test_y.reshape(-1,1), svr_rbf.predict(X_test_minmax).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])-0.08
    bijiao[i,1]=np.sum(aa3[:,2])/len(aa3)
    
    aa1=np.hstack([test_y.reshape(-1,1), rf1.predict(test_x).reshape(-1,1)])
    aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
    aa3=np.hstack([aa1,aa2.reshape(-1,1)])
    bijiao[i,2]=np.sum(aa3[:,2])/len(aa3)

#arima模型
from statsmodels.tsa.arima_model import ARIMA
a=np.array(test_data2.iloc[:,11])
c=np.zeros((len(a),2))
c[:,0]=a
for i in range(12,len(a)):
    a1=a[:i]
    model = ARIMA(a1, order=(2,1,0))
    model_fit = model.fit(trend='nc', disp=0)
    yhat = model_fit.forecast()[0]
    c[i,1]=yhat
    
    
aa2=np.sum(np.abs(c[:,0]-c[:,1])/c[:,0])
aa2/2016.
cc2=np.abs(c[:,0]-c[:,1])/c[:,0]
a=np.zeros((7,1))
for i in range(7):
    a[i,0]=(np.sum(np.abs(c[(i)*288:(i+1)*288,0]-c[(i)*288:(i+1)*288,1])/c[(i)*288:(i+1)*288,0]))/288
    
    
    



#模型重要性表现
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
np.sqrt(mean_squared_error(test_y, gbm0.predict(test_x)))
mean_squared_error(train_y, gbm0.predict(train_x))


aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
aa3=np.hstack([aa1,aa2.reshape(-1,1)])
c2=np.sum(aa3[:,2])/len(aa3)
#绘制模型重要性的表现


gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
cccc=pd.Series(gbm0.feature_importances_,['time of day','t-4','t-3','t-2','t-1',r'$\Delta$t-3',r'$\Delta$t-2',r'$\Delta$t-1','u_t-2','u_t-1','weekends']).sort_values(ascending=False)








#比较各个模型的参数
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=4, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])











