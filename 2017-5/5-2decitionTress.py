# -*- coding: utf-8 -*-
"""
Created on Tue May 02 17:31:40 2017

@author: wutongshu
"""
from math import log
import operator
import numpy as np
def calcShannoEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        labelCounts.setdefault(currentLabel,0)
        labelCounts[currentLabel]+=1
        shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
    return shannonEnt
group=np.array([[1,1.1],[1,1],[0,0],[0,0.1]])
labels=np.array(['A','A','A','B'])
c=np.hstack((group,labels.reshape(-1,1)))

a=c.tolist()
#classify0([0,0],group,labels,3)




def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reduceFeatVec=featVec[:axis]
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet
 

def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannoEnt(dataSet)
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet,i,value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannoEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if infoGain>bestInfoGain:
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature
            



def majorityCnt(classList):
    classCount={}
    for vote in classList:
        classCount.setdefault(vote,0)
        classCount[vote]+=1
    sortedCLassCount=sorted(classCount.iteritems,key=operator.itemgetter(1),\
           reversed=Ture)
    return sortedCLassCount[0][0]




def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0]==len(classList)):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeat][value]=createTree(splitDataSet(\
              dataSet,bestFeat,value),subLabels)
    return myTree
    



















     
        


           