# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:23:32 2022

@author: sara
"""

# 팩토리얼 구하기
def factNumber(num):
    if num <= 1:
        return 1
    return num * factNumber(num-1)		#num이 1보다 작거나 같아질때까지 반복

print(factNumber(5))