# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 12:00:00 2017

@author: wutongshu
"""
import pandas as pd
dianwei=pd.read_csv(r'C:\Users\wutongshu\Desktop\alldianwei.csv',encoding='gbk')
dianwei1=dianwei[dianwei.LATITUDE>0]



import pandas as pd
dianwei2=pd.read_csv(r'C:\Users\wutongshu\Desktop\20170904kongjian.csv',encoding='gbk')

dianwei3=dianwei2[dianwei2.CADDRESSCODE>0]
dianwei4=dianwei2[(dianwei2.CCOLLECTIONADDRESS>0) & (dianwei2.CADDRESSCODE.isnull())]

dataFinal1=pd.merge(dianwei3,dianwei1,how='left',on='CADDRESSCODE')

data2=dataFinal1.groupby([dataFinal1['DAYS'],dataFinal1['HOURS'],dataFinal1['CADDRESSCODE']])['N','LATITUDE','LONGITUDE'].mean()
data2=data2.reset_index()



data3=data2[data2.LATITUDE>0]




data3.to_csv(r'd:\1.csv')
