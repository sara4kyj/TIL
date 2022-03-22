# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:03:05 2021

@author: sara
"""

# python pandas groupby
# 그룹연산
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드 처리 가능

import pandas as pd
from pandas import Series, DataFrame

kimchi = pd.read_csv("./data/kimchi_test.csv", encoding='cp949')

# kimchi.groupby?
# kimchi.groupby(
#     by=None,                        # 그룹핑할 컬럼(기준)
#     axis: 'Axis' = 0,               # 그룹핑 연산 방향
#     level: 'Level | None' = None)   # 멀티 인덱스일 경우, 특정 레벨의 값을 그룹핑 컬럼으로 사용

kimch.groupby(by=None, axis=0, level=None)

# 예제) 제품별, 판매처 별(김치별) 수량 총 합
kimchi.groupby(by=['제품','판매처'])['수량'].sum()
# 제품    판매처 
# 무김치   대형마트    1550027
#       백화점      510114
#       편의점       82623
# 열무김치  대형마트    1491864
#       백화점      567129
#       편의점       89006
# 총각김치  대형마트    1649486
#       백화점      658442
#       편의점      103725
# Name: 수량, dtype: int64

# 제품 기준으로 수량과 판매금액 총 합 구하기
kimchi.groupby(by=['제품'])[['수량','판매금액']].sum()

# 멀티인덱스
kimchi_2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()

# 예제) 제품별, 판매처별(김치별) 수량 총합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])     # aggregate : 종합하다

# agg : 여러 함수를 동시에 전달

# 예제 ) 제품별, 판매처별(김치별) 수량 판매금액, 총합과 평균
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])

# 예졔) 제품별, 판매처별(김치별) 수량은 총합, 판매금액 평균    >> agg 안에 dict() 사용
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})


# 멀티 레벨을 갖는 경우의 groupby 연산
kimchi_2
type(kimchi_2)
kimchi_2.groupby(level=0).sum()
kimchi_2.groupby(level='제품').sum()
kimchi_2.groupby(level=1).sum()
