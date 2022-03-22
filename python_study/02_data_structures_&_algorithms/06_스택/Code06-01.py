# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:03:55 2022

@author: sara
"""
## 스택구조 공부하기 

## 함수

## 전역
# stack = [None,None,None,None,None]
size = 5
stack = [None for _ in range(size)]
top = -1

## 메인
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print(stack)

data = stack[top]
stack[top] = None
top -= 1
print('pop: ', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop: ', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop: ', data)

print(stack)