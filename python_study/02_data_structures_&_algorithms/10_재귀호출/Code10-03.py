# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:19:09 2022

@author: sara
"""

# 재귀 3

def addNumber(num):
    if num <= 1:
        return 1
    return num + addNumber(num-1)		# num이 1보다 작거나 같아질때까지 반복

print(addNumber(10))