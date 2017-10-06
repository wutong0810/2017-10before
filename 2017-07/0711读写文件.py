# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:51:38 2017

@author: wutongshu
"""
import os
#获取目标文件夹的路径


path1=r'E:\华为数据\6'
path2=unicode(path1,"utf8")
filename_total=[]
for dirpath, dirnames, filenames in os.walk(path2):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.txt':
            filename2=os.path.join(dirpath,filename)
#            print filename2
            filename_total.append(filename2) 
     
        
#path1=r'E:\华为数据\6\rImport_ysb_201705050001_01_1.txt'
#path2=unicode(path1,"utf8")        
#
#f=open(path2,'w')
##先遍历文件名
#for filename in filename_total:
#    #遍历单个文件，读取行数
#    if os.path.getsize(filename):
#        print os.path.getsize(filename)
#        with open(filename) as g:
#            f.write(g.read())
#            f.write('\n')
###关闭文件
#f.close()





#import numpy as np
#a=np.loadtxt(path2,dtype=str,delimiter=',',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))

#解释下啦
#第1行数据车牌1，第二行车牌2，第3行车牌类型1，第4行车牌类型2，第6行车牌识别时间，第8行检测点id，第9行
#进出口类型，第10行车道id，第11行颜色，第12行类型，
#第13,14,15行车标 信息卡编码 违法类型 
#第16,17,18列速度 前端id 行驶方向




0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18


c=[]
path1=r'E:\华为数据\data0505.txt'
path2=unicode(path1,"utf8")        
path3=r'E:\华为数据\6\med.txt'
path4=unicode(path3,"utf8")
f=open(path2,'w')
#先遍历文件名
n=len(filename_total)
i=0
for filename in filename_total:
    #遍历单个文件，读取行数
    i=i+1
    print 'finished'+'%2.1f'%(i/float(n)*100)+'%'
    if os.path.getsize(filename):
#        print os.path.getsize(filename)
        try:
            a=np.loadtxt(filename,dtype=str,delimiter=',',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18))
            np.savetxt(path4,a,fmt='%s',delimiter=',')
            with open(path4) as g:
                f.write(g.read())
                f.write('\n')
        except :
            c.append(filename)
##关闭文件
f.close()
















