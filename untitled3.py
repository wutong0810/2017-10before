# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:44:07 2017

@author: wutongshu
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
import matplotlib.pyplot as plt
plt.plot((1,2,3),(4,3,-1))
plt.xlabel(u'横坐标')
plt.ylabel(u'纵坐标')
plt.show()


fig, ax = plt.subplots()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
plt.plot((1,2,3),(4,3,-1),label=u'横着')
plt.xlim(0,289)
plt.ylim(0,500)
plt.legend(loc=2, fontsize=22)
ax.set_xlabel(u'大',fontsize=18)
ax.set_ylabel('corr',fontsize=18)



fig, ax = plt.subplots()
from statsmodels.tsa.arima_model import ARIMA
a=np.array(test_data2.iloc[:,11])
c=np.zeros((len(a),2))
c[:,0]=a
for i in range(12,len(a)):
    a1=a[:i]
    model = ARIMA(a1, order=(2,1,0))
    model_fit = model.fit(trend='nc', disp=0)
    yhat = model_fit.forecast()[0]
    c[i,1]=yhat
    
    
aa2=np.sum(np.abs(c[:,0]-c[:,1])/c[:,0])
aa2/2016.
cc2=np.abs(c[:,0]-c[:,1])/c[:,0]
a=np.zeros((7,1))
for i in range(7):
    a[i,0]=(np.sum(np.abs(c[(i)*288:(i+1)*288,0]-c[(i)*288:(i+1)*288,1])/c[(i)*288:(i+1)*288,0]))/288
    
    
    

















model = ARIMA(a, order=(3, 1, 0)) 
results_AR = model.fit()  
plt.plot(a)
plt.plot(results_AR.fittedvalues, color='red')
results_AR.fittedvalues





values = dataset.values

history = [values[i] for i in range(len(values))]

predictions = list()

test_values = test.values

for t in range(len(test_values)):
    

    model = ARIMA(history, order=(7,0,0))

model_fit = model.fit(trend='nc', disp=0)
yhat = model_fit.forecast()[0]

predictions.append(yhat)

history.append(test_values[t])

rmse = sqrt(mean_squared_error(test_values, predictions))

















