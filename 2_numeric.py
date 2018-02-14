# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:26:34 2018

@author: gurumanoj.r
"""

def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c :
        return b        
    else:
        return c
print('Enter the first value')
a=int(input())
print('Enter the second value')
b=int(input())
print('Enter the third value')
c=int(input())
print('The greatest Value is',max_of_three(a,b,c))