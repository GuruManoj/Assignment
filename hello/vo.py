#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    a="NO"
    while x1<x2:
        x1=x1+v1
        x2=x2+v2
        #print(x1,x2)
        if x1==x2:
            a=a.replace(a,"YES")
            #print(a)
            break
    return a

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
