# -*- coding: utf-8 -*-
import cPickle as pickle

def writeObject(path0,data):
    path1 = unicode(path0, "utf8")
    fileOpen=open(path1,'wb')
    pickle.dump(data,fileOpen)
    fileOpen.close()



def loadObject(path0):
    path1 = unicode(path0, "utf8")
    fileOpen=open(path1,'rb')
    data=pickle.load(fileOpen)
    fileOpen.close()
    return data
