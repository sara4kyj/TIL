# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:15:49 2022

@author: sara
"""
## 선형리스트 - 함수화하기

## 함수부분
def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, position, -1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position] = friend
        
def delete_data(position):
    katok[position] = None
    klen = len(katok)
    for i in range(position+1, klen, 1):
        katok[i-1]=katok[i]
        katok[i]=None
    del(katok[klen-1])
    
    
## 전역변수 부분
katok = []


## 메인 코드부분
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)