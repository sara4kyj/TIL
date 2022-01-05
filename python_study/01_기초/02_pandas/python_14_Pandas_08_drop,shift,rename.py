# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:14:38 2021

@author: sara
"""

# 14. drop, shift, rename

# 기타메소드

run my_modules  # 라이브러리 호출 함수 모음

# 1. drop
# - 특정 행, 컬럼 제거
# - 이름 전달

emp = pd.read_csv("./data/emp.csv")
emp

# scott 퇴사
emp['ename']=='scott'                    # 조건문

emp.loc[emp['ename']=='scott',:]         # scott 관련된 record
emp.loc[~(emp['ename']=='scott'),:]      # ~ : scott를 제외한 record

emp.drop?
emp.drop(4, axis=0)                      # 행기준, 4번째 idx 제외

# [예제] 
# emp 데이터에서 sal 컬럼 제외(iloc)
emp 
emp['sal']
# 1.
emp.iloc[:,0:3]
# 2.
emp.iloc[:,:-1]
# 3.
emp.drop('sal', axis=1)
# 4.
emp.loc[:, "empno":"deptno"]

emp.drop(['ename','deptno'], axis=1)

# shift
# - 행 또는 열을 이동
# - 전일자 대비 증감율

emp
emp['sal'].shift()      # dafault : axis=0

# 예제 : 다음 데이터프레임에서 전일자 대비 증감율 출력
s1 = Series([3000,3500,4200,2800,3600], 
       index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
s1

# 1월 2일 증감율 >> (3500-30000)/3000
s1.shift()
(s1-s1.shift())/s1.shift() * 100

# 3. rename
# - 행, 컬럼명 변경

emp
emp.columns = ['emptno','ename','deptno','salary']      # sal를 salary로 변경
emp

emp.rename({'salary':'sal','deptno':'dept_no'}, axis=1)


# 예제 emp 데이터에서 ename을 index로 설정 후 scott을 대문자로 변경
emp.rename?
# 1.
emp = emp.set_index('ename')
emp = emp.rename({'scott':'SCOTT'}, axis=0)
emp

# 2.
emp = pd.read_csv("./data/emp.csv")
emp = emp.set_index('ename').rename({'scott':'SCOTT'}, axis=0)
emp