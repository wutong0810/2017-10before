# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 08:44:11 2017

@author: wutongshu
"""

import urllib2
import json
import pandas as pd
import numpy as np
import json
cordId=pd.read_csv(r'C:\Users\wutongshu\Desktop\sz.csv')



#html='http://api.map.baidu.com/direction/v1?mode=driving&origin='+'北京邮电大学'+'&destination='+'北京大学'+'&origin_region=深圳&destination_region=深圳&output=json&ak=FEWAdks14E8Kul8QtRUO01p1'
#
#response=urllib2.urlopen(html,timeout=5)
#a=response.read()
#b=json.loads(a)
#b['result']['routes'][0]['distance']
#b['result']['routes'][0]['duration']
num=len(cordId)**2
distance=np.zeros((len(cordId)**2,6))
for i in range(200,248):
    for j in range(len(cordId)):
        distance[i*len(cordId)+j,0]=cordId.iloc[i,0]
        distance[i*len(cordId)+j,1]=cordId.iloc[j,0]
        distance[i*len(cordId)+j,4]=1
        html='http://api.map.baidu.com/direction/v1?mode=driving&origin='+str(cordId.iloc[i,2])+','+str(cordId.iloc[i,1])+'&destination='+str(cordId.iloc[j,2])+','+str(cordId.iloc[j,1])+'&origin_region=深圳&destination_region=深圳&output=json&coord_type=wgs84&ak=KNZIT83bDR7X4AwUyrxxELh96RtR1Svq'
        try:
            print 'finished'+'%2.1f'%((j+i*len(cordId))/float(num)*100)+'%'
            response=urllib2.urlopen(html,timeout=5)
            a=response.read()
            b=json.loads(a)
            if b['status']==0:
                distance[i*len(cordId)+j,5]=1
                distance[i*len(cordId)+j,2]=b['result']['routes'][0]['distance']
                distance[i*len(cordId)+j,3]=b['result']['routes'][0]['duration']
        except Exception, e:
            print str(e)