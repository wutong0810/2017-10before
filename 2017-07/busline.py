# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:27:13 2017

@author: wutongshu
"""

import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
import urllib
import urllib2
import codecs
headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

def cityLine(cityName='guangzhou'):
    urlAll=[]
    for i in range(20):
        a='http://'+str(cityName)+'.8684.cn/line'+str(i+1)
        urlAll.append(a)
    return urlAll


#urllib2.urlopen(all_url, timeout=1).read() is None
import sys
def busLine(filename=r'D:\ 1.txt',cityName='guangzhou'):
    
    urlAll=cityLine(cityName)
    filename1 = unicode(filename , "utf8")
    file1=codecs.open(filename1,'w+','utf-8')
    for i in range(20):
        url=urlAll[i]
        start_html = requests.get(url, headers=headers)
        try:
            Soup = BeautifulSoup(start_html.text, 'lxml')
            a=Soup.find_all(class_='stie_nav_name')
    #        print a[i].get_text()+'/n'
            file1.write('\n'+a[i].get_text()+'\n')
            b=Soup.findAll('div',class_='stie_list')[0].findAll('a')
            for j in b:
    #            print j.get_text()+','
                file1.write('\''+j.get_text()+'\''+',')
        except Exception, e:
            pass
    file1.close()






busLine(filename=sys.argv[1],cityName=sys.argv[2])