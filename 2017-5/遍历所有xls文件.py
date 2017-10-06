# -*- coding: utf-8 -*-
"""
Created on Mon May 08 11:11:07 2017

@author: Administrator
"""
#输入大的文件夹名path1，程序会搜索所有的子文件名，并写入一个csv文件并解码，csv_filename为写入文件名
import xlrd

import xlwt
import csv
import sys
from datetime import date,datetime        
import os
path1=r'F:\萧山卡口流量0410-0416'
path2=unicode(path1,"utf8")
filename_total=[]
for dirpath, dirnames, filenames in os.walk(path2):
    for filename in filenames:
        if os.path.splitext(filename)[1]=='.xls':
            filename2=os.path.join(dirpath,filename)
#            print filename2
            filename_total.append(filename2)      
            
csv_filename=r'd:/1.csv' 
csv_file = file(csv_filename, 'wb')
csv_file_writer = csv.writer(csv_file)       
for filename in filename_total:           
    try:    
        workbook = xlrd.open_workbook(filename,encoding_override="utf-8")   
        sheet2 = workbook.sheet_by_index(0)   
        for row in xrange(0, sheet2.nrows):
            rows = sheet2.row_values(row)
            row_container = []
            for cell in rows:
                if type(cell) == unicode:
                    row_container.append(cell.encode('utf8'))
                else:
                    row_container.append(str(cell))
            csv_file_writer.writerow(row_container)
    except Exception as e:
            print(e)
            print ('错误文件')+filename
csv_file.close()     
