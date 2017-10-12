# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
def computeCorrelation(X, Y):
    xBar = np.mean(X)
    yBar = np.mean(Y)
    SSR = 0
    varX = 0
    varY = 0
    for i in range(0, len(X)):
        # 对应分子部分
        diffXXBar = X[i] - xBar
        diffYYBar = Y[i] - yBar
        SSR +=(diffXXBar * diffYYBar)
        # 对应分母求和部分
        varX += diffXXBar ** 2
        varY += diffYYBar ** 2
    SST = math.sqrt(varX * varY)
    return SSR / SST


def gridSearch(train_data, valid_data, pamater=range(20, 200, 20)):
    MAPE = np.zeros((1, len(pamater)))
    train_x = np.array(train_data.iloc[:, :-1])
    train_y = np.array(train_data.iloc[:, -1])
    valid_x = np.array(valid_data.iloc[:, :-1])
    valid_y = np.array(valid_data.iloc[:, -1])
    minMape = 1
    minPam = 0
    for i, j in enumerate(pamater):
        gbm0 = RandomForestRegressor(n_estimators=j, min_samples_split=50, min_samples_leaf=20, max_depth=4,
                                     max_features='sqrt', random_state=0)
        gbm0.fit(train_x, train_y)
        aa1 = np.hstack([valid_y.reshape(-1, 1), gbm0.predict(valid_x).reshape(-1, 1)])
        aa2 = np.abs(aa1[:, 0] - aa1[:, 1]) / aa1[:, 0]
        aa3 = np.hstack([aa1, aa2.reshape(-1, 1)])
        c1 = np.sum(aa3[:, 2]) / len(aa3)
        if c1 < minMape:
            minMape = c1
            minPam = i
        MAPE[0, i] = c1
    return minMape, pamater[minPam], MAPE


# 状态评估函数
def stateMap(x, freeV=86.3):
    c = 0
    x = max(1 - freeV / x, 0)
    if (x >= 0) & (x <= 0.2):
        c = 0
    elif (x > 0.2) & (x <= 0.4):
        c = 1
    elif (x > 0.4) & (x <= 0.6):
        c = 2
    elif (x > 0.6) & (x <= 0.8):
        c = 3
    elif (x > 0.8):
        c = 4
    return c
