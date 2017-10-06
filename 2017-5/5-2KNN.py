# -*- coding: utf-8 -*-
"""
Created on Tue May 02 16:47:09 2017

@author: wutongshu
"""
import numpy as np
import operator
def autoNorm(dataSet):
    minvals=dataSet.min(0)
    maxvals=dataSet.max(0)
    ranges=maxvals-minvals
    normDataSet=np.zeros((shape(dataSet)))
    m=dataSet.shape[0]
    normDataSet=dataSet-np.tile(minvals,(m,1))
    normDataSet=normDataSet/np.tile(ranges,(m,1))
    return normDataSet
    
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqDistance=np.sqrt(np.sum(diffMat**2,axis=1))
    sortedDistanceIndices=np.argsort(sqDistance)
    classCount={}
    for i in range(k):
        voteLabel=labels[sortedDistanceIndices[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
    

#测试数据集
#group=np.array([[1,1.1],[1,1],[0,0],[0,0.1]])
#labels=['A','A','B','B']
#classify0([0,0],group,labels,3)
