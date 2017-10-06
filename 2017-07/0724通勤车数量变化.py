# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:09:26 2017

@author: wutongshu
"""

import pandas as pd
data=pd.read_csv(r'C:\Users\wutongshu\Desktop\car_commute.csv')






plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
cmap=sns.light_palette("navy",as_cmap = True)
#cmap=sns.cubehelix_palette(rot=-.0)
#cmap=sns.color_palette("Blues",as_cmap = True)
aa=data.pivot("DAYS", "HOURS", "COUNT")
aa.index=range(len(aa))
f, ax = plt.subplots(figsize=(16, 9))
sns.heatmap(aa, annot=True, fmt="d", cmap=cmap,ax=ax)
ax.set_xlabel(u'时间（单位：小时）')
ax.set_ylabel(u'工作日（单位：天）')
plt.savefig('d:/workday2.png',dpi=200) 