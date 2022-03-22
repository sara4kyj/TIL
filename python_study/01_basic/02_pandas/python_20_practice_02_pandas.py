# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 15:13:32 2022

@author: sara
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
from pandas.tseries.offsets import Day, Hour, Second
from datetime import timedelta
import matplotlib.pyplot as plt
from numpy import nan as NA
import math

# card.csv 파일 읽어오기
card = pd.read_csv('./data/card.csv', encoding='cp949')

# NUM를 인덱스로 사용
card = card.set_index('NUM')

# 문제 ) 일자별 총 지출 금액을 구해서, 마지막 컬럼에 추가
# (천단위 구분기호 제거 후 숫자 컬럼 변경하시오.)

# int('19,400'.replace(',',''))
# 이 행위(행변환 함수)를 전체에 적용할 때 사용

# applymap : 2차원 데이터 셋(data frame)에 함수 적용 위해 사용
card = card.applymap(lambda x : int(x.replace(',','')))
card

card['총합'] = card.sum(axis=1)



# [참고 - 위 함수를 특정 컬럼에 대해 적용]
card_new = pd.read_csv('./data/card.csv', encoding='cp949')
card_new = card_new.set_index('NUM')

# 식료품 컬럼에만 적용
card_new['식료품'].applymap(lambda x : int(x.replace(',','')))
# 1차원 데이터 셋(Series)에 적용 불가
card_new['식료품'] = card_new['식료품'].map(lambda x : int(x.replace(',','')))

card_new['의복'] = card_new['의복'].str.replace(',','').astype('int')

card_new['책값'].replace(',','')
# 값 치환 메서드(특정값과 정확히 일치하는 값을 변경하거나 삭제)
# ','와 완전히 일치하는 값을 변경 또는 삭제
card_new['책값'].replace('28,000','')


# 2) 일자별로 각 품목별 지출 비율을 출력하세요. (%로 출력하세요)
card = pd.read_csv('./data/card.csv', encoding='cp949')
card = card.set_index('NUM')

card = card.applymap(lambda x : int(x.replace(',','')))

# 첫번재 행에 대해 확인
(card.iloc[0,:] / card.iloc[0,:].sum())*100        # 첫째날 지출 총 합

# apply 메서드 이용, 각 일자별로 적용
f2 = lambda x: (x / x.sum())*100
card.apply(f2, axis=1)

# 결과 해석
# >> 의복비 지출이 심함(일자별 지출 중 의복비 비중이 50% 이상)
# insight : 의복비 비중을 줄일 필요성이 있음(주관적 의견)

# 형(데이터 타입) 변환 : 함수, astype 메서드
# 적용함수 : map 함수, map 메서드, apply 메서드, applymap 메서드
# 치환함수 : 문자열 메서드, 벡터화 내장된 문자열 메서드, 값 치환 메서드
# 색인
# 컬럼 추가, 컬러 내용 변경


# 문제 ) 각 구매마다 포인트 확인하고, POINT 컬럼 생성
# POINT 는 주문금액 5만 1%, 5만이상 10만 미만 2%, 10만 이상 3%
# 문제풀이 포인트 : 조건에 따른 치환 혹은 연산
df1 = pd.read_csv('./data/ex_test1.csv', encoding='cp949')

# sol1)
result = []

for i in df1['주문금액']:
    if i < 50000:
        result.append(i*0.01)
    elif i < 100000:
        result.append(i*0.02)
    else :
        result.append(i*0.03)

df1['point'] = np.round(result,2)

# sol2) np.where(벡터연산가능한 조건 연산 함수)
# sql에서 copy
# sql : select * from db_name where 조건문
# np.where(조건, 참리턴, 거짓리턴)
# 첫번째 조건이 거짓이라면, 새로운 조건 추가

# np.where(df1['주문금액']<50000, df1['주문금액']*0.01, df1['주문금액']*0.02)
df1['point'] = np.where(df1['주문금액']<50000,
                         df1['주문금액']*0.01,
                         np.where(df1['주문금액']<100000,
                                  df1['주문금액']*0.02,
                                  df1['주문금액']*0.03))

# 2. 회원번호별 총 주문금액과 총 포인트 금액 확인
df1.groupby('회원번호')[['주문금액', 'point']].sum()

# [연습문제 : Y 값을 서로 다른 숫자로 변경]
# 출제 의도 : 조건에 따른 치환

df2 = DataFrame({'Y':['a','a','b','b','c','a','a','b'],
           'X1':[1,2,4,4,6,3,5,4],
           'X2':[10,30,43,34,43,43,94,32]})

# 하나씩 사용자가 치환
df2['Y'].replace({'a':0, 'b':1, 'c':2})

# 자동 변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb = LabelEncoder()
m_lb.fit_transform(df2['Y'])


# [연습문제 - 조건에 따른 값의 수정]
# df2에서 X1이 5이상일 경우, X1 평균으로 수정(최빈값, 중앙값, 최소값)

df2['X1'][df2['X1']>=5]

df2.loc[df2['X1']>=5, 'X1']   # >> 추천

df2
m1 = df2['X1'].mean()       # 평균값
m2 = df2['X1'].median()     # 중위값
m3 = df2['X1'].mode()       # 최빈값
m4 = df2['X1'].mode()[0]
m5 = df2['X1'].min()        # 최소값
m6 = df2['X1'].max()        # 최대값

import statistics as stat
stat.mode(df2['X1'])        # 4 : 하나의 상수로 리턴


df2 = DataFrame({'Y':['a','a','b','b','c','a','a','b'],
           'X1':[1,2,4,4,6,3,5,4],
           'X2':[10,30,43,34,43,43,94,32]})

df2.loc[df2['X1'] >= 5, 'X1'] = m4



