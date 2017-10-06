# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 14:39:34 2017

@author: wutongshu
"""

import urllib2
import json
import pandas as pd
import numpy as np





#地区生产总值
codeList1=['D0010000','D1960000','D0500000' ]  
#人口数据
codeList2=['D0080000','D0090000','D1800000','D1810000','D1820000','D1830000','D0120000','D0130000','D0160000','D0170000']
#民生数据
codeList3=['D0230000','D2140000','D0240000','D0250000','D0270000','D0280000','D1750000','D2150000','D2160000']
#行政区划和自然资源
codeList4=['D1140000','D2310000','D1160000','D2330000','D1150000']
#城市概况
codeList5=['D0400000','D0410000','D2190000','D2230000','D2240000']
#三大产业
codeList6=['D0630000','D1250000','D2550000','D3120000','D0640000','D1290000','D1300000','D1310000','D1320000','D1460000','D0730000','D0660000','B0290000','B0300000']
#财政
codeList7=['D0470000','D0480000']
#交通运输
codeList8=['D0890000','D0920000','D0930000','D0900000','D0910000','D0940000','D0950000']





def codename(codeBegin):
    codelist=[]
    begin=int(codeBegin[1:])
    for i in range(begin+1,begin+17):
        s='%07d' % i
        codelist.append(codeBegin[0]+s)
    return codelist



def codeFinal(codelist):
    codeFinal=[]
    for i in codelist:
        codeMidum=codename(i)
        codeFinal.extend(codeMidum)
    return codeFinal
        
        
#地区生产总值       
codetotal1=codeFinal(codeList1)  
#人口数据      
codetotal2=codeFinal(codeList2) 
#民生数据
codetotal3=codeFinal(codeList3) 
#行政区划和自然资源
codetotal4=codeFinal(codeList4) 
#城市概况
codetotal5=codeFinal(codeList5) 
#三大产业
codetotal6=codeFinal(codeList6) 
#财政
codetotal7=codeFinal(codeList7) 
#交通运输
codetotal8=codeFinal(codeList8)


codeTotal=[codetotal1,codetotal2,codetotal3,codetotal4,codetotal5,codetotal6,codetotal7,codetotal8]
codeTotalFinal=[]
for i in codeTotal:
    codeTotalFinal.extend(i)
    

def search(allname,filename,stDate=2015,enDate=2016,cicode=330000):
    filename1 = unicode(filename , "utf8")
    num=len(allname)
    file1=open(filename1,'w+')
    for j,i in enumerate(allname):
        html='http://calendar.hexun.com/area/data/DiQuZhiBiao.ashx?startDate='+str(stDate)+'&endDate='+str(enDate)+'&codelist='+i+'&citycode='+str(cicode)
        print 'finished'+'%2.1f'%(j/float(num)*100)+'%'
        try:
            response=urllib2.urlopen(html,timeout=5)
            a=response.read()
            a1=eval(a[9:-1]) 
#            print i
            if a1:
                c=a1[a1.keys()[0]]['Data']
#                print c
                file1.write(a1.keys()[0]+',')
                for t in c:
                    for g in t:
#                        print g
                        file1.write(g+',')
                file1.write('\n')
        except Exception, e:
            print str(e)
            
    file1.close()
                



search(allname=codeTotalFinal,filename=r'D:\Data\数据\2017-07\20170704铁四院经调\20170706杭临绩项目\浙江数据.txt',stDate=2000,enDate=2016,cicode=330000)

#search(allname=codeTotalFinal,filename=r'D:\Data\数据\2017-07\20170704铁四院经调\20170712温福铁路经调\福建数据.txt',stDate=2000,enDate=2016,cicode=350000)





















#
#def search(allname,stDate=2015,enDate=2016,cicode=330000):
#    data=np.zeros((len(allname),2*(enDate-stDate)+3))
#    data1=pd.DataFrame(data)
#    for j,i in enumerate(allname):
#        html='http://calendar.hexun.com/area/data/DiQuZhiBiao.ashx?startDate='+str(stDate)+'&endDate='+str(enDate)+'&codelist='+i+'&citycode='+str(cicode)
#
##        print html
#        try:
#            response=urllib2.urlopen(html)
#            a=response.read()
#            a1=eval(a[9:-1]) 
#            if a1:
#                data1.iloc[j,0]=a1.keys()[0]
#                c=a1[a1.keys()[0]]['Data']
#                for t in c:
#                    for g in t:
#                        print g
##                if len(c)>1:
##                    data1.iloc[j,1]=c[0][0]
##                    data1.iloc[j,2]=c[0][1]
##                    data1.iloc[j,3]=c[1][0]
##                    data1.iloc[j,4]=c[1][1]
##                else :
##                    data1.iloc[j,3]=c[0][0]
##                    data1.iloc[j,4]=c[0][1]
#        except urllib2.URLError, e:
#            print e.reason
#    return data1



























































