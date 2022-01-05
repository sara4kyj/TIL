# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:30:10 2022

@author: sara
"""
## 큐 구조 - front에 none 값이 있을 경우 처리하는 방법
## 함수
def isQueueFull():
    global SIZE, queue, front, rear 
    if (rear != SIZE-1) :
        return False
    elif (rear == SIZE-1) and (front == -1) :
        return True
    else:
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def enQueue(data):
    global SIZE, queue, front, rear 
    if (isQueueFull()):
        print('Queue is Full')
        return
    rear += 1
    queue[rear] = data
    
def isQueueEmpty():
    global SIZE, queue, front, rear 
    if (front == rear):
        return
    else : 
        return False

def deQueue():
    global SIZE, queue, front, rear 
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear 
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    return queue[front+1]

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


## 메인
queue = [None,None,'문별','휘인','선미']
front = 1
rear = 4

print('출구 <-- ', queue, '<-- 입구\n')

enQueue('유정')
print('출구 <-- ', queue, '<-- 입구\n')

enQueue('재남')
print('출구 <-- ', queue, '<-- 입구\n')

enQueue('윤아')
print('출구 <-- ', queue, '<-- 입구\n')
