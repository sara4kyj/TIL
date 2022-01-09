# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:29:26 2022

@author: sara
"""

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None



## 전역
memory=[]
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']


## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)
for name in nameAry[1:] :
    node = TreeNode()
    node.data = name
    
    current = root
    while True :				
        if (current.data > name) :		
            if (current.left == None):
                current.left = node
                break
            current = current.left
        else :
            if (current.right == None):
                current.right = node
                break
            current = current.right
    memory.append(node)

print('이진 탐색 트리 구성 완료')

findName = '마마무'

current = root
while True :				# name를 찾을때까지 반복
    if current.data == findName :
        print(findName, 'find sucess!')
        break
    elif current.data > findName:
        if current.left == None:
            print(findName, 'not found')
            break
        current = current.left			# name이 없으므로 currnet를 currnet의 왼쪽노드로 변경
    else :
        if current.right == None:
            print(findName, 'not found')
            break
        current = current.right		# name이 없으므로 currnet를 currnet의 오른쪽노드로 변경






