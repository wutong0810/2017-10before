# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:00:25 2017

@author: wutongshu
"""

#绘制工作日与非工作日数据
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
fig, ax = plt.subplots(figsize=(5,5))
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.plot(tt_deall_5min3[23][:,0],tt_deall_5min3[23][:,5],'--',label=u'12月27日-休息日') 
plt.plot(tt_deall_5min3[21][:,0],tt_deall_5min3[21][:,5],'-',label=u'12月25日-工作日') 
plt.subplots_adjust(left=0.2, bottom=0.15, top=0.88,right=0.93) 
plt.xlim(0,289)
plt.ylim(0,400)
plt.legend(loc=2, fontsize=16)
ax.set_xlabel(u'时间/h',fontsize=15)
xticks1=range(0,300,48)
ax.set_xticks(xticks1)
ax.set_xticklabels([ "$%d$" %(y/12) for y in xticks1], fontsize=15)
ax.set_ylabel(u'行程时间/s',fontsize=15) 
sns.despine()       
plt.savefig('d:/picture/workday.png',dpi=200) 





















#绘制数据预处理图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(match_total_final2[11].iloc[:,1],match_total_final2[11].iloc[:,9],s=8)
ax.set_xlabel(u'时间/s',fontsize=13)
ax.set_ylabel(u'行程时间/s',fontsize=13)
plt.subplots_adjust(left=0.13, bottom=0.18, top=0.9,right=None,hspace=0.53)
#ax.set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
sns.despine() 
plt.savefig('d:/picture/data_oral.png',dpi=200) 






#绘制数据预处理图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(tt_deall[11].iloc[:,1],tt_deall[11].iloc[:,8],s=8)
ax.set_xlabel(u'时间/s',fontsize=13)
ax.set_ylabel(u'行程时间/s',fontsize=13)
plt.subplots_adjust(left=0.13, bottom=0.18, top=0.9,right=None,hspace=0.53)
#ax.set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
sns.despine() 
plt.savefig('d:/picture/data_deal.png',dpi=200) 

















#时空相关性图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(7,6))
ax.plot(np.arange(1,22),cc.iloc[:,1], label=r"$TT_{t-5}$", lw=1.5, ls='-', marker='o', markersize=10)
ax.plot(np.arange(1,22),cc.iloc[:,2], label=r"$TT_{t-4}$", lw=1.5, ls='-', marker='<', markersize=10)
ax.plot(np.arange(1,22),cc.iloc[:,3],label=r"$TT_{t-3}$", lw=1.5, ls='-', marker='s', markersize=10)
ax.plot(np.arange(1,22),cc.iloc[:,4],label=r"$TT_{t-2}$", lw=1.5, ls='-', marker='D', markersize=10)
ax.plot(np.arange(1,22),cc.iloc[:,5],label=r"$TT_{t-1}$", lw=1.5, ls='-', marker='*', markersize=10)
ax.legend(fontsize=14, bbox_to_anchor=(0.8,-0.15),ncol=3)
ax.set_xlabel(u'天数',fontsize=14)
ax.set_ylabel(u'相关性',fontsize=14)
xticks =range(1,22)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
yticks =np.arange(0.3,1,0.1)
plt.ylim(0.3,1)
plt.subplots_adjust(left=0.15, bottom=0.25, top=None,right=None)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=13)
sns.despine()  
plt.savefig('d:/picture/time_corrl.png',dpi=200) 



#分开画图
import matplotlib as mpl
mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=13) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(np.arange(21),cc.iloc[:,6], label="up_t-4",  lw=2, ls='-', marker='o', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,7], label="up_t-3",  lw=2, ls='-', marker='<', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,8],label="up_t-2",  lw=2, ls='-', marker='s', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,9],label="up_t-1",  lw=2, ls='-', marker='D', markersize=10)
ax.legend(fontsize=12, bbox_to_anchor=(0.8,-0.12),ncol=2)
#ax.legend(loc=2,fontsize=12)
ax.set_xlabel(u'天数',fontsize=14)
ax.set_ylabel(u'相关性',fontsize=14)
#ax[0].set_title(u'（a）上游路段与当前路段的相关性',position=(0.5,-0.43),fontsize=13)
xticks =range(1,22)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
plt.subplots_adjust(left=0.15, bottom=0.20, top=None,right=None,hspace=0.5)
sns.despine() 
plt.savefig('d:/picture/spatical_up.png',dpi=200) 




























#绘图过程
#绘制c=1,回归树的棵树变化关系
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
markers=['o','s','D','*','^']
plt.subplots_adjust(left=0.2, bottom=0.15, top=None,right=None,hspace=0.5)
for i in range(5):
        c=mape1[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,marker=markers[i])
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize=12)
#        plt.title(u'C=1',fontsize=13)
        sns.despine()  
        ax.set_xlabel(u'树的棵树M',fontsize=13)
        ax.set_ylabel('MAPE',fontsize=13)
plt.savefig('d:/picture/C1.png',dpi=200)



#绘制c=4,回归树的棵树变化关系
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
markers=['o','s','D','*','^']
plt.subplots_adjust(left=0.2, bottom=0.15, top=None,right=None,hspace=0.5)
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        ax.plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000],c2,marker=markers[i])
        plt.legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize=12)
#        plt.title(u'C=1',fontsize=13)
        sns.despine()  
        ax.set_xlabel(u'树的棵树M',fontsize=13)
        ax.set_ylabel('MAPE',fontsize=13)
plt.savefig('d:/picture/c4.png',dpi=200) 



#分开画绘制，学习率变化图，c=1
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
plt.subplots_adjust(left=0.18, bottom=0.3)
markers=['o','s','D','*','^','p']
for i in range(6):
        c=mape4[i,:]
        c2=c
#        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=12, bbox_to_anchor=(1.1,-0.20),ncol=3)
#        ax.set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)
        ax.set_xlabel(u'学习率lr',fontsize=13)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax.set_ylabel('MAPE',fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/lr1.png',dpi=200) 

#学习率变化图，c=4
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
plt.subplots_adjust(left=0.18, bottom=0.3)
markers=['o','s','D','*','^','p']
for i in range(6):
        c=mape5[i,:]
        c2=c
#        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=12, bbox_to_anchor=(1.1,-0.20),ncol=3)
#        ax.set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)
        ax.set_xlabel(u'学习率lr',fontsize=13)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax.set_ylabel('MAPE',fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/lr4.png',dpi=200)




#学习深度lr=0.5
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
plt.subplots_adjust(left=0.18, bottom=0.25, top=0.9,right=None,hspace=0.58)
markers=['o','s','D']
for i in range(3):
        c=mape6[i,:]
        c2=c
#        plt.ylim(0.02,0.35)
        c1=np.arange(4)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1000','M-2000','M-8000'],fontsize=12, bbox_to_anchor=(1.15,-0.20),ncol=3)
#        ax.set_title(u'（a）学习率lr=0.5',position=(0.5,-0.50),fontsize=14)
        ax.set_xlabel(u'学习深度C',fontsize=13)
        ax.set_xticks(range(4))
        ax.set_xticklabels([1,2,3,4], fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/c-1.png',dpi=200) 

#学习深度lr=0.005
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(3.8,3.8))
plt.subplots_adjust(left=0.18, bottom=0.25, top=0.9,right=None,hspace=0.58)
markers=['o','s','D']
for i in range(3):
        c=mape7[i,:]
        c2=c
#        plt.ylim(0.02,0.35)
        c1=np.arange(4)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1000','M-2000','M-8000'],fontsize=12, bbox_to_anchor=(1.15,-0.20),ncol=3)
#        ax.set_title(u'（a）学习率lr=0.5',position=(0.5,-0.50),fontsize=14)
        ax.set_xlabel(u'学习深度C',fontsize=13)
        ax.set_xticks(range(4))
        ax.set_xticklabels([1,2,3,4], fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/c-2.png',dpi=200)




