# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:34:15 2018

@author: gurumanoj.r
"""
def check(character):
    if (character=='a')or(character=='e')or(character=='i')or(character=='o')or(character=='u'):
        return True
    else:
        return False
print("Enter a character")
character = str(input())
print(check(character))