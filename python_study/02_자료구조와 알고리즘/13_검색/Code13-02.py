# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:18:15 2022

@author: sara
"""
import random

## 이진검색(=탐색) 
# >> 중간값을 기준으로 좌측에 있을경우 end값을 중간값-1 로 설정 
# >> 		      우측에 있을 경우 start값을 중간값+1 로 설정
# >> start가 end보다 작거나 같은데 탐색하지 못한 경우 탐색 종료

## 함수
def binaryqSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) -1
    while start <= end :
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else : 
            end = mid -1
    return pos

## 전역
dataAry = [random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0, len(dataAry)-1)]
dataAry.sort()

## 메인
print('배열 ->', dataAry)
position = binaryqSearch(dataAry, findData)
if position == -1:
    print(findData, '없어요')
else:
    print(findData, '가', position, '에 있음')






