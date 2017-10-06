# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:31:16 2017

@author: wutongshu
"""
import os
import pandas as pd
for i in g[4:10]:
    for j in i:
        try :
            a1=os.path.split(j)[0]
            a2=os.path.split(j)[1]
            b=os.path.split(a1)[1]
            c1=os.path.join(r'E:\huawei\huaweiData',b)
            c2=os.path.join(c1,a2)
            
            print c2
            pd.read_csv(c2,header=None)
        except Exception, e:
            print str(e)

#第一列数据车牌1，第二列车牌2，第三列车牌类型1，第四列车牌类型2，第五列车牌识别时间，第六列检测点id，第七列
#进出口类型，第八列车道id，第九列颜色，第十列类型，
#第十一列,第十二列,第十三列 车标 信息卡编码 违法类型 
#第十四列,第十五列,第十六列 速度 前端id 行驶方向

import os
import pandas as pd
data=pd.read_csv(r'E:\huawei\huaweiDataFinal\19.txt',header=None,parse_dates=[4])

#timeStart='2017-05-13 00:00:00'
#timeEnd='2017-05-13 23:59:59'

timeStart=pd.to_datetime('2017-05-19 00:00:00')
timeEnd=pd.to_datetime('2017-05-19 23:59:59')



data=data[(data.iloc[:,4]>timeStart)&(data.iloc[:,4]<timeEnd)]



data.iloc[:,0]=data.iloc[:,0].apply(lambda x:str(x))

data.iloc[:,0]=data.iloc[:,0].apply(lambda x:unicode(x,"utf8"))


#data['carLen']=data.iloc[:,0].apply(len)

#data['carBegin']=data.iloc[:,0].apply(strGet)


#wrongData=data.iloc[:,-1].apply(lambda x:x!=35)

carTimes=data.iloc[:,0].value_counts()

carTimes=carTimes.reset_index()



aa2=data.iloc[:,0].value_counts().head(10)

aa2=aa2.reset_index()
carTimes['carBegin']=carTimes.iloc[:,0].apply(strGet)

cc1=carTimes['carBegin'].value_counts()



len(data)








aa1=data['carBegin'].value_counts()


carTimes=data.iloc[:,0].value_counts()

carTimes=carTimes.reset_index()


carTimes['carLen']=carTimes.iloc[:,0].apply(lambda x: len(x))

def strGet(x):
    if len(x)>3:
        y=x[:2]
    else :
        y=0
    return y


carTimes['carBegin']=carTimes.iloc[:,0].apply(strGet)

c=carTimes.iloc[1,0]


cc1=carTimes['carBegin'].value_counts()










Carnum1=['京','津','沪','渝','冀','渝','云','辽','黑','湘' ,'皖' ,'鲁' ,'新','苏','浙','赣','鄂','桂','甘','晋','蒙','闽','贵','粤','青','川','宁','琼','军']


Carnum2=[chr(i) for i in range(65,91)]

Carnum=[]
for i in Carnum1:
    for j in Carnum2:
        Carnum.append(unicode(i+j,"utf8"))
        print unicode(i+j,"utf8")
        




















