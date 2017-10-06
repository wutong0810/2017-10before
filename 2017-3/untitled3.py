# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 17:04:44 2017

@author: wutongshu
"""

a0=plt.figure()
a0=plt.scatter(match_total_final[11].iloc[:,1],match_total_final[11].iloc[:,9],s=15)
a0=plt.xlim(0,86400)
a0=plt.ylim(0,900)



a1=plt.figure()
a1=plt.scatter(tt_deal[10].iloc[:,1],tt_deal[10].iloc[:,8],s=15)
a1=plt.xlim(0,86400)
a1=plt.ylim(0,900)






x = np.linspace(0, 5, 10)
y = x ** 2
fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes
# main figure
axes1.scatter(tt_deal[10].iloc[:,1],tt_deal[10].iloc[:,8],s=15)
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')
# insert
axes2.scatter(tt_deal[10].iloc[:,1],tt_deal[10].iloc[:,8],s=15)
plt.xlim(20000,23000)
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title')





fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');




















