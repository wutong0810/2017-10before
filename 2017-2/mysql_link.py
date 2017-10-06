# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 12:06:29 2017

@author: wutongshu
"""

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE scraping")
cur.execute("SELECT * FROM pages WHERE id=1")
a=cur.fetchall()
print a

cur.close()
conn.close()