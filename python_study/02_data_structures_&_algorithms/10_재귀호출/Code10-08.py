# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:26:16 2022

@author: sara
"""

# N 제곱을 계산하는 코드
def pow2(x, n):
    if n <= 1:		# n이 1보다 작거나 같아지면 종료
        return x
    return x*pow2(x,n-1)

print(pow2(2,10))