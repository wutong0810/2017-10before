# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:37:57 2017

@author: wutongshu
"""


import urllib2
import json
import pandas as pd
import numpy as np
import json
import sys





#def loadDict(path1=r'D:\常德市.txt'):
#    path2=unicode(path1,"utf8") 
#    with open(path2,'r') as load_f:
#        load_dict = json.load(load_f)
#    return load_dict


#import datetime
#starttime = datetime.datetime.now()


def getCording(path1=r'D:\常德市.txt',path3=r'D:\changde.txt'):
    path2=unicode(path1,"gbk") 
    with open(path2,'r') as load_f:
        load_dict = json.load(load_f)
    for i in range(len(load_dict)):
        for j in range(len(load_dict[i]['points'])):
            y=load_dict[i]['points'][j]['lat']
            x=load_dict[i]['points'][j]['lng']
            html='http://api.map.baidu.com/geoconv/v1/?coords='+str(x)+','+str(y)+'&from=1&to=5&ak=KNZIT83bDR7X4AwUyrxxELh96RtR1Svq'
            attempts=0
            success=False
            while attempts<3 and not success:
                try:
                    print 'finished'+'%2.1f'%(i/float(len(load_dict))*100)+'%'
                    success=True
                    response=urllib2.urlopen(html,timeout=5)
                    a=response.read()
                    b=json.loads(a)
                    if b['status']==0:
                       load_dict[i]['points'][j]['lat']=2*y-b['result'][0]['y']
                       load_dict[i]['points'][j]['lng']=2*x-b['result'][0]['x']
                except Exception, e:
                    attempts+=1
                    if attempts==3:
                        break
    #                print 'something wrong'
        for t in range(len(load_dict[i]['stops'])):
            y=load_dict[i]['stops'][t]['position']['lat']
            x=load_dict[i]['stops'][t]['position']['lng']
            html='http://api.map.baidu.com/geoconv/v1/?coords='+str(x)+','+str(y)+'&from=1&to=5&ak=KNZIT83bDR7X4AwUyrxxELh96RtR1Svq'
            attempts=0
            success=False
            while attempts<3 and not success:
                try:
                    success=True
        #            print 'finished'+'%2.1f'%(i/float(len(load_dict))*100)+'%'
                    response=urllib2.urlopen(html,timeout=5)
                    a=response.read()
                    b=json.loads(a)
                    if b['status']==0:
                       load_dict[i]['stops'][t]['position']['lat']=2*y-load_dict[i]['stops'][t]['position']['lat']
                       load_dict[i]['stops'][t]['position']['lng']=2*x-load_dict[i]['stops'][t]['position']['lng']
                except Exception, e:
                        attempts+=1
                        if attempts==3:
                            break
    path4=unicode(path3,"gbk") 
    with open(path4, 'w') as json_file:
        json_file.write(json.dumps(load_dict))
        
        
        
getCording(path1=sys.argv[1],path3=sys.argv[2])
        
        
        
        
        
        
        
        
        
        
#endtime = datetime.datetime.now()
#print endtime-starttime
#1.237s        
#    
#            
#aa=json.dumps(load_dict)
#aa
#
#
#with open(r'D:/changde.txt', 'w') as json_file:
#    json_file.write(json.dumps(load_dict))
#
#
#    
#html='http://api.map.baidu.com/direction/v1?mode=driving&origin='+str(cordId.iloc[i,2])+','+str(cordId.iloc[i,1])+'&destination='+str(cordId.iloc[j,2])+','+str(cordId.iloc[j,1])+'&origin_region=深圳&destination_region=深圳&output=json&coord_type=wgs84&ak=KNZIT83bDR7X4AwUyrxxELh96RtR1Svq'
#        try:
#            print 'finished'+'%2.1f'%((j+i*len(cordId))/float(num)*100)+'%'
#            response=urllib2.urlopen(html,timeout=5)
#            a=response.read()
#            b=json.loads(a)
#            if b['status']==0:
#                distance[i*len(cordId)+j,5]=1
#                distance[i*len(cordId)+j,2]=b['result']['routes'][0]['distance']
#                distance[i*len(cordId)+j,3]=b['result']['routes'][0]['duration']
#        except Exception, e:
#            print str(e)