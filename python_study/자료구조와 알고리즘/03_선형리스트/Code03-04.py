# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:39:11 2022

@author: sara
"""
## 선형리스트 입출력 반복문 만들기

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

## 전역변수 선언 부분
katok = []
select = 1


## 메인 코드 부분

if __name__ == '__main__':
    while(select != 4):
        select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->'))
        
        if(select == 1):
            data = input('추가할 데이터 -->')
            add_data(data)
            print(katok)
        elif(select == 2):
            pos = int(input('삽입할 위치 --> '))
            data = input('추가할 데이터 --> ')
            insert_data(pos, data)
            print(katok)
        elif(select == 3):
            pos = int(input('삭제할 위치 --> '))
            delete_data(pos)
            print(katok)
        elif(select == 4):
            print(katok)
            break;
        else :
            print('1~4 중 하나를 입력하세요.')
            continue