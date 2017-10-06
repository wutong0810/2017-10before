# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:29:16 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
i=0.113/365
theda_0=8*365

#定义函数
def fun(x):
    y=x/(1-math.pow((1+i),-x))
    return y
    
#画段1
x1=np.arange(100,8*365,0.5)
y1=np.zeros((len(x1),1))
for j in range(len(x1)):
    y1[j]=fun(x1[j])
#画段2
x2=np.arange(8*365,6000,0.5)
y2=np.zeros((len(x2),1))
for j in range(len(x2)):
    y2[j]=fun(x2[j])



#画段3
x3=np.arange(100,8*365,0.5)
y3=x3/(1-math.pow((1+i),-365*8))
#画段4
x4=np.arange(8*365,6000,0.5)
y4=x4/(1-math.pow((1+i),-365*8))
#画渐近线5
x5=np.arange(100,6000,0.5)
y5=0.5*x5+1/(np.log(1+i))
#画渐进线6
x6=np.arange(100,6000,0.5)
y6=x6





fig,ax = plt.subplots(figsize=(6,6))
plt.plot(x1,y1,ls='-',lw=3,color='blue')
plt.plot(x2,y2,ls='-.',lw=1.5,color='blue',alpha=0.5)
plt.plot(x3,y3,ls='-.',lw=1.5,color='red',alpha=0.5)
plt.plot(x4,y4,ls='-',lw=3,color='red')
plt.plot(x5,y5,ls='--',lw=0.8,color='black')
#plt.plot(x6,y6,ls='--',lw=0.8,color='black')
plt.text(4500, 5300, r"$y=0.5*\theta+\frac{1}{\ln (1+i)}$", fontsize=14, color="black")
#ax.text(4500, 4000, r"$y=\theta$", fontsize=14, color="black")
ax.text(1000, 4700, r"$y=\frac{\theta}{1-(1+i)^{-\theta}}$", fontsize=14, color="black")
plt.text(1400, 2200, r"$y=\frac{\theta}{1-(1+i)^{-\theta_0}}$", fontsize=14, color="black")
ax.text(4000, 8500, r"$y=f(\theta)*\frac{m}{iC_b}$", fontsize=14, color="black")
#plt.text(8*365, 0, r"$\theta_0$", fontsize=14, color="black")
ax.set_xlabel(r"$\theta$",fontsize=13)
ax.set_ylabel('y',fontsize=13)
plt.annotate(r"$\theta_0$", xy=(8*365, 4980), xytext=(8*365, 0),
            arrowprops=dict(facecolor='black', shrink=0.01,width=0.1,frac=0.1,headwidth=0.1,ls='--'),
            )
plt.xlim(0,6000)
plt.ylim(0,10000)
sns.despine() 



#fig, ax = plt.subplots(figsize=(6,6))
#
##ax.plot(xx, xx**2, xx, xx**3)
#
#ax.text(0.95, 0.2, r"$y=x^2$", fontsize=20, color="blue")
#ax.text(0.85, 0.1, r"$y=x^3$", fontsize=20, color="green");
#
#
#
#
#fig,ax = plt.subplots(figsize=(6,6))
#plt.plot(x1,y1,ls='-',lw=1.5,color='blue')
#ax.text(5000, 5000, r"$y=x^2$", fontsize=20, color="blue")
#ax.text(0.85, 0.1, r"$y=x^3$", fontsize=20, color="green");







