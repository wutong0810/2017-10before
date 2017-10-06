# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:26:12 2017

@author: wutongshu
"""
import pandas as pd

path1=r'E:\huaweiDataFinal\1.txt'

#第1列carNumber1 ,第2列carNumber2 ,第3列 carNumType1 ,
#第4列carNumType2 ,第5列 dateCollect ,第6列 collectAddress ,
#第7列inOutType ,第8列 claneId ,第9列carType ,
#第10列illegalType ,第11 列carSpeed ,第12 列carDirect 
chunks = pd.read_csv(path1,header=None,usecols=[0,4,5,7,10])
#chunk = chunks.get_chunk(2000)
#print chunk
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
pysqldf('''
        select * from chunks ;''').head()



import pandas as pd
#读入数据
path1=r'E:\huawei\huaweiDataFinal\24.txt'
#写出数据
path2=r'E:\huawei\huaweiDataFinal2\24.txt'

#第1列carNumber1 ,第2列carNumber2 ,第3列 carNumType1 ,
#第4列carNumType2 ,第5列 dateCollect ,第6列 collectAddress ,
#第7列inOutType ,第8列 claneId ,第9列carType ,
#第10列illegalType ,第11 列carSpeed ,第12 列carDirect 

chunks = pd.read_csv(path1,header=None) 
chunks.to_csv(path2,index=False,header=None,encoding='gbk')



import pandas as pd
a2=pd.read_csv(r'E:\errData\rrImport_ysb_201705241801_01_9.txt',header=None)
a2.to_csv(path2,index=False,header=None,mode='a',encoding='gbk')



chunks = pd.read_csv(path1,header=None,usecols=[0,4,5,7,10]) 