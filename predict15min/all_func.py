# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:21:49 2017

@author: wutongshu
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 13:52:45 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.ensemble import RandomForestRegressor
#方向：1表示东，4表示北






#原始数据第1列车牌，第2列过车时刻，第3列车道，第4列为进口道方向，第5列为车型；
def openfile(inpath1 = r"C:\Users\wutongshu\Desktop\贵阳数据\zh_zy1201-1215.csv", inpath2 = r"C:\Users\wutongshu\Desktop\贵阳数据\rj_zy1201-1215.csv"):
    uipath1 = unicode(inpath1 , "utf8")
    uipath2 = unicode(inpath2 , "utf8")
    down_data=pd.read_csv(uipath1,encoding='gbk')
    up_data=pd.read_csv(uipath2,encoding='gbk')
    down_data.iloc[:,2]=pd.to_datetime(down_data.iloc[:,2])
    up_data.iloc[:,2]=pd.to_datetime(up_data.iloc[:,2])
    down_data['day']=down_data.iloc[:,2].apply(lambda x:100*x.month+x.day)
    up_data['day']=up_data.iloc[:,2].apply(lambda x:100*x.month+x.day)
    down_data['sj']=down_data.iloc[:,2].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    up_data['sj']=up_data.iloc[:,2].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    day_num=down_data.day.unique()
    return down_data,up_data,day_num


#数据转换函数，即将时间化为秒，和按天区分
#原始数据第1列车牌，第2列过车时刻，第3列车道，第4列为进口道方向，第5列为车型
def dataTran(dataSet):
    dataSet.iloc[:,1]=pd.to_datetime(dataSet.iloc[:,1])
    dataSet['sj']=dataSet.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    dataSet['day']=dataSet.iloc[:,1].apply(lambda x:100*x.month+x.day)
    day_num=dataSet.day.unique()
    return dataSet,day_num
    
    
    
    
    
    
    
    
    
    



#2.匹配行程时间函数
#原始数据第1列车牌，第2列过车时刻，第3列车道，第4列为进口道方向，第5列为车型；

#行程时间匹配函数，以下为参数说明
#up_data上游数据，down_data下游数据，down_direction下游进口道的方向，
#maxtime最大匹配行程时间，mintime最小匹配行程时间
#匹配函数
def match_traveltime(up_data,down_data,maxtime,mintime,down_direction):
    down_data=down_data[down_data.ix[:,3]==down_direction]
    down_data.index=range(len(down_data))
#筛选正常数据，异常数据主要为未识别和无牌，因此数据位数都不为9,中文字符占2个
    down_data=down_data.assign(car_length=down_data.iloc[:,0].apply(lambda x:len(x)))
#    down_data['car_length']=down_data.iloc[:,0].apply(lambda x:len(x))
    down_true=down_data[(down_data.iloc[:,5]==7 )| (down_data.iloc[:,5]==9)]
    down_true.index=range(len(down_true))
#计算下游识别率
#    if len(up_data)>0:
#        plate_identify_rate1=float(len(down_true))/len(down_data)
#同理筛选上游正常数据，异常数据主要为未识别和无牌，因此数据位数都不为9
    up_data=up_data.assign(car_length=up_data.iloc[:,0].apply(lambda x:len(x)))
#    up_data['car_length']=up_data.iloc[:,0].apply(lambda x:len(x))
    up_true=up_data[(up_data.iloc[:,5]==7)|(up_data.iloc[:,5]==9)]
    up_true.index=range(len(up_true))
#计算上游识别率
#    if len(up_data)>0:
#        plate_identify_rate2=float(len(up_true))/len(up_data)
#初始化最终的大矩阵match_du，上游的车牌先进行排序
    down_true1=np.array(down_true)
    down_true=down_true.assign(up_t=np.nan)
    down_true=down_true.assign(up_clane=np.nan)
    down_true=down_true.assign(up_direct=np.nan)
    down_true=down_true.assign(tt=0)
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
    for h in range(1,len(match_time1)):
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
    if len(match_du)==0:
        match_rate=0
    else :
        match_rate=float(len(match_final))/len(match_du)
    return match_tt,match_final,match_rate

    
    
#循环匹配函数,前面为上下游数据，以及天，后面为匹配函数的主要参数
def loopMatch(downData,upData,dayNum,maxtime1=900,mintime1=40,down_direction1=3):
    match_total_tt=[]
    match_total_final=[]
    match_total_rate=[]
    #匹配车牌行程时间，按天分别匹配
    for i in dayNum:
        down_data2=downData[downData.iloc[:,-1]==i]
        up_data2=upData[upData.iloc[:,-1]==i]
        if (len(down_data2)==0)|(len(up_data2)==0):
            match_total_tt.append(0)
            match_total_final.append(0)
            match_total_rate.append(0)
            continue
        down_data3=down_data2.iloc[:,[0,5,2,3,4]]
        up_data3=up_data2.iloc[:,[0,5,2,3,4]]
        match_tt,match_final,match_rate=match_traveltime(up_data3,down_data3,maxtime=maxtime1,mintime=mintime1,down_direction=down_direction1)        
        match_total_tt.append(match_tt)
        match_total_final.append(match_final)
        match_total_rate.append(match_rate)
    return match_total_tt,match_total_final,match_total_rate
    



#驶入驶出流量统计函数，参数1为上游交叉口，参数2为下游交叉口，参数3为上游交叉口驶入方向1，参数4为上游交叉口驶入方向1的驶入车道
#参数5为上游交叉口驶入方向2，参数6为上游交叉口驶入方向2的驶入车道
#参数7为下游驶出方向1，参数8为下游交叉口的驶出方向1的驶出车道,参数9为下游交叉口的驶出方向1的驶出车道匹配统计的车道
#返回数组是第1列是时间，第2列为驶入量，第3列为驶出量，第4列为匹配车道的过车流量
def inOut(upInsec,downInsec,upDire1,upClane1,upDire2,upClane2,downDire,downClane1):
    upInsec.iloc[:,1]=pd.to_datetime(upInsec.iloc[:,1])
    downInsec.iloc[:,1]=pd.to_datetime(downInsec.iloc[:,1])
    upInsec['day']=upInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    upInsec['sj']=upInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    downInsec['day']=downInsec.iloc[:,1].apply(lambda x:100*x.month+x.day)
    downInsec['sj']=downInsec.iloc[:,1].apply(lambda x:3600*x.hour+60*x.minute+x.second)
    q_total=[]
    for i in range(1204,1232):
        med_data=np.zeros((96,5))
        med_data[:,0]=range(96)
    
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
        for j in range(96):
            med_data[j,1]=len(in_q1Final[(in_q1Final.iloc[:,-2]>j*15*60)&(in_q1Final.iloc[:,-2]<(j+1)*15*60)])+len(in_q2Final[(in_q2Final.iloc[:,-2]>j*15*60)&(in_q2Final.iloc[:,-2]<(j+1)*15*60)])
            med_data[j,2]=len(out_q1Final[(out_q1Final.iloc[:,-2]>j*15*60)&(out_q1Final.iloc[:,-2]<(j+1)*15*60)])
            med=out_q1Final[(out_q1Final.iloc[:,-2]>j*15*60)&(out_q1Final.iloc[:,-2]<(j+1)*15*60)]
            med_final1=[]
            for y in downClane1:
                cach=med[(med.iloc[:,2]==y)]
                med_final1.append(cach)
            medFinal=pd.concat(med_final1, ignore_index=True)
            med_data[j,3]=len(medFinal)
        q_total.append(med_data)    
    return q_total
















def listConcat(data):
    medDataFinal=data[0]
    for i in range(1,len(data)):
        medDataFinal=np.vstack([medDataFinal,data[i]])
    return medDataFinal










    

    
#循环处理数据
def loopDeal(match_total_final,claneNum):
    tt_deal=[]
    for i in range(len(match_total_final)):
        test=match_total_final[i].iloc[:,[0,1,2,3,4,6,7,8,9]]
        if len(test)>0:
            medData=[]
            for j in claneNum:
                straightData=test[(test.iloc[:,2]==j)]
                medData.append(straightData)
            medFinal=pd.concat(medData, ignore_index=True) 
            med_data=np.array(medFinal)
            med_deal=data_deal(med_data,tet=60,tet1=1800,tet2=300,num=10,td=90,lc=1.1)
        else :
            med_deal=0
        tt_deal.append(med_deal)  
    return tt_deal
        
    
    
#验证匹配率变化值
#路段1的匹配率变化曲线，首先选择出直行车辆上的车辆数
def matchRate(matchTotal,clane):
    rateMat=np.zeros((len(matchTotal),96))
    for i in range(len(matchTotal)):
        medData=matchTotal[i]
        medData1=[]
        for j in clane:
            straightData=medData[medData.iloc[:,2]==j]
            medData1.append(straightData)
        medFinal=pd.concat(medData1, ignore_index=True) 
        med_data=np.array(medFinal)
        for h in range(96):
            medData2=med_data[(med_data[:,1]>15*60*h)&(med_data[:,1]<15*60*(h+1))]
            if len(medData2)>0:
                a=len(medData2[medData2[:,-1]>0])
                b=len(medData2)
                c=float(a)/b
                
            else :
                c=-0.1
#                print 'None'
            rateMat[i,h]=c
    return rateMat    
    
    
    
#得到每天匹配率的分位值：
def rateQuan(rateMat):
    rateQ=np.zeros((rateMat.shape[0],5))
    for i in range(rateMat.shape[0]):
        a=rateMat[i,:]
        a=a[a>-0.1]
        quan_5=np.percentile(a,5)
        quan_15=np.percentile(a,15)
        quan_35=np.percentile(a,35)
        quan_50=np.percentile(a,50)
        quan_75=np.percentile(a,75)
        rateQ[i,0]=quan_5
        rateQ[i,1]=quan_15
        rateQ[i,2]=quan_35
        rateQ[i,3]=quan_50
        rateQ[i,4]=quan_75
    return rateQ    
    
    
    

    
    
    
    
    
    
    
    
    


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

#4.处理成15分钟数据函数  ,输入原始数据为第一行为下游时刻，第二行为行程时间  
#车牌匹配后的行程时间DataFrame，含9列，1列车牌信息，2列为下游过车时刻，3列下游车道编号，4列下游行驶方向，5列车型，6列上游过车时刻，7列上游车道编号，8列上游进口方向，9列行程时间
#num是行程时间置信数量，就是当匹配到的车辆数少于一定时，考虑如何对数据进行修正
#输出数据，第1列时间，第2列5分钟均值，第3列为是否为补全数据，第4列中位数，第5列周几，第6列为最后数据，第7列为是否为补全数据


#def deal_5min(match_time,num=3,day=0,data_full=60):
#    match_time1=np.array(match_time)
#    time_5min=np.zeros((96,7))
#    time_5min[:,0]=np.linspace(0,24,96)
#    time_5min[:,4]=(day+2)%7
#    for i in range(96):
#        data_m=match_time1[(match_time1[:,1]>i*3*300)&(match_time1[:,1]<(i+1)*3*300)]
#        if len(data_m)>num:
#            time_5min[i,1]=np.mean(data_m[:,8])
#            time_5min[i,3]=np.median(data_m[:,8])
##       样本数量较小，进行补全数据
#        elif len(data_m)<=num:
##           当处于夜间低峰期时
#            time_5min[i,1]=-1
#            if i<=4*7 :
##               i大于3开始
#                if i>=3:
##               判断前N=3个周期是否存在数据
#                    if np.sum(time_5min[i-3:i,1])>0:
#                        a=time_5min[i-3:i,1]
#                        b=a[a>0]
#                        c=np.mean(b)
#                        time_5min[i,2]=c
#                    else :
##                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
#                        time_5min[i,2]=data_full
##                i小于3时，
#                elif (i>0)&(i<3) :
#                    if np.sum(time_5min[0:i,1])>0:
#                        a=time_5min[0:i,1]
#                        b=a[a>0]
#                        c=np.mean(b)
#                        time_5min[i,2]=c
#                    else :
##                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
#                        time_5min[i,2]=data_full
#                elif i==0 :
#                    if np.sum(time_5min[0,1])>0:
#                        a=time_5min[0,1]
#                        b=a[a>0]
#                        c=np.mean(b)
#                        time_5min[i,2]=c
#                    else :
##                       当前3个周期没有数据时，用信号控制下的自由流行程时间补全
#                        time_5min[i,2]=data_full
##           当非低峰期时，使用前3个周期的数据的特征值进行补全
#            if i>3*7:
##               判断前N=3个周期是否存在数据
#                if np.sum(time_5min[i-3:i,1])>0:
#                    a=time_5min[i-3:i,1]
#                    b=a[a>0]
#                    c=np.mean(b)
#                    time_5min[i,2]=c
#                else :
##                   当前3个周期没有数据时，用历史同期（同周日同时刻）的数据补全，这里还没有补全
#                    time_5min[i,2]=1
#        if time_5min[i,1]>0:
#            time_5min[i,5]=time_5min[i,1]
#        if time_5min[i,2]>0:
#            time_5min[i,5]=time_5min[i,2]
#            time_5min[i,6]=1
#    return time_5min
    
    
#处理成15min函数，第一个参数是预处理后的数据集，第二个是下游的过车的流量，第3个是给他们加上星期属性，第四个是自由流行程时间；   
#第5个为最低匹配率，默认为10%
def deal_5min(match_time,q,day=0,data_full=60,K=0.1,L=400):
#   定义拥堵速度为5km/h
    Vb=5
    match_time1=np.array(match_time)
    time_5min=np.zeros((96,7))
    time_5min[:,0]=range(96)
    time_5min[:,4]=(day+2)%7
    for i in range(96):
        num=q[i,3]*K
        data_m=match_time1[(match_time1[:,1]>i*3*300)&(match_time1[:,1]<(i+1)*3*300)]
        if len(data_m)>num:
            time_5min[i,1]=np.mean(data_m[:,8])
            time_5min[i,3]=np.median(data_m[:,8])
#       样本数量较小，进行补全数据
        elif len(data_m)<=num:
#           当处于夜间低峰期时
            time_5min[i,1]=-1
            if i<=4*6 :
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
            if i>4*6:
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
    c=match_final_2[(match_final_2.iloc[:,0]>0)&(match_final_2.iloc[:,0]<24)]
#    取自由流速度
    data_full1=np.percentile(c.iloc[:,1],15)
    deal_15min_2=[]
    for z in range(len(dataDeal)):
        med_data=dataDeal[z]
        q1=q_total[i]
        med_deal=deal_5min(med_data,q1,day=i,data_full=data_full1,K=0.1,L=400)
        med_data1=np.array(med_deal)
        for j in range(96):
		#这里针对前3个周期都没有数据的情况，进行补全，考虑使用历史同星期，同时刻的均值进行补全；
            if med_data1[j,5]==1:
                d=match_final_2[(match_final_2.iloc[:,0]==j)&(match_final_2.iloc[:,4]==med_data1[j,4])]
                if len(d)>0:
                   med_data1[j,5]=np.mean(d.iloc[:,1])
                elif len(d)==0:
                   med_data1[j,5]= med_data1[j-1,5]
        deal_15min_2.append(med_data1)
    return deal_15min_2,data_full1

    
    
    
    
    
    
    
    
    
def computeCorrelation(X, Y):  
    xBar = np.mean(X)  
    yBar = np.mean(Y)  
    SSR = 0  
    varX = 0  
    varY = 0  
    for i in range(0, len(X)):  
        #对应分子部分  
        diffXXBar = X[i] - xBar  
        diffYYBar = Y[i] - yBar  
        SSR +=(diffXXBar * diffYYBar)  
        #对应分母求和部分  
        varX += diffXXBar**2  
        varY += diffYYBar**2  
    SST = math.sqrt(varX * varY)  
    return SSR/SST  




def gridSearch(train_data,valid_data,pamater=range(20,200,20)):
    MAPE=np.zeros((1,len(pamater)))
    train_x=np.array(train_data.iloc[:,:-1])
    train_y=np.array(train_data.iloc[:,-1])
    valid_x=np.array(valid_data.iloc[:,:-1])
    valid_y=np.array(valid_data.iloc[:,-1])
    minMape=1
    minPam=0
    for i,j in enumerate(pamater):
        gbm0 = RandomForestRegressor(n_estimators=j, min_samples_split=50,\
                                      min_samples_leaf=20,max_depth=4,max_features='sqrt',random_state=0)  
        gbm0.fit(train_x,train_y)
        aa1=np.hstack([valid_y.reshape(-1,1), gbm0.predict(valid_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        if c1<minMape:
            minMape=c1
            minPam=i
        MAPE[0,i]=c1
    return minMape,pamater[minPam],MAPE


#状态评估函数
def stateMap(x,freeV=86.3):
    c=0
    x=max(1-freeV/x,0)
    if (x>=0)&(x<=0.2):
        c=0
    elif (x>0.2)&(x<=0.4):
        c=1
    elif (x>0.4)&(x<=0.6):
        c=2
    elif (x>0.6)&(x<=0.8):
        c=3
    elif (x>0.8):
        c=4
    return c        



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






































