# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:40:53 2022

@author: sara
"""
import random
## 선택정렬 2 >> 정렬되지 않는 상태에서 n번째에서 n번째 위치에 최소값을 저장
## 함수
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k                
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

## 전역
dataAry = [random.randint(1,99) for _ in range(20)]

## 메인
print('정렬전 -> ', dataAry)
dataAry = selectionSort(dataAry)
print('정렬후 -> ', dataAry)
