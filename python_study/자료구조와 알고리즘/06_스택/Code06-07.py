# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:22:27 2022

@author: sara
"""
## 스택구조 함수화하기 

## 함수
def isStackFull():
    global size, stack, top
    if top >= size-1:
        return True
    else :
        return False

def push(data):
    global size, stack, top
    if isStackFull():
        print('Stack is Full')
        return 
    top += 1
    stack[top] = data
    
def isStackEmpty():
    global size, stack, top
    if top == -1:
        return True
    else:
        return False

def pop():
    global size, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역
size = 5
stack = [None for _ in range(size)]
top = -1


## 메인
stack = ['커피', '녹차', '꿀물', '콜라', None]
top=3
# print(isStackFull())

push('맥주')
print(stack)

push('포도주')
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)

print(pop())
print(stack)




