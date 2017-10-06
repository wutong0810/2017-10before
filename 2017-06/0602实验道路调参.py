# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 20:18:41 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *





minMape,minPam,MAPE=gridSearch(train_data=train_data2,valid_data=valid_data2,pamater=range(20,300,20))









   fig, ax = plt.subplots(5,7,figsize=(6,5))
    for i in range(len(dataDeal10)):
        plt.subplot(5,7,i+1)
#        plt.plot(tt_deal_5min9_1[i][:,0],pd.Series(tt_deal_5min9_1[i][:,5]).map(stateMap),'o-',markersize=3) 
        plt.plot( tt_deal3_5min3[i][:,0], pd.Series(tt_deal3_5min3[i][:,5]).map(stateMap),'o-',markersize=3) 
#        xticks =range(0,25)
#        ax[i].set_xticks(xticks)
#        ax[i].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
        plt.xlim(0,24.1)