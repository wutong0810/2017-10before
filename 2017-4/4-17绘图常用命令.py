# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:05:37 2017

@author: wutongshu
"""
#绘图使用说明
#设置x,y label属性
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 

#中文字体设置
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False


#背景设置
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False



#图例位置设置
ax.legend(fontsize=13, bbox_to_anchor=(0.8,-0.13),ncol=3)


#整张图位置布设
plt.subplots_adjust(left=0.13, bottom=0.25, top=None,right=None)


#标题具体位置设置
ax.set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)



#公式标注
ax.text(1000, 4700, r"$y=\frac{\theta}{1-(1+i)^{-\theta}}$", fontsize=14, color="black")
ax.text(1400, 2200, r"$y=\frac{\theta}{1-(1+i)^{-\theta_0}}$", fontsize=14, color="black")



#图上加注释
plt.annotate(r"$\theta_0$", xy=(8*365, 4980), xytext=(8*365, 0),
            arrowprops=dict(facecolor='black', shrink=0.01,width=0.1,frac=0.1,headwidth=0.1,ls='--'),
            )



#图大小和排版设置
fig, ax = plt.subplots(2,1,figsize=(3.8,3.8))
#ax[0]分别画图








