# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:22:40 2022

@author: sara
"""
# 큐 원형구조 파악 및 함수화하기

## 함수
def isQueueEmpty():
    global SIZE, queue, front, rear 
    if (front == rear):
        return
    else : 
        return False

def isQueueFull():
    global SIZE, queue, front, rear 
    if ( (rear+1) % SIZE == front):
        return True
    else :
        return False 
    
def enQueue(data):
    global size, queue, front, rear 
    if isQueueFull():
        print('Queue is Full')
        return
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global size, queue, front, rear 
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인
queue = [None,None,'문별','휘인','선미']
front = 1
rear = 4

enQueue('재남')
print('출구 <-- ', queue, '<-- 입구')

deQueue()
enQueue('유정')
print('출구 <-- ', queue, '<-- 입구')



