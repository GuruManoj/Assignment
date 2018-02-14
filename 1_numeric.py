# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:28:51 2018

@author: gurumanoj.r
"""

def max(a,b):
    if a>b:
        return a
    else:
        return b
print('Enter the first value')
a=int(input())
print('Enter the second value')
b=int(input())
print('The greatest Value is',max(a,b))