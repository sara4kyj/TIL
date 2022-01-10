# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:00:24 2022

@author: sara
"""

## 재귀 1

## 함수
def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:			# count가 0이되면 재귀 종료
        print('반지넣기')
        return
    openBox()
    print('!!!! 상자 닫기')
    return

## 메인
count = 5
openBox()


