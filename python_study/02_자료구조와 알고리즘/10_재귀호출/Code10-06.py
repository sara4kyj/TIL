# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:26:16 2022

@author: sara
"""

# 입력한 숫자만큼 차례대로 별 모양을 출력하는 코드

def printStar(n):
    if n > 0:		# n이 0보다 클때 반복
        printStar(n-1)	# n-1하여 함수 실행  -> n번 반복하면 함수 종료
        print('*'*n)
        
printStar(5)