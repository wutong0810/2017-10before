# -*- coding: utf-8 -*-
from src.travelTimeDeal.timeDeal import *
from src.qDeal.qStatis import *


# 函数参数说明：参数1上游数据路径，参数2下游数据路径，参数3路段长度，参数4上游驶入的方向1，参数5驶入方向1的驶入车道
# 参数6上游驶入方向2，参数7上游驶入方向2的驶入车道，参数8下游驶离方向，下游驶出车道，下游直行的驶出车道

def GetTravelTime(path1, path2, L,upDirect1,upLane1,upDirect2,upLane2, downDirect,downLane1,downLane2):
    dataUp=pd.read_csv(path1,encoding='utf-8')
    dataUpRoad,dataUpDay=dataTran(dataUp)
    dataDown=pd.read_csv(path2,encoding='utf-8')
    dataDownRoad, dataDownDay = dataTran(dataDown)
    maxtime=(L/60.0*3.6)
    mintime=(L/1.5*3.6)
    match_total_tt, match_total_final, match_total_rate = loopMatch(downData=dataDownRoad, upData=dataUpRoad,
                                                                    dayNum=dataDownDay, maxtime1=maxtime, mintime1=mintime,
                                                                    down_direction1=downDirect)
    q_total1 = inOut(upInsec=dataUp, downInsec=dataDown, upDire1=upDirect1, upClane1=upLane1, upDire2=upDirect2, upClane2=upLane2,
                     downDire=downDirect, downClane1=downLane,downClane2=downLane2)
    # 预处理,分车道,处理直行车道
    dataDeal1 = loopDeal(match_total_final1, claneNum=downLane2)
    data_15min1, freeV1 = loop_15min(dataDeal1, q_total1)
    return data_15min1,freeV1,q_total1







