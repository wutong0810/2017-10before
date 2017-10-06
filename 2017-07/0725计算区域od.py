# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:33:21 2017

@author: wutongshu
"""

import pandas as pd
data=pd.read_csv(r'd:/PA_mat.csv',header=None)
import numpy as np
data2=np.zeros((247*247,3))


for i in range(1,247):
    for j in range(1,247):
        
        data2[i*247+j,0]=data.iloc[i,0]
        data2[i*247+j,1]=data.iloc[0,j]
        data2[i*247+j,2]=data.iloc[i,j]

data3=pd.read_csv(r'd:/12.csv')
