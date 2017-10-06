# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:11:34 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

def openfile(inpath1 = r"C:\Users\wutongshu\Desktop\贵阳数据\zh_zy1201-1215.csv", inpath2 = r"C:\Users\wutongshu\Desktop\贵阳数据\rj_zy1201-1215.csv"):
    uipath1 = unicode(inpath1 , "utf8")
    uipath2 = unicode(inpath2 , "utf8")
    down_data=pd.read_csv(uipath1,encoding='gbk')
    up_data=pd.read_csv(uipath2,encoding='gbk')
    down_data.iloc[:,1]=pd.to_datetime(down_data.iloc[:,1])
    up_data.iloc[:,1]=pd.to_datetime(up_data.iloc[:,1])
    down_data['day']=down_data.iloc[:,1].apply(lambda x:100*x.month+x.day)
    up_data['day']=up_data.iloc[:,1].apply(lambda x:100*x.month+x.day)
    down_data['sj']=down_data.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    up_data['sj']=up_data.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    day_num=down_data.day.unique()
    return down_data,up_data,day_num





#2.匹配行程时间函数
#原始数据第1列车牌，第2列过车时刻，第3列车道，第4列为进口道方向，第5列为车型；

#行程时间匹配函数，以下为参数说明
#up_data上游数据，down_data下游数据，down_direction下游进口道的方向，
#maxtime最大匹配行程时间，mintime最小匹配行程时间
#匹配函数
def match_traveltime(up_data,down_data,maxtime,mintime,down_direction):
    down_data=down_data[down_data.ix[:,3]==down_direction]
    down_data.index=range(len(down_data))
#筛选正常数据，异常数据主要为未识别和无牌，因此数据位数都不为7
    down_data['car_length']=down_data.iloc[:,0].apply(lambda x:len(x))
    down_true=down_data[down_data.iloc[:,5]==7]
    down_true.index=range(len(down_true))
#计算下游识别率
    plate_identify_rate1=float(len(down_true))/len(down_data)
#同理筛选上游正常数据，异常数据主要为未识别和无牌，因此数据位数都不为7
    up_data['car_length']=up_data.iloc[:,0].apply(lambda x:len(x))
    up_true=up_data[up_data.iloc[:,5]==7]
    up_true.index=range(len(up_true))
#计算上游识别率
    plate_identify_rate2=float(len(up_true))/len(up_data)
#初始化最终的大矩阵match_du，上游的车牌先进行排序
    down_true1=np.array(down_true)
    down_true['up_t']=np.nan
    down_true['up_clane']=np.nan
    down_true['up_direct']=np.nan
    down_true['tt']=0
    match_du=np.array(down_true)
    up_true=up_true.sort_values(by=up_true.columns[1])
    up_true1=np.array(up_true)
#    搜索上游在合理时间范围内的车牌数据
    for i in range(len(down_true)):
        t_min=down_true1[i,1]-maxtime
        t_max=down_true1[i,1]-mintime
        up_medium=up_true1[(up_true1[:,1]>t_min)&(up_true1[:,1]<t_max)]
        m=len(up_medium)
#       如果存在，则匹配车牌信息，并计算行程时间，一旦匹配上则跳出循环
        if m>0:           
            for j in range(m):
                if (cmp(match_du[i,0],up_medium[j,0])==0):
                    match_du[i,6]=up_medium[j,1]
                    match_du[i,7]=up_medium[j,2]
                    match_du[i,8]=up_medium[j,3]
                    match_du[i,9]=match_du[i,1]-up_medium[j,1]
                    break
#    将匹配好的大矩阵按车牌，和下游过程时刻排序，去掉重复匹配的车牌
    match_time=pd.DataFrame(match_du)
    match_time=match_time.sort_values(by=[0,1])
    match_time.index=range(len(match_time))
    match_time1=np.array(match_time)
    indice=[]
#阈值设置为100s
    for h in range(2,len(match_time1)):
        if (cmp(match_time1[h,0],match_time1[h-1,0])==0)& (match_time1[h,1]-match_time1[h-1,1]<100):
            indice.append(h-1)
#给行程时间付上-1来标示行程时间
    for i in indice:
        match_time1[i,9]=-1
#筛选出正常的数据
    match_time2=match_time1[match_time1[:,9]>-1]
    match_tt=pd.DataFrame(match_time2)
#重新按下游过车时刻来排序
    match_tt=match_tt.sort_values(by=[1,0])
#修改索引
    match_tt.index=range(len(match_tt))
#    计算下匹配率
    match_final=match_tt[match_tt.iloc[:,9]>0]
    match_final.columns=['car_num','d_time','d_clane','d_direction','car_type','num_length','u_time','u_clane','u_direction','tt']
#   删掉车牌长度
    match_rate=float(len(match_final))/len(match_du)
    return match_tt,match_final,match_rate



#3.行程时间预处理函数
#根据箱型图原理处理原始数据,滚动时间窗。
#match是车牌匹配后的行程时间矩阵（array），含9列，1列车牌信息，2列为下游过车时刻，3列下游车道编号，4列下游行驶方向，5列车型，6列上游过车时刻，7列上游车道编号，8列上游进口方向，9列行程时间
#cd为周期划分方案
#tet,处理间隔
#tet1,低峰期每tet处理一次，每次提取tet1时长的时距tet1
#tet2,非低峰期每tet处理一次，每次提取tet2时长的时距tet1
#num，样本数阈值
#cs,时间窗中IQR的系数，默认1.5
#td,替代分位值，采用上一时间窗的td 100-td分位值进行替代
#lc，采用标准差变化率时，本时间窗标准差与上一时间窗标准差的正常变化范围参数，默认1.8
#plot10,是否画图，是为1，否为0
#match_pre,预处理后的行程时间矩阵，含7列，1列上游过车时刻，2列上游车道编号，3列上游进口方向，4列下游过车时刻，5列下游车道编号，6列下游进口方向，7列行程时间
#ap_et，预处理评价矩阵，1、2为时间窗，3列上边界，4列下边界，5列一次处理后的标准差    
#    tet为处理步长，tet默认为60s，即每60s来一个数据，
def data_deal(match_du,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8):
    cd=np.array([[0,25200,77,23],[25200,32400,100,24],[32400,59400,110,25],[59400,72000,100,24],[72000,86400,77,23]])
    match_final_1=[]
    match_twp_time=[]
#    处理步数
    step=(24*3600/tet)
    ap_et=np.zeros(((24*3600/tet),6))
    for i in range(step):
        if (i*tet<3600*7)|(i*tet>=3600*19.5):
            ap_et[i,0]=i*tet-tet1
            ap_et[i,1]=i*tet
        else:
            ap_et[i,0]=i*tet-tet2
            ap_et[i,1]=i*tet
        if ap_et[i,0]<0:
            ap_et[i,0]=0
        gc1=cd[(ap_et[i,0]>=cd[:,0])&(ap_et[i,0]<cd[:,1])][:,3]
        gc2=cd[(ap_et[i,1]>=cd[:,0])&(ap_et[i,1]<cd[:,1])][:,3]
        gc=max(gc1,gc2)
        cc1=cd[(ap_et[i,0]>=cd[:,0])&(ap_et[i,0]<cd[:,1])][:,2]
        cc2=cd[(ap_et[i,1]>=cd[:,0])&(ap_et[i,1]<cd[:,1])][:,2]
        cc=max(cc1,cc2)
        match_tw_time=match_du[(match_du[:,1]>=ap_et[i,0])&(match_du[:,1]<ap_et[i,1])]
        if (len(match_tw_time)==0):
            continue
        else:
            if (len(match_tw_time)<=num):
                if len(match_twp_time)>0:
                    match_tw_time1=match_tw_time[(match_tw_time[:,8]<(np.percentile(match_twp_time[:,8],td)+cc))&(match_tw_time[:,8]>=(np.percentile(match_twp_time[:,8],100-td)-cc))]
                else: 
#                    上限
                    ap_et[i,2]=1.5*(np.percentile(match_tw_time[:,8],75)-np.percentile(match_tw_time[:,8],25))+np.percentile(match_tw_time[:,8],75)
#                    下限
                    ap_et[i,3]=-1.5*(np.percentile(match_tw_time[:,8],75)-np.percentile(match_tw_time[:,8],25))+np.percentile(match_tw_time[:,8],25)
                    match_tw_time1=match_tw_time[(match_tw_time[:,8]>=ap_et[i,3])&(match_tw_time[:,8]<=ap_et[i,2])]
            else:
#                上限
                ap_et[i,2]=1.5*(np.percentile(match_tw_time[:,8],75)-np.percentile(match_tw_time[:,8],25))+np.percentile(match_tw_time[:,8],75)
#                下限
                ap_et[i,3]=-1.5*(np.percentile(match_tw_time[:,8],75)-np.percentile(match_tw_time[:,8],25))+np.percentile(match_tw_time[:,8],25)
                match_tw_time1=match_tw_time[(match_tw_time[:,8]>=ap_et[i,3])&(match_tw_time[:,8]<=ap_et[i,2])]
                ap_et[i,4]=np.std(match_tw_time1[:,8])
                if ap_et[i,4]<(gc/2.+10):
    #                上限
                    ap_et[i,2]=(np.percentile(match_tw_time[:,8],25))+cc
    #                下限
                    ap_et[i,3]=(np.percentile(match_tw_time[:,8],25))-cc
                    match_tw_time1=match_tw_time[(match_tw_time[:,8]>=ap_et[i,3])&(match_tw_time[:,8]<=ap_et[i,2])]
                else:
                    if len(match_twp_time)>0:
                        if ap_et[i-1,5]<=gc/2.+10:
                            bzgu=gc/2.+10
                        else:
                            bzgu=ap_et[i-1,5]
                        if ap_et[i,4]>lc*bzgu:
                            match_tw_time1=match_tw_time[(match_tw_time[:,8]<(np.percentile(match_twp_time[:,8],td)+cc))&(match_tw_time[:,8]>=(np.percentile(match_twp_time[:,8],100-td)-cc))]
            match_twp_time=match_tw_time1
            ap_et[i,5]=np.std(match_tw_time1[:,8])
        if len(match_tw_time1)>0:
            match_tw_time1=match_tw_time1[(match_tw_time1[:,1]>=((i-1)*tet)) & (match_tw_time1[:,1]<(i*tet))]
#            一分钟时间窗内有数据，就保存这一分钟数据
            if len(match_tw_time1)>0:
                match_tw_time1=pd.DataFrame(match_tw_time1)
                match_final_1.append(match_tw_time1)
    match_final1 = pd.concat(match_final_1, ignore_index=True)
    return match_final1

#4.处理成五分钟数据函数  ,输入原始数据为第一行为下游时刻，第二行为行程时间  
#车牌匹配后的行程时间DataFrame，含9列，1列车牌信息，2列为下游过车时刻，3列下游车道编号，4列下游行驶方向，5列车型，6列上游过车时刻，7列上游车道编号，8列上游进口方向，9列行程时间
#num是行程时间置信数量，就是当匹配到的车辆数少于一定时，考虑如何对数据进行修正
#输出数据，第1列时间，第2列5分钟均值，第3列为是否为补全数据，第4列中位数，第5列周几，第6列为最后数据，第7列为是否为补全数据


def deal_5min(match_time,num=3,length=575,day=0):
    match_time1=np.array(match_time)
    time_5min=np.zeros((288,7))
    time_5min[:,0]=range(288)
    time_5min[:,4]=(day+2)%7
    for i in range(288):
        data_m=match_time1[(match_time1[:,1]>i*300)&(match_time1[:,1]<(i+1)*300)]
        if len(data_m)>num:
            time_5min[i,1]=np.mean(data_m[:,8])
            time_5min[i,3]=np.median(data_m[:,8])
#       样本数量较小，进行补全数据
        elif len(data_m)<=num:
#           当处于夜间低峰期时
            time_5min[i,1]=-1
            if i<=12*7 :
#               i大于3开始
                if i>=3:
#               判断前N=3个周期是否存在数据
                    if np.sum(time_5min[i-3:i,1])>0:
                        a=time_5min[i-3:i,1]
                        b=a[a>0]
                        c=np.mean(b)
                        time_5min[i,2]=c
                    else :
#                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
                        time_5min[i,2]=90
#                i小于3时，
                elif (i>0)&(i<3) :
                    if np.sum(time_5min[0:i,1])>0:
                        a=time_5min[0:i,1]
                        b=a[a>0]
                        c=np.mean(b)
                        time_5min[i,2]=c
                    else :
#                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
                        time_5min[i,2]=90
                elif i==0 :
                    if np.sum(time_5min[0,1])>0:
                        a=time_5min[0,1]
                        b=a[a>0]
                        c=np.mean(b)
                        time_5min[i,2]=c
                    else :
#                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
                        time_5min[i,2]=90
#           当非低峰期时，使用前3个周期的数据的特征值进行补全
            if i>12*7:
#               判断前N=3个周期是否存在数据
                if np.sum(time_5min[i-3:i,1])>0:
                    a=time_5min[i-3:i,1]
                    b=a[a>0]
                    c=np.mean(b)
                    time_5min[i,2]=c
                else :
#                   当前3个周期没有数据时，用历史同期（同周日同时刻）的数据补全，这里还没有补全
                    time_5min[i,2]=1
        if time_5min[i,1]>0:
            time_5min[i,5]=time_5min[i,1]
        if time_5min[i,2]>0:
            time_5min[i,5]=time_5min[i,2]
            time_5min[i,6]=1
    return time_5min


















#开始数据分析，首先合并数据
down_data1,up_data1,day_num1=openfile(inpath1 = r"C:\Users\wutongshu\Desktop\贵阳数据\zh_zy1216-1231.csv", inpath2 = r"C:\Users\wutongshu\Desktop\贵阳数据\rj_zy1215-1231.csv")
down_data,up_data,day_num=openfile()
down_data_total=pd.concat([down_data,down_data1],ignore_index=True)
up_data_total=pd.concat([up_data,up_data1],ignore_index=True)
down_data_total2=down_data_total.drop_duplicates()
up_data_total2=up_data_total.drop_duplicates()
day_num=down_data_total2.day.unique()
#合并数据
down_data2=down_data_total2.iloc[:,[0,7,4,5,6]]
up_data2=up_data_total2.iloc[:,[0,7,4,5,6]]




#提取1202日数据
test_d1=down_data2[down_data2.iloc[:,4]==1202]
test_u1=up_data2[up_data2.iloc[:,4]==1202]
test_d1['car_length']=test_d1.iloc[:,0].apply(lambda x:len(x))
test_u1['car_length']=test_u1.iloc[:,0].apply(lambda x:len(x))
#剔除无牌及错误识别的数据
test_d2=test_d1[test_d1.iloc[:,-1]>2]
test_u2=test_u1[test_u1.iloc[:,-1]>2]
#不剔除数据进行统计
#统计下游的流量
match_1=test_d1[(test_d1.iloc[:,3]==3)]
match_2=test_u1[((test_u1.iloc[:,3]==3)&((test_u1.iloc[:,2]==3)|(test_u1.iloc[:,2]==4)|(test_u1.iloc[:,2]==5)))]
match_3=test_u1[((test_u1.iloc[:,3]==2)&(test_u1.iloc[:,2]==1))]
ap1=np.zeros((288,6))
for i in range(288):
    ap1[i,0]=i    
    aa=match_1[(match_1.iloc[:,1]>i*300)&(match_1.iloc[:,1]<(i+1)*300)]
    ap1[i,1]=len(aa)
    bb=match_2[(match_2.iloc[:,1]>i*300)&(match_2.iloc[:,1]<(i+1)*300)]
    cc=match_3[(match_3.iloc[:,1]>i*300)&(match_3.iloc[:,1]<(i+1)*300)] 
    ap1[i,2]=len(bb)
    ap1[i,3]=len(cc)
    ap1[i,4]=ap1[i,2]+ap1[i,3]
    ap1[i,5]=ap1[i,4]-ap1[i,1]
    
data_test=match_total_final[1]
data_test1=tt_deal[1]
a=data_test1[(data_test1.iloc[:,1]>0)&(data_test1.iloc[:,1]<7*3600)]   
b=a.iloc[:,8].quantile(0.15)



    
a8=plt.figure()
a8=plt.plot(tt_deal_5min2[1][:,0],tt_deal_5min2[1][:,5],'o-',markersize=3) 
a8=plt.plot(ap1[:,0],ap1[:,5],'o-',markersize=3) 
np.corrcoef(ap1[:,1],tt_deal_5min2[1][:,5])







    
    
a8=plt.figure()
#a8=plt.plot(ap1[:,0],ap1[:,1])
#a8=plt.plot(ap1[:,0],ap1[:,4])
a8=plt.plot(ap1[:,0],ap1[:,5])
a8=plt.plot(tt_deal_5min3[1][:,0],tt_deal_5min3[1][:,5],'o-',markersize=3) 



match_1=test1[((test1.iloc[:,3]==3)&((test1.iloc[:,2]==3)|(test1.iloc[:,2]==4)|(test1.iloc[:,2]==5)))]
match_2=test1[((test1.iloc[:,3]==2)&(test1.iloc[:,2]==1))]
match_1=test_d1[(test_d1.iloc[:,3]==3)]
match_2=test3[((test3.iloc[:,3]==2)&(test3.iloc[:,2]==1))]



#    初始化list
match_total_tt=[]
match_total_final=[]
match_total_rate=[]
#匹配车牌行程时间，按天分别匹配
for i in day_num:
    down_data3=down_data2[down_data2.iloc[:,-1]==i]
    up_data3=up_data2[up_data2.iloc[:,-1]==i]
    down_data4=down_data3.iloc[:,0:4]
    up_data4=up_data3.iloc[:,0:4]
    #因为这里没有车型属性，给其附上车型属性
    down_data4['car_type']=0
    up_data4['car_type']=0
    match_tt,match_final,match_rate=match_traveltime(up_data4,down_data4,maxtime=900,mintime=50,down_direction=3)        
    match_total_tt.append(match_tt)
    match_total_final.append(match_final)
    match_total_rate.append(match_rate)
    
#    绘制匹配行程时间的图
    a0=plt.figure()
    for i in range(28):
        a0=plt.subplot(4,7,i+1)
        a0=plt.scatter(match_total_final1[i].iloc[:,1],match_total_final1[i].iloc[:,9],s=15)
        a0=plt.xlim(0,86400)
        a0=plt.ylim(0,900)


        a0=plt.figure()
        a0=plt.scatter(match_total_final[1].iloc[:,1],match_total_final[1].iloc[:,9],s=15)
        a0=plt.xlim(0,86400)
        a0=plt.ylim(0,900)
        
        
        a0=plt.figure()
        a0=plt.scatter(tt_deal[15].iloc[:,1],tt_deal[15].iloc[:,8],s=15)
        a0=plt.xlim(0,86400)
        a0=plt.ylim(0,900)
        
        a2=plt.figure()
        a2=plt.plot(tt_deal_5min3[1][:,0],tt_deal_5min3[1][:,5],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900) 
        
        a2=plt.figure()
        a2=plt.plot(tt_deal_5min3[8][:,0],tt_deal_5min3[8][:,5],'o-',markersize=3)   
        a2=plt.plot(tt_deal_5min3[15][:,0],tt_deal_5min3[15][:,5],'o-',markersize=3) 
        a2=plt.plot(tt_deal_5min3[22][:,0],tt_deal_5min3[22][:,5],'o-',markersize=3) 
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900) 




#    行程时间预处理
    tt_deal=[]
    for i in range(31):
        test=match_total_final[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
        med_data=np.array(test)
        med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.8)
        tt_deal.append(med_deal)
#    绘制预处理后的数据图
    a1=plt.figure()
    for i in range(31):
        a1=plt.subplot(5,7,i+1)
        a1=plt.scatter(tt_deal[i].iloc[:,1],tt_deal[i].iloc[:,8],s=15)
        a1=plt.xlim(0,86400)
        a1=plt.ylim(0,900)



#    处理成五分钟行程时间,先得到历史数据
    tt_deal_5min=[]
    for i in range(31):
        med_data=tt_deal[i]
        med_deal=deal_5min(med_data,num=3,day=i)
        med_deal2=pd.DataFrame(med_deal)
        tt_deal_5min.append(med_deal2)
    match_final_1 = pd.concat(tt_deal_5min, ignore_index=True)    
    match_final_2=match_final_1[match_final_1.iloc[:,1]>1] 
    
#   利用历史数据进行补全 
   tt_deal_5min2=[] 
   for i in range(31):
       med_data=np.array(tt_deal_5min[i])
       for j in range(288):
           if med_data[j,2]==1:
               c=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data[j,4])]
               if len(c)>0:
                   med_data[j,5]=np.mean(c.iloc[:,1])
        
               
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
    
    a2=plt.figure()
    for i in range(31):
        a2=plt.subplot(5,7,i+1)
        a2=plt.plot(tt_deal_5min2[i][:,0],tt_deal_5min2[i][:,5],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900)        
    
    
#平滑数据,使用对数平滑数据
    tt_deal_5min3=[]
    for i in range(31): 
        med_data=np.array(tt_deal_5min2[i])
        for j in range(1,288):
            med_data[j,5]=math.exp(0.5*math.log(med_data[j,5])+0.5*math.log(med_data[j-1,5]))
        tt_deal_5min3.append(med_data)     
    
    a2=plt.figure()
    for i in range(31):
        a2=plt.subplot(5,7,i+1)
        a2=plt.plot(tt_deal_5min3[i][:,0],tt_deal_5min3[i][:,1],'o-',markersize=3)   
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900)     
        a2=plt.figure()
        a2=plt.plot(tt_deal_5min3[0][:,0],tt_deal_5min3[2][:,5],'o-',markersize=3)  
        a2=plt.plot(tt_deal_5min3[9][:,0],tt_deal_5min3[9][:,5],'o-',markersize=3) 
        a2=plt.plot(tt_deal_5min3[16][:,0],tt_deal_5min3[16][:,5],'o-',markersize=3)
        a2=plt.plot(tt_deal_5min3[23][:,0],tt_deal_5min3[23][:,5],'o-',markersize=3)
        a2=plt.xlim(0,289)
        a2=plt.ylim(0,900)     
        

    
    
#预测数据
tt_deal_5min4=[]
for i in range(31): 
        med_data=np.array(tt_deal_5min2[i])
        ap=np.zeros((289,7))
        for j in range(3,288):
            ap[j,0]=j
            ap[j,1]=med_data[j-2,5]
            ap[j,2]=med_data[j-1,5]
            ap[j,3]=med_data[j,5]
            ap[j,4]=med_data[j,4]
            ap[j,5]=med_data[j+1,5]
            ap[j,6]=i/7
        tt_deal_5min4.append(pd.DataFrame(ap))
match_final_3 = pd.concat(tt_deal_5min4, ignore_index=True)     
match_final_4=match_final_3[match_final_3.iloc[:,1]>0]             






import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import mean_squared_error

x0=match_final_4[(match_final_4.iloc[:,6]>=0)&(match_final_4.iloc[:,6]<=2)]    
x1=np.array(x0.iloc[:,:-2])
y1=np.array(x0.iloc[:,-2])
gbm0 = GradientBoostingRegressor(n_estimators=80, learning_rate=0.1, max_depth=3, random_state=10, loss='ls')    
gbm0.fit(x1,y1)  
mean_squared_error(y1, gbm0.predict(x1)) 


x2=match_final_4[match_final_4.iloc[:,6]==3]    
x3=np.array(x2.iloc[:,:-2])
y3=np.array(x2.iloc[:,-2])
mean_squared_error(y3, gbm0.predict(x3)) 
aa=gbm0.predict(x3)
gbm0 = GradientBoostingRegressor(random_state=10)  


param_test1 = {'n_estimators':range(20,300,10)}
gsearch1 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, min_samples_split=300,
                                  min_samples_leaf=20,max_depth=8,max_features='sqrt', subsample=0.8,random_state=10), 
                       param_grid = param_test1,iid=False,cv=5)
gsearch1.fit(x1,y1)
gsearch1.grid_scores_, gsearch1.best_params_, gsearch1.best_score_


param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(100,801,200)}
gsearch2 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=80, min_samples_leaf=20, 
      max_features='sqrt', subsample=0.8, random_state=10), 
   param_grid = param_test2,iid=False, cv=5)
gsearch2.fit(x1,y1)
gsearch2.grid_scores_, gsearch2.best_params_, gsearch2.best_score_

param_test3 = {'min_samples_split':range(300,1200,200), 'min_samples_leaf':range(30,101,10)}
gsearch3 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=80,max_depth=9,
                                     max_features='sqrt', subsample=0.8, random_state=10), 
                       param_grid = param_test3, iid=False, cv=5)
gsearch3.fit(x1,y1)
gsearch3.grid_scores_, gsearch3.best_params_, gsearch3.best_score_


param_test4 = {'learning_rate':[0.001,0.005,0.01,0.1,1]}
gsearch4 = GridSearchCV(estimator = GradientBoostingRegressor(learning_rate=0.1, n_estimators=80,max_depth=9, min_samples_leaf =40, 
               min_samples_split =500, subsample=0.8, random_state=10), 
                       param_grid = param_test4, iid=False, cv=5)
gsearch4.fit(x1,y1)
gsearch4.best_params_    
    
gsearch4.fit(x1,y1)
gsearch4.grid_scores_, gsearch4.best_params_, gsearch4.best_score_



y4=np.zeros((1994,1))

for i in range(1994):
    y4[i,0]=np.mean(x3[i,1:4])
mean_squared_error(y3, y4) 
mean_squared_error(y3, gbm0.predict(x3)) 


from sklearn import svm
clf = svm.SVR(C=0.0001)
clf.fit(x1, y1)
mean_squared_error(y3, clf.predict(x3)) 
y5=clf.predict(x3)

a2=plt.figure()
a2=plt.plot(y3,'o-',markersize=3)
a2=plt.plot(aa,'o-',markersize=3)
a2=plt.plot(y5,'o-',markersize=3)
a2=plt.plot(aa,'o-',markersize=3)

