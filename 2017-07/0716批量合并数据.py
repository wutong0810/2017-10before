# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:36:24 2017

@author: wutongshu
"""

import os
#获取目标文件夹的路径

def pathGet(path1=r'E:\华为数据\测试',dataFomat='.txt'):
    path2=unicode(path1,"utf8")
    filename_total=[]
    for dirpath, dirnames, filenames in os.walk(path2):
        for filename in filenames:
            if os.path.splitext(filename)[1]==dataFomat:
                filename2=os.path.join(dirpath,filename)
    #            print filename2
                filename_total.append(filename2) 
    return filename_total







import pandas as pd
def txtTotal(filename_total,path1=r'E:\华为数据\test1.txt'):
    c=[]
    path2=unicode(path1,"utf8")        
    #先遍历文件名
    n=len(filename_total)
    i=0
    for filename in filename_total:
        #遍历单个文件，读取行数
        i=i+1
    #    print 'finished'+'%2.1f'%(i/float(n)*100)+'%'
        if os.path.getsize(filename):
            try:
                a=pd.read_csv(filename,header=None)
                a2=a.iloc[:,[0,1,2,3,5,7,8,9,11,14,15,17]]
                a2.to_csv(path2,index=False,header=None,mode='a',encoding='gbk')
            except :
                c.append(filename)
    return c













os.chdir(r'E:\huawei\huaweiData')
os.getcwd()
dir1=[os.path.join('E:\huawei\huaweiData', x) for x in os.listdir('.') if os.path.isdir(x)]
dir2=[os.path.join('E:\huawei\huaweiData',(x+'.txt')) for x in os.listdir('.') if os.path.isdir(x)]

import datetime
starttime = datetime.datetime.now()
g=[]
for i in range(len(dir1)):
    filename_total1=pathGet(dir1[i])
    c=txtTotal(filename_total=filename_total1,path1=dir2[i])
    g.append(c)
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds