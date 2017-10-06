# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:12:13 2017

@author: wutongshu
"""

import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.plot([1,2,3],[10,-10,30])



import pickle
pickle.dump(fig, open('FigureObject.fig.pickle', 'wb')) 


import pickle
figx = pickle.load(open('FigureObject.fig.pickle', 'rb'))

figx.show()
 # Show the figure, edit it, etc.!
 
 
 
import numpy as np
import matplotlib.pyplot as plt
import pickle as pl

# Plot simple sinus function
fig_handle = plt.figure()
x = np.linspace(0,2*np.pi)
y = np.sin(x)
plt.plot(x,y)

# Save figure handle to disk
pl.dump(fig_handle,file('sinus.pickle','w'))










import matplotlib.pyplot as plt
import pickle as pl
import numpy as np

# Load figure from disk and display
fig_handle = pl.load(open('sinus.pickle','rb'))
fig_handle.show()