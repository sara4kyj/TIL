# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:08:59 2022

@author: sara
"""
## 선형리스트 

katok = ['다현','정연', '쯔위', '사나', '지효']
katok.append(None)  # 빈칸 추가
katok[5] = '모모'

print(katok)

katok.append(None)  # 빈칸 추가
katok[6] = katok[5]
katok[5]=None
katok[5] = katok[4]
katok[4]=None
katok[4] = katok[3]
katok[3]=None
katok[3] = '미나'

print(katok)





