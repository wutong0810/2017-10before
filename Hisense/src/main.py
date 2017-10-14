# -*- coding: utf-8 -*-
from src.travelTimeDeal.timeDeal import *
from src.qDeal.qStatis import *
from src.otherFunc.func import *



# 函数参数说明：参数1上游数据路径，参数2下游数据路径，参数3路段长度，参数4上游驶入的方向1，参数5驶入方向1的驶入车道
# 参数6上游驶入方向2，参数7上游驶入方向2的驶入车道，参数8下游驶离方向，下游驶出车道，下游直行的驶出车道
# 函数输出行程时间，自由流行程速度，驶入驶出流量
def GetTravelTime(path1, path2, L,upDirect1,upLane1,upDirect2,upLane2, downDirect,downLane1,downLane2):
    ipath1=unicode(path1,'utf8')
    ipath2=unicode(path2,'utf-8')
    dataUp=pd.read_csv(ipath1,encoding='utf-8')
    dataUpRoad,dataUpDay=dataTran(dataUp)
    dataDown=pd.read_csv(ipath2,encoding='utf-8')
    dataDownRoad, dataDownDay = dataTran(dataDown)
    maxtime=(L/1.5*3.6)
    mintime=(L/60.0*3.6)
    match_total_tt, match_total_final, match_total_rate = loopMatch(downData=dataDownRoad, upData=dataUpRoad,
                                                                    dayNum=dataDownDay, maxtime1=maxtime, mintime1=mintime,
                                                                    down_direction1=downDirect)
    q_total1 = inOut(days=dataDownDay,upInsec=dataUp.iloc[:,:5], downInsec=dataDown.iloc[:,:5], upDire1=upDirect1, upClane1=upLane1, upDire2=upDirect2, upClane2=upLane2,
                     downDire=downDirect, downClane1=downLane1,downClane2=downLane2)
    # 预处理,分车道,处理直行车道
    dataDeal1 = loopDeal(match_total_final, claneNum=downLane2)
    data_15min1, freeV1 = loop_15min(dataDeal1, q_total1)
    return data_15min1,freeV1,q_total1,match_total_rate







if __name__=='__main__':
    dataFinal1=GetTravelTime(path1=r'D:\Data\数据\贵阳数据\rj_xg1205.csv', path2=r'D:\Data\数据\贵阳数据\rj_zy1205.csv', L=400,upDirect1=1,upLane1=[2,3,4],upDirect2=3,upLane2=[1,2], downDirect=1,downLane1=[1,2,3,4,5,6],downLane2=[3,4,5,6])
    writeObject(path0=r'd:/test.txt',data=dataFinal1)



