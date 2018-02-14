# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:31:05 2018

@author: gurumanoj.r
"""

def len(string):
    i=0
    for x in string:
        i+=1
    return i
print("Enter the String")
string=input()
print("The lengthn of the string",len(string))