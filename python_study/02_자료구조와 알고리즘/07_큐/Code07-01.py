# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 09:20:05 2022

@author: sara
"""
## 큐 구조 파악하기 

## 함수


## 전역
size = 5
queue = [None for _ in range(size)]
# queue = [None, None, None, None, None]
front = rear = -1


## 메인
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구 <-- ', queue, '<-- 입구')

# 입장

front += 1
data = queue[front]
queue[front] = None
print('이번에 입장한 손님은 ' , data)

front += 1
data = queue[front]
queue[front] = None
print('이번에 입장한 손님은 ' , data)

front += 1
data = queue[front]
queue[front] = None
print('이번에 입장한 손님은 ' , data)

print(queue)
