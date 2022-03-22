# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:26:16 2022

@author: sara
"""

# 랜덤하게 생성한 배열의 합계를 구하는 코드
import random

def arySum(ary, n):
    if n <=0 :				# n이 0이되면 반복 종료
        return ary[0]
    return ary[n] + arySum(ary, n-1)	

ary = [random.randint(0,255) for _ in range(random.randint(20, 30))]

print(ary)
sum(ary)
print('sumAry is', arySum(ary, len(ary)-1))

