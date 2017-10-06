# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:31:03 2017

@author: wutongshu
"""
import sys
t=raw_input().split()
n=t[0]
m=t[1]
string_all=['X','#','1','2','3','4','5','6','7','8','9']
number1=['1','2','3','4','5','6','7','8','9']
all1=set()
for i in m:
    if i not in string_all:
        print 'somethings wrong'
        break
if len(m)!=int(n):
     print 'somethings wrong'
for j,i in enumerate(m):
    if i in number1:
        num=int(i)+1
        for h in range(num):
            if j-h>=0:
                if m[j-h]=='X':
                    all1.add(j-h)
            if j+h<int(n):
                if m[j+h]=='X':
                    all1.add(j+h)
len(all1)
                    
                    
import sys
t=raw_input()                    
                 
                
        
    