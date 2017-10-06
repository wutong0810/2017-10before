# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 21:21:50 2017

@author: Administrator
"""

train_data=[]
for i in range(0,21):
    deal=np.zeros((96,19))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV2
            deal[j,10]=freeV2
            deal[j,11]=freeV2
            deal[j,12]=freeV4
            deal[j,13]=freeV4
            deal[j,14]=freeV4
            deal[j,15]=0
            deal[j,16]=0
            deal[j,17]=0
            deal[j,18]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link2[j-3,5]
            deal[j,10]=link2[j-2,5]
            deal[j,11]=link2[j-1,5]
            deal[j,12]=link4[j-3,5]
            deal[j,13]=link4[j-2,5]
            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j-3,5]-link3[j-4,5]
            deal[j,16]=link3[j-2,5]-link3[j-3,5]
            deal[j,17]=link3[j-1,5]-link3[j-2,5]
            deal[j,18]=link3[j,5]
    train_data.append(deal)    
    
    
train_data1=[]
for i in range(21):
    a=pd.DataFrame(train_data[i])
    train_data1.append(a)
train_data2 = pd.concat(train_data1, ignore_index=True)     
    
    

    
    
valid_data=[]
for i in range(21,25):
    deal=np.zeros((96,19))
    deal[:,0]=range(96)
    link1=data_15min1[i]
    link2=data_15min2[i]
    link3=data_15min3[i]
    link4=data_15min4[i]
    deal[:,1]=(i+2)%7
    for j in range(96):
        if j<4:
            deal[j,2]=freeV3
            deal[j,3]=freeV3
            deal[j,4]=freeV3
            deal[j,5]=freeV3
            deal[j,6]=freeV1
            deal[j,7]=freeV1
            deal[j,8]=freeV1
            deal[j,9]=freeV2
            deal[j,10]=freeV2
            deal[j,11]=freeV2
            deal[j,12]=freeV4
            deal[j,13]=freeV4
            deal[j,14]=freeV4
            deal[j,15]=0
            deal[j,16]=0
            deal[j,17]=0
            deal[j,18]=link3[j,5]
        else :
            deal[j,2]=link3[j-4,5]
            deal[j,3]=link3[j-3,5]
            deal[j,4]=link3[j-2,5]
            deal[j,5]=link3[j-1,5]
            deal[j,6]=link1[j-3,5]
            deal[j,7]=link1[j-2,5]
            deal[j,8]=link1[j-1,5]
            deal[j,9]=link2[j-3,5]
            deal[j,10]=link2[j-2,5]
            deal[j,11]=link2[j-1,5]
            deal[j,12]=link4[j-3,5]
            deal[j,13]=link4[j-2,5]
            deal[j,14]=link4[j-1,5]
            deal[j,15]=link3[j-3,5]-link3[j-4,5]
            deal[j,16]=link3[j-2,5]-link3[j-3,5]
            deal[j,17]=link3[j-1,5]-link3[j-2,5]
            deal[j,18]=link3[j,5]
    valid_data.append(deal)   
    
    

valid_data1=[]
for i in range(len(valid_data)):
    a=pd.DataFrame(valid_data[i])
    valid_data1.append(a)
valid_data2 = pd.concat(valid_data1, ignore_index=True)  

gbm0 = RandomForestRegressor(n_estimators=180, min_samples_split=10,\
                                      min_samples_leaf=20,max_depth=11,max_features='sqrt',random_state=0)  
import copy
Mape1=np.zeros((1,18))
Vector=[]
minMape=1
index=0
total=range(18)
for i in range(17):
    minMape=1
    for j in total:
        total1=copy.deepcopy(total)
        total1.remove(j)
        train_x1=np.array(train_data2.iloc[:,:-1])
        train_y=np.array(train_data2.iloc[:,-1])
        train_x=train_x1[:,total1]
        test_x1=np.array(valid_data2.iloc[:,:-1])
        test_x=test_x1[:,total1]
        test_y=np.array(valid_data2.iloc[:,-1])
        gbm0.fit(train_x,train_y)
        aa1=np.hstack([test_y.reshape(-1,1), gbm0.predict(test_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
#        print c1
        if c1<minMape:
#            mapechange=True
            minMape=c1
            index=j
    Mape1[0,i]=minMape
#    if mape
    total.remove(index) 
    total2=copy.deepcopy(total)
    Vector.append(total2)




















  
    
    
    
    
    
    
    