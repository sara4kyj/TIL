# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 10:30:10 2022

@author: sara
"""
## 큐 구조 함수화하기

## 함수
def isQueueFull():
    global size, queue, front, rear 
    if (rear >= size-1):
        return True
    else :
        return False

def enQueue(data):
    global size, queue, front, rear 
    if isQueueFull():
        print('Queue is Full')
        return
    rear += 1
    queue[rear] = data
    
def isQueueEmpty():
    global size, queue, front, rear 
    if (front == rear):
        return
    else : 
        return False

def deQueue():
    global size, queue, front, rear 
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global size, queue, front, rear 
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    return queue[front+1]

## 전역
size = 5
queue = [None for _ in range(size)]
front = rear = -1


## 메인
# queue = ['화사','솔라','문별','휘인','선미']
# front = -1
# rear = 4
# isQueueFull()

# queue = ['화사','솔라','문별','휘인', None]
# front = -1
# rear = 3
# enQueue('재남')
# enQueue('빅데이터 학생')

queue = ['화사','솔라',None,None, None]
front = -1
rear = 1

print('출구 <-- ', queue, '<-- 입구')

retData = peek()
print('다음 준비 손님 =>' , retData)

retData = deQueue()
print('입장할 손님은 ', retData)
retData = deQueue()
print('입장할 손님은 ', retData)
retData = deQueue()
print('입장할 손님은 ', retData)

print('출구 <-- ', queue, '<-- 입구')

