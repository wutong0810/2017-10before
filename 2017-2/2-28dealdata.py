# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:51:20 2017

@author: wutongshu
"""



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
a0=plt.scatter(match_total_final1[27].iloc[:,1],match_total_final1[27].iloc[:,9],s=15)
match_du=match_total_final1[27]

def data_deal(match_du,T_up=900,T_down=40,tet=60,tet1=1800,tet2=300):
    final=[]
    for i in range(0,7*3600,900):
#       时间段划分，0到7点为一个处理间隔
        med_1=np.array(match_du[(match_du.iloc[:,1]>i)&(match_du.iloc[:,1]<i+900)])
#        初步剔除
        med_2=med_1[(med_1[:,9]>T_down)&(med_1[:,9]<T_up)]
        if len(med_2)>0:
            th=np.std(med_2[:,9])
            t_mean=np.mean(med_2[:,9])
            med_3=med_2[(med_2[:,9]<t_mean+2*th)&(med_2[:,9]>t_mean-2*th)]
            if len(med_3)>0:
                b=pd.DataFrame(med_3)
            for j in range(5):
                b=pd.DataFrame(b)
                if len(b)>0:
                    b=np.array(b.sort_values(by=b.columns[9]))
                    if mod(len(b),2)==0:
                        m=(len(b))/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m,9])-m*a)/m
                        d2=(np.sum(b[m+1:,9])-m*a)/m
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
                    elif mod(len(b),2)==1:
                        m=(len(b)+1)/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m-1,9])-(m-1)*a)/(m-1)
                        d2=(np.sum(b[m+1:,9])-(m-1)*a)/(m-1)
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
            final.append(pd.DataFrame(b)) 
     
    for i in range(7*3600,24*3600,300):
#       时间段划分，0到7点为一个处理间隔
        med_1=np.array(match_du[(match_du.iloc[:,1]>i)&(match_du.iloc[:,1]<i+300)])
#        初步剔除
        med_2=med_1[(med_1[:,9]>T_down)&(med_1[:,9]<T_up)]
        if len(med_2)>0:
            th=np.std(med_2[:,9])
            t_mean=np.mean(med_2[:,9])
            med_3=med_2[(med_2[:,9]<t_mean+2*th)&(med_2[:,9]>t_mean-2*th)]
            if len(med_3)>0:
                b=pd.DataFrame(med_3)
            for j in range(5):
                b=pd.DataFrame(b)
                if len(b)>0:
                    b=np.array(b.sort_values(by=b.columns[9]))
                    if mod(len(b),2)==0:
                        m=(len(b))/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m,9])-m*a)/m
                        d2=(np.sum(b[m+1:,9])-m*a)/m
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
                    elif mod(len(b),2)==1:
                        m=(len(b)+1)/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m-1,9])-(m-1)*a)/(m-1)
                        d2=(np.sum(b[m+1:,9])-(m-1)*a)/(m-1)
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
            final.append(pd.DataFrame(b)) 
    match_final1 = pd.concat(final, ignore_index=True)             
            
            
            
            
            
    for i in range(7,24*3600,300):
        med_1=np.array(match_du[(match_du.iloc[:,1]>i)&(match_du.iloc[:,1]<i+900)])
        med_2=med_1[(med_1[:,9]>T_down)&(med_1[:,9]<T_up)]
        th=np.std(med_2[:,9])
        t_mean=np.mean(med_2[:,9])
        med_3=med_2[(med_2[:,9]<t_mean+2*th)&(med_2[:,9]>t_mean-2*th)]
        if len(med_3)>0:
                b=pd.DataFrame(med_3)
            for j in range(3):
                b=pd.DataFrame(b)
                if len(b)>0:
                    b=np.array(b.sort_values(by=b.columns[9]))
                    if mod(len(b),2)==0:
                        m=(len(b))/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m,9])-m*a)/m
                        d2=(np.sum(b[m+1:,9])-m*a)/m
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
                    elif mod(len(b),2)==1:
                        m=(len(b)+1)/2
                        a=np.median(b[:,9])
                        d1=(np.sum(b[0:m-1,9])-(m-1)*a)/(m-1)
                        d2=(np.sum(b[m+1:,9])-(m-1)*a)/(m-1)
                        c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                        b=c
            final.append(pd.DataFrame(b))         
     
    


    
        a0=plt.scatter(match_final1.iloc[:,1],match_final1.iloc[:,9],s=15)
        a0=plt.scatter(match_du.iloc[:,1],match_du.iloc[:,9],s=15)
        a0=plt.scatter(med_deal.iloc[:,1],med_deal.iloc[:,8],s=15)
        b=pd.DataFrame(med_3)
        for j in range(4):
            b=pd.DataFrame(b)
            b=np.array(b.sort_values(by=b.columns[9]))
            if mod(len(b),2)==0:
                m=(len(b))/2
                a=np.median(b[:,9])
                d1=(np.sum(b[0:m,9])-m*a)/m
                d2=(np.sum(b[m+1:,9])-m*a)/m
                c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                b=c
            elif mod(len(b),2)==1:
                m=(len(b)+1)/2
                a=np.median(b[:,9])
                d1=(np.sum(b[0:m-1,9])-m*a)/(m-1)
                d2=(np.sum(b[m+1:,9])-m*a)/(m-1)
                c=b[(b[:,9]>a+3*d1)&(b[:,9]<a+3*d2)]
                b=c
        final.append(pd.DataFrame(b))  
         
            a=np.median(b[:,9])
            d=(np.sum(b[:,9])-len(b)*a)/float(len(b))
            
            c=b[(b[:,9]<a+3*d)&(b[:,9]>a-3*d)]
            b=c
        t_mediam=np.median(med_3[:,9])
        d=(np.sum(med_3[:,9])-len(med_3)*t_mediam)/float(len(med_3))
        med_4=med_3[(med_3[:,9]<t_mediam+3*d)&(med_3[:,9]>t_mediam-3*d)]
        
        t_mediam=np.median(med_4[:,9])
        d=(np.sum(med_4[:,9])-len(med_4)*t_mediam)/float(len(med_4))
        med_5=med_4[(med_4[:,9]<t_mediam+3*d)&(med_4[:,9]>t_mediam-3*d)]
            
        t_mediam=np.median(med_4[:,9])
        d=(np.sum(med_4[:,9])-len(med_4)*t_mediam)/float(len(med_4))
        med_5=med_4[(med_4[:,9]<t_mediam+3*d)&(med_4[:,9]>t_mediam-3*d)]

        t_mediam=np.median(med_4[:,9])
        d=(np.sum(med_4[:,9])-len(med_4)*t_mediam)/float(len(med_4))
        med_5=med_4[(med_4[:,9]<t_mediam+3*d)&(med_4[:,9]>t_mediam-3*d)]

        t_mediam=np.median(med_4[:,9])
        d=(np.sum(med_4[:,9])-len(med_4)*t_mediam)/float(len(med_4))
        med_5=med_4[(med_4[:,9]<t_mediam+3*d)&(med_4[:,9]>t_mediam-3*d)]
        
    for i in range(step):
        if (i*tet<3600*7)|(i*tet>=3600*19.5):
            ap_et[i,0]=i*tet-tet1
            ap_et[i,1]=i*tet
        else:
            ap_et[i,0]=i*tet-tet2
            ap_et[i,1]=i*tet
        if ap_et[i,0]<0:
            ap_et[i,0]=0