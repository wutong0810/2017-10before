# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:58:15 2017

@author: wutongshu
"""

from pandasql import sqldf, load_meat, load_births
pysqldf = lambda q: sqldf(q, globals())
meat = load_meat()
births = load_births()
pysqldf("SELECT * FROM med_deal2")
