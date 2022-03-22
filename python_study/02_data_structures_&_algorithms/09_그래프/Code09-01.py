# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:22:28 2022

@author: sara
"""

## 함수
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


## 전역
G = None


## 메인
G = Graph(4)

# 점 a,b,c,d를 각각 행렬의 0,1,2,3이고 각 점이 만나는 값을 1이라고 할때의 그래프 표현 방법
G.graph[0][1] = 1; G.graph[0][2] = 1; G.graph[0][3] = 1
G.graph[1][1] = 1; G.graph[1][3] = 1
G.graph[2][0] = 1; G.graph[2][1] = 1; G.graph[2][3] = 1
G.graph[3][0] = 1; G.graph[3][2] = 1

print('## 무방향 그래프 ##')
for row in range(4):
    for col in range(4):
        print(G.graph[row][col], end=' ')
    print()

