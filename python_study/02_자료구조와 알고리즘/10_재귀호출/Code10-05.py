# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:26:16 2022

@author: sara
"""

# 우주선 발사 카운트다운

def countDown(n):
    if n==0:
        print('발사')
    else:
        print(n)
        countDown(n-1)		# 0이 될때까지 반복
        
countDown(5)