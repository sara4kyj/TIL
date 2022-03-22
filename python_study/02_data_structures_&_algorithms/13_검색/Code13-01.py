# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:05:27 2022

@author: sara
"""
import random
## 순차검색
## 함수
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    for i in range(size):
        if ary[i] == fData:  	# 찾는 데이터와 같다면 반복문 종료
            pos = i
            break    
    return pos

## 전역
dataAry = [random.randint(1,99) for _ in range(20)]
findData = dataAry[random.randint(0, len(dataAry)-1)]


## 메인
print('배열 ->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1:
    print(findData, '없어요')
else:
    print(findData, '가', position, '에 있음')


