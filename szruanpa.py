# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:05:15 2017

@author: wutongshu
"""

import urllib2
import json
import pandas as pd
import numpy as np
import json
cordId=pd.read_csv(r'C:\Users\wutongshu\Desktop\sz.csv')



distance0=distance[distance[:,4]==1]



a=np.vstack([distance0,d1,d2,d3,d4])
bb=a[a[:,5]==0]

c=np.where(a[:,5]==0)
g=c[0]
len(g)




for i in range(len(bb)):
    a1=cordId[cordId.iloc[:,0]==bb[i,0]]
    b1=cordId[cordId.iloc[:,0]==bb[i,1]]
    html='http://api.map.baidu.com/direction/v1?mode=driving&origin='+str(a1.iloc[0,2])+','+str(a1.iloc[0,1])+'&destination='+str(b1.iloc[0,2])+','+str(b1.iloc[0,1])+'&origin_region=深圳&destination_region=深圳&output=json&coord_type=wgs84&ak=KNZIT83bDR7X4AwUyrxxELh96RtR1Svq'
    try :
        response=urllib2.urlopen(html,timeout=3)
        a=response.read()
        b=json.loads(a)
        if b['status']==0:
            bb[i,2]=b['result']['routes'][0]['distance']
            bb[i,3]=b['result']['routes'][0]['duration']
    except Exception, e:
        print str(e)
for i in range(len(g)):
    a[g[i],2]=bb[i,2]
    a[g[i],3]=bb[i,3]
                
            
np.savetxt('D:/a.csv',a,delimiter=',')           
            
tt=pd.DataFrame(a)       
            
            
            
            
            