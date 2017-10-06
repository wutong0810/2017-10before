# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 09:51:10 2017

@author: wutongshu
"""






E:\huaweiData\16\rImport_ysb_201705161731_01_6.txt





import pandas as pd
pd.read_csv(r'E:\errData\rImport_ysb_201705161731_01_6.txt')
E:\huaweiData\24\rrImport_ysb_201705241801_01_9.txt




import json

#读取json文件
path1=r'D:\历史文件管理\2017-07\0720\1.json'
path2=unicode(path1,"utf8") 
with open(path2,'r') as load_f:
    load_dict = json.load(load_f)
    
    
    
import json

#读取json文件
path1=r'D:\历史文件管理\2017-07\0720\2.json'
path2=unicode(path1,"utf8") 
with open(path2,'r') as load_f:
    load_dict2 = json.load(load_f)
    
    
import json

#读取json文件
path1=r'D:\历史文件管理\2017-07\0720\3.json'
path2=unicode(path1,"utf8") 
with open(path2,'r') as load_f:
    load_dict3 = json.load(load_f)