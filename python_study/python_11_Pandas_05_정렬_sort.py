# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 13:25:11 2021

@author: sara
"""

#  pandas 정렬 sort()

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# pwd         # present working dierectory 현 위치 폴더(디렉토리)

pd.read_csv('./data/emp.csv')

# import os
# os.getcwd()           # get currnet working directory
# os.chdir('경로')      # change directory '경로'

# sort() 정렬
# 1. sort.index 
# - Series, DataFrame 호출 가능
# - index, column 재배치

emp = pd.read_csv('./data/emp.csv')

#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000

emp.ename
emp['ename']

# 0    smith
# 1    allen
# 2     ford
# 3    grace
# 4    scott
# 5     king
# Name: ename, dtype: object
# 요청결과를 Series로 반환

emp.idx = emp['empno']
emp.idx
emp.iloc[:,1:]      # >> 행은 전부, 열은 2번째(column 1)부터 출력
emp.set_index('ename')

emp = emp.set_index('ename')

emp.sort_index(ascending=False)     # >> ascending : 상승
emp.sort_index(ascending=True)      
emp.sort_index()                    # >> defalut : ascending=True

emp.sort_index(axis=0)
emp.sort_index(axis=1)      


# 2. sort.values
# - Series DataFrame 호출 가능
# - 본문의 값(value)으로 정렬(Series, DataFrame 특정 컬럼 순서대로)

emp.sort_values(by='sal')
emp.sort_values('sal')      # by 생략 가능

emp.sort_values(by='sal', ascending=False)

# 부서별 연봉 수준 : 부서는 내림차순, 연봉은 오름차순
emp.sort_values(by=['deptno','sal'], ascending=[True,False])
emp.sort_values(['deptno','sal'], ascending=[True,False])
