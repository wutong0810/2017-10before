# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:46:30 2017

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
plt.subplots_adjust(left=0.15, bottom=0.14, top=0.88,right=0.93) 
plt.xlim(0,289)
plt.ylim(0,500)
plt.legend(loc=2, fontsize=13)
ax.set_xlabel(u'时间',fontsize=13)
ax.set_ylabel(u'行程时间/(s)',fontsize=13) 
sns.despine()       
plt.savefig('d:/picture/workday.png',dpi=200) 






ax.set_xticklabels(fontsize=18) 
ax.set_xscale(fontsize=13) 
ax.set_xticks(fontsize=13)
ax.set_yticks(fontsize=13)



#, color="purple"
#, color="blue"
#, color="red"
#, color="orange"
#, color="green"
#,alpha=0.9
#,alpha=0.9
#,alpha=0.9
#,alpha=0.9
#,alpha=0.9

#时空相关性图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(6,5))
ax.plot(np.arange(1,22),cc.iloc[:,1], label="t-5", lw=1.5, ls='-', marker='o', markersize=12)
ax.plot(np.arange(1,22),cc.iloc[:,2], label="t-4", lw=1.5, ls='-', marker='<', markersize=12)
ax.plot(np.arange(1,22),cc.iloc[:,3],label="t-3", lw=1.5, ls='-', marker='s', markersize=12)
ax.plot(np.arange(1,22),cc.iloc[:,4],label="t-2", lw=1.5, ls='-', marker='D', markersize=12)
ax.plot(np.arange(1,22),cc.iloc[:,5],label="t-1", lw=1.5, ls='-', marker='*', markersize=12)
ax.legend(fontsize=13, bbox_to_anchor=(0.8,-0.12),ncol=3)
ax.set_xlabel(u'天数',fontsize=13)
ax.set_ylabel(u'相关性',fontsize=13)
xticks =range(1,22)
ax.set_xticks(xticks)
ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
yticks =np.arange(0.3,1,0.1)
plt.ylim(0.3,1)
plt.subplots_adjust(left=None, bottom=0.20, top=None,right=None)
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=12)
sns.despine()  
plt.savefig('d:/picture/workday2.png',dpi=200) 






#绘制数据预处理图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(2,1,figsize=(6,5))
ax[0].scatter(match_total_final2[11].iloc[:,1],match_total_final2[11].iloc[:,9],s=8)
ax[0].set_xlabel(u'时间',fontsize=13)
ax[0].set_ylabel(u'行程时间(s)',fontsize=13)
plt.subplots_adjust(left=None, bottom=0.15, top=0.9,right=None,hspace=0.53)
ax[0].set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
sns.despine() 
ax[1].scatter(tt_deall[11].iloc[:,1],tt_deall[11].iloc[:,8],s=8)
ax[1].set_xlabel(u'时间',fontsize=13)
ax[1].set_ylabel(u'行程时间(s)',fontsize=13)
ax[1].set_title(u'（b）数据预处理后',position=(0.5,-0.53),fontsize=13)
sns.despine() 
plt.savefig('d:/picture/datadeal.png',dpi=200) 










#绘制空间相关性图
#绘制空间相关性图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(2,1,figsize=(6,9))
ax[0].plot(np.arange(21),cc.iloc[:,6], label="up_t-4",  lw=2, ls='-', marker='o', markersize=10)
ax[0].plot(np.arange(21),cc.iloc[:,7], label="up_t-3",  lw=2, ls='-', marker='<', markersize=10)
ax[0].plot(np.arange(21),cc.iloc[:,8],label="up_t-2",  lw=2, ls='-', marker='s', markersize=10)
ax[0].plot(np.arange(21),cc.iloc[:,9],label="up_t-1",  lw=2, ls='-', marker='D', markersize=10)
ax[0].legend(fontsize=12, bbox_to_anchor=(1.1,-0.18),ncol=4)
ax[0].set_xlabel(u'天数',fontsize=12)
ax[0].set_ylabel(u'相关性',fontsize=12)
ax[0].set_title(u'（a）上游路段与当前路段的相关性',position=(0.5,-0.43),fontsize=13)
xticks =range(1,22)
ax[0].set_xticks(xticks)
plt.subplots_adjust(left=0.15, bottom=0.20, top=None,right=None,hspace=0.5)
sns.despine() 



ax[1].plot(np.arange(21),cc.iloc[:,10], label="down_t-4",  lw=2, ls='-', marker='*', markersize=10)
ax[1].plot(np.arange(21),cc.iloc[:,11], label="down_t-3", lw=2, ls='-', marker='v', markersize=10)
ax[1].plot(np.arange(21),cc.iloc[:,12],label="down_t-2",  lw=2, ls='-', marker='^', markersize=10)
ax[1].plot(np.arange(21),cc.iloc[:,13],label="down_t-1",  lw=2, ls='-', marker='p', markersize=10)
ax[1].legend(fontsize=12, bbox_to_anchor=(1.1,-0.18),ncol=4)
ax[1].set_xlabel(u'天数',fontsize=12)
ax[1].set_ylabel(u'相关性',fontsize=12)
ax[1].set_title(u'（b）下游路段与当前路段的相关性',position=(0.5,-0.43),fontsize=13)
xticks =range(1,22)
ax[1].set_xticks(xticks)
#plt.subplots_adjust(left=None, bottom=0.20, top=None,right=None)
#plt.ylim(0.2,0.7)
#ax[1].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
sns.despine() 
#yticks =np.arange(0,1,0.1)
#ax.set_yticks(yticks)
#ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=12)
plt.savefig('d:/picture/spatical.png',dpi=200) 





#分开画图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(7,6))
ax.plot(np.arange(21),cc.iloc[:,6], label="up_t-4",  lw=2, ls='-', marker='o', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,7], label="up_t-3",  lw=2, ls='-', marker='<', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,8],label="up_t-2",  lw=2, ls='-', marker='s', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,9],label="up_t-1",  lw=2, ls='-', marker='D', markersize=10)
ax.legend(fontsize=12, bbox_to_anchor=(0.8,-0.12),ncol=2)
#ax.legend(loc=2,fontsize=12)
ax.set_xlabel(u'天数',fontsize=13)
ax.set_ylabel(u'相关性',fontsize=13)
#ax[0].set_title(u'（a）上游路段与当前路段的相关性',position=(0.5,-0.43),fontsize=13)
xticks =range(1,22)
ax.set_xticks(xticks)
plt.subplots_adjust(left=0.15, bottom=0.20, top=None,right=None,hspace=0.5)
sns.despine() 
plt.savefig('d:/picture/spatical_up.png',dpi=200) 





sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(5,5))
ax.plot(np.arange(21),cc.iloc[:,10], label="down_t-4",  lw=2, ls='-', marker='*', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,11], label="down_t-3", lw=2, ls='-', marker='v', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,12],label="down_t-2",  lw=2, ls='-', marker='^', markersize=10)
ax.plot(np.arange(21),cc.iloc[:,13],label="down_t-1",  lw=2, ls='-', marker='p', markersize=10)
ax.legend(fontsize=12, bbox_to_anchor=(0.8,-0.12),ncol=2)
ax.set_xlabel(u'天数',fontsize=12)
ax.set_ylabel(u'相关性',fontsize=12)
#ax.set_title(u'（b）下游路段与当前路段的相关性',position=(0.5,-0.43),fontsize=13)
xticks =range(1,22)
ax.set_xticks(xticks)
#plt.subplots_adjust(left=None, bottom=0.20, top=None,right=None)
#plt.ylim(0.2,0.7)
#ax[1].set_xticklabels(["$%d$" % y for y in xticks], fontsize=12)
plt.subplots_adjust(left=0.15, bottom=0.18, top=None,right=None,hspace=0.5)
sns.despine() 
#yticks =np.arange(0,1,0.1)
#ax.set_yticks(yticks)
#ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=12)
plt.savefig('d:/picture/spatical_down.png',dpi=200) 


















#c=3时
mape3=np.zeros((5,18))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000,1500,2000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=3, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape3[z,i]=c1

#c=1时
mape1=np.zeros((5,18))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000,1500,2000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape1[z,i]=c1













        
        
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(2,1,figsize=(5,8))
plt.subplots_adjust(left=0.16, bottom=0.16, top=None,right=None,hspace=0.4)
markers=['o','s','D','*','^']
for i in range(5):
        c=mape1[i,:]
        c2=c
        plt.ylim(0.06,0.30)
        ax[0].plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000,1500,2000],c2,marker=markers[i])
        ax[0].legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize=12)
        ax[0].set_title(u'（a）C=1',position=(0.5,-0.35),fontsize=13)
        sns.despine()  
        ax[0].set_xlabel(u'树的棵树M',fontsize=13)
        ax[0].set_ylabel('MAPE',fontsize=13)
        sns.despine() 
for i in range(5):
        c=mape3[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        ax[1].plot([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000,1500,2000],c2,marker=markers[i])
        ax[1].legend(['lr-0.5','lr-0.1','lr-0.05','lr-0.01','lr-0.005'],loc=1, fontsize=12)
        ax[1].set_title(u'（b）C=3',position=(0.5,-0.35),fontsize=13)
        sns.despine()  
        ax[1].set_xlabel(u'树的棵树M',fontsize=13)
        ax[1].set_ylabel('MAPE',fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/c3.png',dpi=200)      




#c=1，调整学习率
mape4=np.zeros((6,6))

for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape4[i,z]=c1        



#c=4，调整学习率
mape5=np.zeros((6,6))
for i,j in enumerate([1,100,200,400,800,1000]):
    for z,h in enumerate([0.005,0.01,0.05,0.1,0.5,1]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=4, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        aa1=np.hstack([y_test.reshape(-1,1), gbm0.predict(X_test).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape5[i,z]=c1 
        
        
        
#绘制学习率变化图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(2,1,figsize=(5,8))
plt.subplots_adjust(left=0.18, bottom=0.16, top=0.9,right=None,hspace=0.63)
markers=['o','s','D','*','^','p']
for i in range(6):
        c=mape4[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax[0].plot(c1,c2,marker=markers[i])
        ax[0].legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
        ax[0].set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)
        ax[0].set_xlabel(u'学习率',fontsize=13)
        ax[0].set_xticks(range(6))
        ax[0].set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax[0].set_ylabel('MAPE',fontsize=13)
for i in range(6):
        c=mape5[i,:]
        c2=c
        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax[1].plot(c1,c2,marker=markers[i])
        ax[1].legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
        ax[1].set_title(u'（b）C=3',position=(0.5,-0.58),fontsize=14)
        ax[1].set_xlabel(u'学习率',fontsize=13)
        ax[1].set_xticks(range(6))
        ax[1].set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax[1].set_ylabel('MAPE',fontsize=13)
plt.savefig('d:/picture/c5.png',dpi=200) 



#分开画绘制学习率变化图
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(left=0.18, bottom=0.25)
markers=['o','s','D','*','^','p']
for i in range(6):
        c=mape4[i,:]
        c2=c
#        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
#        ax.set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)
        ax.set_xlabel(u'学习率lr',fontsize=13)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax.set_ylabel('MAPE',fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/lr1.png',dpi=200) 

sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(left=0.18, bottom=0.25)
markers=['o','s','D','*','^','p']
for i in range(6):
        c=mape5[i,:]
        c2=c
#        plt.ylim(0.05,0.30)
        c1=np.arange(6)
        ax.plot(c1,c2,marker=markers[i])
        ax.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
#        ax.set_title(u'（a）C=1',position=(0.5,-0.58),fontsize=14)
        ax.set_xlabel(u'学习率lr',fontsize=13)
        ax.set_xticks(range(6))
        ax.set_xticklabels([0.005,0.01,0.05,0.1,0.5,1], fontsize=13) 
        ax.set_ylabel('MAPE',fontsize=13)
        sns.despine() 
plt.savefig('d:/picture/lr4.png',dpi=200) 




























sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(2,1,figsize=(5,8))
plt.subplots_adjust(left=0.18, bottom=0.16, top=0.9,right=None,hspace=0.58)
markers=['o','s','D']
for i in range(3):
        c=mape6[i,:]
        c2=c
#        plt.ylim(0.02,0.35)
        c1=np.arange(4)
        ax[0].plot(c1,c2,marker=markers[i])
        ax[0].legend(['M-1000','M-2000','M-8000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
        ax[0].set_title(u'（a）学习率lr=0.5',position=(0.5,-0.50),fontsize=14)
        ax[0].set_xlabel(u'学习深度C',fontsize=13)
        ax[0].set_xticks(range(4))
        ax[0].set_xticklabels([1,2,3,4], fontsize=13)    
        
for i in range(3):
        c=mape7[i,:]
        c2=c
#        plt.ylim(0.02,0.35)
        c1=np.arange(4)
        ax[1].plot(c1,c2,marker=markers[i])
        ax[1].legend(['M-1000','M-2000','M-8000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
        ax[1].set_title(u'（a）学习率lr=0.05',position=(0.5,-0.50),fontsize=14)
        ax[1].set_xlabel(u'学习深度C',fontsize=13)
        ax[1].set_xticks(range(4))
        ax[1].set_xticklabels([1,2,3,4], fontsize=13)          
plt.savefig('d:/picture/c6.png',dpi=200)    










alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T


x=np.array([0.5,0.1,0.05,0.01,0.005])
y=np.array(range(10,1010,10))
X,Y = np.meshgrid(x, y)
z=mape1
Z=z.T
fig = plt.figure(figsize=(6,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot


# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 1, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)



mape1=np.zeros((5,16))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate([1,20,30,40,60,80,100,140,200,250,300,350,400,600,800,1000]):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=3, random_state=10, loss='ls')    
        gbm0.fit(train_x,train_y) 
        aa1=np.hstack([train_y.reshape(-1,1), gbm0.predict(train_x).reshape(-1,1)])
        aa2=np.abs(aa1[:,0]-aa1[:,1])/aa1[:,0]
        aa3=np.hstack([aa1,aa2.reshape(-1,1)])
        c1=np.sum(aa3[:,2])/len(aa3)
        mape1[z,i]=c1
        
        
from sklearn.metrics import mean_squared_error

mape1=np.zeros((5,100))
for z,h in enumerate([0.5,0.1,0.05,0.01,0.005]):
    for i,j in enumerate(range(10,1010,10)):
        gbm0 = GradientBoostingRegressor(n_estimators=j, learning_rate=h, max_depth=1, random_state=10, loss='ls')    
        gbm0.fit(X_train,y_train) 
        c1=mean_squared_error(y_test,gbm0.predict(X_test))
        mape1[z,i]=c1



















# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)










gbm0 = GradientBoostingRegressor(n_estimators=180, learning_rate=0.1, max_depth=3, random_state=10, loss='ls')    
gbm0.fit(train_x,train_y)  
test_x=np.array(test_data2.iloc[:,:-1])
test_y=np.array(test_data2.iloc[:,-1])
cccc=pd.Series(gbm0.feature_importances_,['time of day','t-4','t-3','t-2','t-1',r'$\Delta$t-3',r'$\Delta$t-2',r'$\Delta$t-1','u_t-2','u_t-1','weekends']).sort_values(ascending=False)









sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(6,6))
ccc=np.array(cccc)
ax.bar(np.arange(len(ccc)),ccc)
#ax.legend(['M-1','M-100','M-200','M-400','M-800','M-1000'],fontsize=13, bbox_to_anchor=(0.95,-0.20),ncol=3)
ax.set_title(u'（b）C=3',position=(0.5,-0.58),fontsize=14)
ax.set_xticks(range(len(ccc)))
ax.set_xlabel(u'各特征向量',fontsize=13)
plt.subplots_adjust(left=0.15, bottom=0.20, top=None,right=None)
ax.set_xticklabels(['t-1','time of day','$\Delta$t-1',r'$\Delta$t-3','t-2','u_t-2',r'$\Delta$t-2','t-3','t-4','u_t-1','weekends'], fontsize=12,rotation=50) 
ax.set_ylabel(u'重要性',fontsize=13)
sns.despine() 
plt.savefig('d:/picture/c7.png',dpi=200) 


     
        
        
       
    
#预测与实际数据    
a2=plt.figure()
for i in range(7):
    a2=plt.subplot(3,3,i+1)
    test_med=test_data[i]
    test_x=np.array(test_med[:,:-1])
    test_y=np.array(test_med[:,-1])
    a2=plt.plot(range(288),test_y,'-',label=u'实际数据')
    a2=plt.plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
    a2=plt.ylim(0,750)
    a2=plt.legend(loc=2)
    
#data01=test_data[4][:,-1]
#test_x=np.array(test_data[4][:,:-1])
#data02=gbm0.predict(test_x)   
    
    
    
    
    
    
    
    

sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(3,1,figsize=(5,8))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)

test_med=test_data[0]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax[0].plot(range(288),test_y,'-',label=u'实际数据')
ax[0].plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
plt.ylim(0,500)
ax[0].legend(loc=2)
ax[0].set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax[0].set_xlabel(u'时间',fontsize=12)
ax[0].set_ylabel(u'行程时间',fontsize=12)
sns.despine() 

test_med=test_data[1]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax[1].plot(range(288),test_y,'-',label=u'实际数据')
ax[1].plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
plt.ylim(0,500)
ax[1].legend(loc=2)
ax[1].set_title(u'（b）12月26日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax[1].set_xlabel(u'时间',fontsize=12)
ax[1].set_ylabel(u'行程时间',fontsize=12)
sns.despine() 

test_med=test_data[2]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax[2].plot(range(288),test_y,'-',label=u'实际数据')
ax[2].plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
plt.ylim(0,500)
ax[2].legend(loc=2)
ax[2].set_title(u'（c）12月27日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax[2].set_xlabel(u'时间',fontsize=12)
ax[2].set_ylabel(u'行程时间',fontsize=12)
sns.despine() 
plt.savefig('d:/picture/c8.png',dpi=200) 








mpl.rc('ytick', labelsize=15) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(9,6))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[0]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',lw=1.5,label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',lw=1.5,label=u'预测数据')
plt.ylim(50,300)
ax.legend(loc=2,fontsize=16)
#ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间/h',fontsize=15)
ax.set_ylabel(u'行程时间/s',fontsize=15)
sns.despine() 
xticks1=range(0,300,48)
ax.set_xticks(xticks1)
ax.set_xticklabels([ "$%d$" %(y/12) for y in xticks1], fontsize=15)
plt.savefig('d:/picture/day25.png',dpi=200) 




import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=14) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(9,6))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[1]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',lw=1.5,label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',lw=1.5,label=u'预测数据')
plt.ylim(50,300)
##xticks1=range(0,288,12)
#ax.set_xticks(xticks1)
#ax.set_xticklabels([ "$%d$" %(y/12) for y in yticks1], fontsize=11)
ax.legend(loc=2,fontsize=16)
#ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间/h',fontsize=15)
ax.set_ylabel(u'行程时间/s',fontsize=15)
sns.despine() 
#ax.set_yticklabels(fontsize=11)
xticks1=range(0,300,48)
ax.set_xticks(xticks1)
ax.set_xticklabels([ "$%d$" %(y/12) for y in xticks1], fontsize=15)
plt.savefig('d:/picture/day26.png',dpi=200) 


import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=14) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(9,6))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[6]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',lw=1.5,label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',lw=1.5,label=u'预测数据')
plt.ylim(50,500)
##xticks1=range(0,288,12)
#ax.set_xticks(xticks1)
#ax.set_xticklabels([ "$%d$" %(y/12) for y in yticks1], fontsize=11)
ax.legend(loc=2,fontsize=16)
#ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间/h',fontsize=15)
ax.set_ylabel(u'行程时间/s',fontsize=15)
sns.despine() 
#ax.set_yticklabels(fontsize=11)
xticks1=range(0,300,48)
ax.set_xticks(xticks1)
ax.set_xticklabels([ "$%d$" %(y/12) for y in xticks1], fontsize=15)
plt.savefig('d:/picture/day31.png',dpi=200) 




import matplotlib as mpl
#mpl.rc('xtick', labelsize=13) 
mpl.rc('ytick', labelsize=14) 
sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(9,6))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[3]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',lw=1.5,label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',lw=1.5,label=u'预测数据')
plt.ylim(50,400)
##xticks1=range(0,288,12)
#ax.set_xticks(xticks1)
#ax.set_xticklabels([ "$%d$" %(y/12) for y in yticks1], fontsize=11)
ax.legend(loc=2,fontsize=16)
#ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间/h',fontsize=15)
ax.set_ylabel(u'行程时间/s',fontsize=15)
sns.despine() 
#ax.set_yticklabels(fontsize=11)
xticks1=range(0,300,48)
ax.set_xticks(xticks1)
ax.set_xticklabels([ "$%d$" %(y/12) for y in xticks1], fontsize=15)
plt.savefig('d:/picture/day29.png',dpi=200) 


























sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[1]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
plt.ylim(0,500)
ax.legend(loc=2)
ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间',fontsize=12)
ax.set_ylabel(u'行程时间/s',fontsize=12)
sns.despine() 



sns.set_style('white')
sns.set_style("ticks")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots(figsize=(5,5))
plt.subplots_adjust(left=0.15, bottom=0.12, top=None,right=None,hspace=0.68)
test_med=test_data[2]
test_x=np.array(test_med[:,:-1])
test_y=np.array(test_med[:,-1])
ax.plot(range(288),test_y,'-',label=u'实际数据')
ax.plot(range(288), gbm0.predict(test_x),'--',label=u'预测数据')
plt.ylim(0,500)
ax.legend(loc=2)
ax.set_title(u'（a）12月25日路段II行程时间',position=(0.5,-0.58),fontsize=14)
ax.set_xlabel(u'时间',fontsize=12)
ax.set_ylabel(u'行程时间',fontsize=12)
sns.despine() 


















