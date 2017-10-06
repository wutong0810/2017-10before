# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cx_Oracle
db=cx_Oracle.connect('hiatmp/hiatmp@orcl')
print db.version
db.close()
