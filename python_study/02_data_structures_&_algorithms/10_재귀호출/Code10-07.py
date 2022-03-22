# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:26:16 2022

@author: sara
"""

# 2단부터 9단까지 구구단을 출력하는 코드
def gugu(dan, num):
    print("%d X %d = %d" % (dan, num, dan*num))
    if num < 9:			# num이 9보다 작을때 반복
        gugu(dan, num+1)
        
for dan in range(1, 10):
    print('##', dan ,'단 ##')
    gugu(dan,1)
