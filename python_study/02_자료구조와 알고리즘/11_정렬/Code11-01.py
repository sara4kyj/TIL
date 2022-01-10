# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:19:34 2022

@author: sara
"""

## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if(ary[minIdx] > ary[i]):		# i 위치의 값이 가장 작을 때 minidx를 i로 변경
            minIdx = i
    return minIdx		
    
## 전역
testAry = [55, 88, 33, 77]


## 메인
minPos = findMinIndex(testAry)
print('제일 작은 값 --> ', testAry[minPos])
