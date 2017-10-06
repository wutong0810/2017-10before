# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:51:01 2017

@author: wutongshu
"""
#参数调整
import numpy as np
train_data3=np.array(train_data2)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
train_x=np.array(train_data2.iloc[:,:-1])
train_y=np.array(train_data2.iloc[:,-1])
X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3, random_state=0)


#c=1时
mape1=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape1[z,i]=c1

fig, ax = plt.subplots()
for i in range(5):
        c=mape1[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=1',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)

#c=2时
mape2=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=2, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape2[z,i]=c1

fig, ax = plt.subplots()
for i in range(5):
        c=mape2[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=2',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)
        
        
#c=3时
mape3=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=3, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape3[z,i]=c1

fig, ax = plt.subplots()
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=3',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)        
        

        
fig, ax = plt.subplots(3,1,1)
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        plt.title('max_depth C=3',fontsize=20)
        ax.set_xlabel('Number of Trees(M)',fontsize=20)             
        
fig, axes = plt.subplots(3,1, figsize=(12,12))  
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        axes[2].plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
        axes[2].set_title('max_depth C=3',fontsize=20)
        axes[2].set_xlabel('Number of Trees(M)',fontsize=20)          
        
for i in range(5):
        c=mape2[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        axes[1].plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
#        plt.title('max_depth C=2',fontsize=20)
        axes[1].set_title('max_depth C=2',fontsize=20)

        axes[1].set_xlabel('Number of Trees(M)',fontsize=20)         
        
for i in range(5):
        c=mape1[i,:]
        c2=c
        plt.ylim(0.05,0.3)
        axes[0].plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,'s-')
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize='x-large')
#        plt.title('max_depth C=1',fontsize=20)
        axes[0].set_title('max_depth C=3',fontsize=20)
        axes[0].set_xlabel('Number of Trees(M)',fontsize=20)           
        
        
        
        
        
        
        
        
        
#c=1，调整学习率
mape4=np.zeros((6,6))

for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=2, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape4[i,z]=c1        
        
fig, ax = plt.subplots()
for i in range(6):
        c=mape4[i,:]
        c2=c
        plt.ylim(0.1,0.35)
        c1=np.arange(6)
        ax.plot(c1,c2,'s-')
        plt.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],loc=1, fontsize='x-large')
        plt.title('C=1',fontsize=20)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=18)       
        
        
        
        
#c=3，调整学习率
mape5=np.zeros((6,6))

for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=3, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape5[i,z]=c1        
        
fig, ax = plt.subplots()
for i in range(6):
        c=mape4[i,:]
        c2=c
        plt.ylim(0.1,0.30)
        c1=np.arange(6)
        ax.plot(c1,c2,'s-')
        plt.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],loc=1, fontsize='x-large')
        plt.title('max_depth C=3',fontsize=20)
        ax.set_xlabel('learning rate',fontsize=20)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=18)          
        
        
mape6=np.zeros((3,4))

for i,j in enumerate([1000,2000,8000]):
    for z,h in enumerate([1,2,3,4]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=0.5, max_depth=h, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape6[i,z]=c1        









        
fig, ax = plt.subplots()



a2=plt.figure()
for i in range(28):
    a2=plt.subplot(5,7,i+1)
    a2=plt.plot(tt_deall_5min3[i][:,0],tt_deall_5min3[i][:,5],'o-',markersize=3)   
    a2=plt.xlim(0,289)
    a2=plt.ylim(0,500) 






for i in range(3):
        c=mape6[i,:]
        c2=c
#        plt.ylim(0.02,0.35)
        c1=np.arange(4)
        ax.plot(c1,c2,'s-')
        plt.legend(['M-1000','M-2000','M-8000'],loc=1, fontsize='x-large')
        plt.title('C=3',fontsize=20)
        ax.set_xticks(range(4))
        ax.set_xticklabels([1,2,3,4], fontsize=18)           
        
        
        
        
        
        
        
        
        
        
        