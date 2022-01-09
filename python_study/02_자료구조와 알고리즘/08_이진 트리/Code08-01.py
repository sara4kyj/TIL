# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:17:38 2022

@author: sara
"""

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역



## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2		# node1왼쪽노드에 node2 연결

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4		# node2 왼쪽노드에 node4 연결

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5		# node2 오른쪽노드에 node5 연결

node3 = TreeNode()
node3.data = '문별'
node1.right = node3		# node1 오른쪽노드에 node3 연결

node6 = TreeNode()
node6.data = '선미'
node3.left = node6		# # node3 왼쪽노드에 node6 연결

print(node1.data, end=' ')
print()
print(node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end=' ')
