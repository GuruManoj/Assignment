# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:52:48 2018

@author: gurumanoj.r
"""
def translate(string):
    result=""
    for i in string:
        if (i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u')or(i==" "):
            result+=i
        else:
            result+=i+'o'+i
    return result
string=str(input("Enter the string\n"))
print(translate(string))
            