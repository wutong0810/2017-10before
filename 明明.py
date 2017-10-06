# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:03:47 2017

@author: wutongshu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

dataSet=pd.read_csv(r'd:/1130-1206data.csv',header=None)



dataSet.iloc[:,4]=None
data=[]
for i in range(7):
    for j in range(29):
        dataMedium=dataSet.iloc[(i*288):(i+1)*288,(10*j+2):(10*j+5)].mean(axis=1)
        data.append(dataMedium)
        
data=[]
for i in range(7):
    for j in range(29):
        dataMedium=dataSet.iloc[(i*288):(i+1)*288,10*j+10]
        data.append(dataMedium)        
        
        

       
for i in range(7):
    for j in range(0,16,4):
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'q/veh',fontsize=13)
#        plt.subplots_adjust(left=0.13, bottom=0.18, top=0.9,right=None,hspace=0.53)
        #ax.set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
#        sns.despine() 
        fileLoc='d:/q/'+str(i)+'day'+str(j)+'clane_up.png'
        xticks =range(1,24)
        ax.set_xticks(xticks)
        ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
        plt.savefig(fileLoc,dpi=200) 
#        
#for i in range(7):
#    for j in range(15,29,4):
#        if j<22:
#            data1=data[i*29+j]
#            data2=data[i*29+j+1]
#            data3=data[i*29+j+2]
#            data4=data[i*29+j+3]
#            plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#            plt.rcParams['axes.unicode_minus']=False
#            sns.set_style('white')
#            sns.set_style("ticks")
#            fig, ax = plt.subplots(figsize=(14,14))
#            a1=np.linspace(0,24,288)
#            plt.plot(a1,data1,label=str(j))
#            plt.plot(a1,data2,label=str(j+1))
#            plt.plot(a1,data3,label=str(j+2))
#            plt.plot(a1,data4,label=str(j+3))
#            plt.legend(loc=2,fontsize=12)
#            ax.set_xlabel(u'time/h',fontsize=13)
#            ax.set_ylabel(u'q/veh',fontsize=13)
#        else :
#            data1=data[i*29+j]
#            data2=data[i*29+j+1]
#            data3=data[i*29+j+2]
#            data4=data[i*29+j+3]
#            data5=data[i*29+j+4]
#            data6=data[i*29+j+5]
#            plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
#            plt.rcParams['axes.unicode_minus']=False
#            sns.set_style('white')
#            sns.set_style("ticks")
#            fig, ax = plt.subplots(figsize=(14,14))
#            a1=np.linspace(0,24,288)
#            plt.plot(a1,data1,label=str(j))
#            plt.plot(a1,data2,label=str(j+1))
#            plt.plot(a1,data3,label=str(j+2))
#            plt.plot(a1,data4,label=str(j+3))
#            plt.plot(a1,data5,label=str(j+4))
#            plt.plot(a1,data6,label=str(j+5))
#            plt.legend(loc=2,fontsize=12)
#            ax.set_xlabel(u'time/h',fontsize=13)
#            ax.set_ylabel(u'q/veh',fontsize=13)
#        
##        plt.subplots_adjust(left=0.13, bottom=0.18, top=0.9,right=None,hspace=0.53)
#        #ax.set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
##        sns.despine() 
#        fileLoc='d:/pic/'+str(i)+'day'+str(j)+'clane_down.png'
#        plt.savefig(fileLoc,dpi=200)   
 






       
for i in range(7):
    for j in range(15,22,4):
#        print j
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'q/veh',fontsize=13)        
        fileLoc='d:/q/'+str(i)+'day'+str(j)+'clane_down.png'
        plt.savefig(fileLoc,dpi=200) 
        
for i in range(7):
    for j in [23]:
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        data5=data[i*29+j+4]
        data6=data[i*29+j+5]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.plot(a1,data5,label=str(j+4))
        plt.plot(a1,data6,label=str(j+5))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'q/veh',fontsize=13)     
        fileLoc='d:/q/'+str(i)+'day'+str(j)+'clane_down.png'
        plt.savefig(fileLoc,dpi=200) 
#速度




for i in range(7):
    for j in range(0,16,4):
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'V/(km/h)',fontsize=13)
#        plt.subplots_adjust(left=0.13, bottom=0.18, top=0.9,right=None,hspace=0.53)
        #ax.set_title(u'（a）原始数据',position=(0.5,-0.53),fontsize=13)
#        sns.despine() 
        fileLoc='d:/sudu/'+str(i)+'day'+str(j)+'clane_up.png'
        xticks =range(0,25)
        ax.set_xticks(xticks)
        ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
        plt.savefig(fileLoc,dpi=200) 
                
       
for i in range(7):
    for j in range(15,22,4):
#        print j
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'q/veh',fontsize=13)  
        xticks =range(0,25)
        ax.set_xticks(xticks)
        ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
        fileLoc='d:/sudu/'+str(i)+'day'+str(j)+'clane_down.png'
        plt.savefig(fileLoc,dpi=200) 
        
for i in range(7):
    for j in [23]:
        data1=data[i*29+j]
        data2=data[i*29+j+1]
        data3=data[i*29+j+2]
        data4=data[i*29+j+3]
        data5=data[i*29+j+4]
        data6=data[i*29+j+5]
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False
        sns.set_style('white')
        sns.set_style("ticks")
        fig, ax = plt.subplots(figsize=(14,14))
        a1=np.linspace(0,24,288)
        plt.plot(a1,data1,label=str(j))
        plt.plot(a1,data2,label=str(j+1))
        plt.plot(a1,data3,label=str(j+2))
        plt.plot(a1,data4,label=str(j+3))
        plt.plot(a1,data5,label=str(j+4))
        plt.plot(a1,data6,label=str(j+5))
        plt.legend(loc=2,fontsize=12)
        ax.set_xlabel(u'time/h',fontsize=13)
        ax.set_ylabel(u'q/veh',fontsize=13)   
        xticks =range(0,25)
        ax.set_xticks(xticks)
        ax.set_xticklabels(["$%d$" % y for y in xticks], fontsize=13)
        fileLoc='d:/sudu/'+str(i)+'day'+str(j)+'clane_down.png'
        plt.savefig(fileLoc,dpi=200)    