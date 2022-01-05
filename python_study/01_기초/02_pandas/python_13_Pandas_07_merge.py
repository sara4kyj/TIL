# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:20:29 2021

@author: sara
"""

# 13. merge vx concat
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

np.arange(1,7)
df1 = DataFrame(np.arange(1,7).reshape(2,3), columns=['A','B','C'])
df2= DataFrame(np.arange(10,61,10).reshape(2,3), columns=['A','B','C'])

# concat
pd.concat([df1,df2])
pd.concat([df1,df2],axis=0)
# 행의 결합 >> 기본은 세로방향으로 합쳐짐

pd.concat([df1,df2],axis=1)
# 열의 결합 >> 가로방향으로 합쳐짐

pd.concat([df1,df2], ignore_index=True)
# 순차적인 인덱스 번호 부여됨

emp = pd.read_csv(".\data\emp.csv")
emp

df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석팀']})

# join
# 두 데이터프레임(테이블) 참조조건 활용, 하나의 객체로 합치거나 데이터로 처리하는 행위
# merge가 두 데이터 프레임 조인을 수행, 등가 조건만을 사용하여 조인이 가능

# pd.merge(left,          # 첫번째 데이터프레임
#          right,         # 두번째 데이터프레임
#          how='inner',   # 조인 방법(default = 'inner')
#          on=,           # 조인하는 컬림(컬럼명이 같을 경우)
#          left_on=,      # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
#          right_on=)     # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)

pd.merge(emp, df_dept, on='deptno')
pd.merge(emp, df_dept, how='inner', on='deptno')        
pd.merge(emp, df_dept, how='outer', on='deptno')        
pd.merge(emp, df_dept, how='left', on='deptno')
pd.merge(emp, df_dept, how='right', on='deptno')

# outer join
emp
df_dept_new = DataFrame({'deptno':[10,20], 'dname':['인사총무부','IT분석팀']})
pd.merge(emp, df_dept_new, how='inner', on='deptno')             # emp에 df_def_new(deptno으로 정렬)를 join 하며 join할 대상이 없는 경우 출력 X
pd.merge(emp, df_dept_new, how='outer', on='deptno')             # emp에 df_def_new(deptno으로 정렬)를 join 하며 join할 대상이 없으면 NaN 출력
pd.merge(emp, df_dept_new, how='left', on='deptno')              # emp를 기준(empno로 정렬)으로 df_def_new를 join 하며 df_def_new에 join할 key가 없으면 NaN 출력
pd.merge(emp, df_dept_new, how='right', on='deptno')             # df_def_new(deptno로 정렬)를 기준으로 emp를 join 하며 emp에 join할 key가 없으면 NaN 출력




