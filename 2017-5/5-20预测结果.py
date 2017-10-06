# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:16:38 2017

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append(r'F:\python_script\2017-5\predict')
from all_func import *


























        
gbm0 = GradientBoostingRegressor(n_estimators=360,min_samples_split=50,
                                  min_samples_leaf=20,max_depth=13,max_features='sqrt')    
gbm0.fit(train_x,train_y)  