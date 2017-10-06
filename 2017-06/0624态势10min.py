# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 10:15:19 2017

@author: wutongshu
"""

def inOut(upInsec,downInsec,upDire1,upClane1,upDire2,upClane2,downDire,downClane1,downClane2):
    upInsec.iloc[:,1]=pd.to_datetime(upInsec.iloc[:,1])
    downInsec.iloc[:,1]=pd.to_datetime(downInsec.iloc[:,1])
    upInsec['day']=upInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    upInsec['sj']=upInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    downInsec['day']=downInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    downInsec['sj']=downInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    q_total=[]
    for i in range(1204,1232):
        med_data=np.zeros((144,5))
        med_data[:,0]=range(144)
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
        for j in range(144):
            med_data[j,1]=len(in_q1Final[(in_q1Final.iloc[:,-2]>j*10*60)&(in_q1Final.iloc[:,-2]<(j+1)*10*60)])+len(in_q2Final[(in_q2Final.iloc[:,-2]>j*10*60)&(in_q2Final.iloc[:,-2]<(j+1)*10*60)])
            med_data[j,2]=len(out_q1Final[(out_q1Final.iloc[:,-2]>j*10*60)&(out_q1Final.iloc[:,-2]<(j+1)*10*60)])
            med=out_q1Final[(out_q1Final.iloc[:,-2]>j*10*60)&(out_q1Final.iloc[:,-2]<(j+1)*10*60)]
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
    time_5min=np.zeros((144,7))
    time_5min[:,0]=range(144)
    time_5min[:,4]=(day+2)%7
    for i in range(144):
        num=q[i,3]*K
        data_m=match_time1[(match_time1[:,1]>i*2*300)&(match_time1[:,1]<(i+1)*2*300)]
        if len(data_m)>num:
            time_5min[i,1]=np.mean(data_m[:,8])
            time_5min[i,3]=np.median(data_m[:,8])
#       样本数量较小，进行补全数据
        elif len(data_m)<=num:
#           当处于夜间低峰期时
            time_5min[i,1]=-1
            if i<=2*6*3 :
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
            if i>2*6*3:
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
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<12*3)]
#    取自由流速度
    data_full1=np.percentile(c.iloc[:,1],15)
    deal_15min_2=[]
    for z in range(len(dataDeal)):
        med_data=dataDeal[z]
        q1=q_total[i]
        med_deal=deal_5min(med_data,q1,day=i,data_full=data_full1,K=0.1,L=400)
        med_data1=np.array(med_deal)
        for j in range(144):
		#这里针对前3个周期都没有数据的情况，进行补全，考虑使用历史同星期，同时刻的均值进行补全；
            if med_data1[j,5]==1:
                d=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data1[j,4])]
                if len(d)>0:
                   med_data1[j,5]=np.mean(d.iloc[:,1])
                elif len(d)==0:
                   med_data1[j,5]= med_data1[j-1,5]
        deal_15min_2.append(med_data1)
    return deal_15min_2,data_full1