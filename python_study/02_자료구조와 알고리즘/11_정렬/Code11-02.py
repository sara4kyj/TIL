# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:23:35 2022

@author: sara
"""

import random

## 선택정렬 1 (가장 쉬운 정렬이며, 실무에서 사용해도 무관)

## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

## 전역
before = [random.randint(1,99) for _ in range(20)]
after = []

## 메인
print('정렬 전 -->', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬 후 -->', after)
