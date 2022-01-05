# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:05:58 2021

@author: sara
"""

import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))

dir(df1)    # 도움말

df1
#     0   1   2   3
# 0   1   2   3   4
# 1   5   6   7   8
# 2   9  10  11  12
# 3  13  14  15  16
df1.sum(axis=0) # 행별(서로 다른 행끼리)
# 0    28
# 1    32
# 2    36
# 3    40
# dtype: int64
df1.sum(axis=1) # 컬럼별(서로 다른 열끼리)
# 0    10
# 1    26
# 2    42
# 3    58
# dtype: int64

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()
# skipna = True는 default로 설정되어 있어 자동으로 NaN 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()    # NaN값이 있을경우 평균값으로 변
df1

df1[df1.isnull()]   # 데이터 프레임 전체에서 NaN 값 확인

df1.iloc[:,0].var() # 분산
df1.iloc[:,0].std() # 표준편차
df1.iloc[:,0].min() # 최소값
df1.iloc[:,0].max() # 최대값
df1.iloc[:,0].median() # 중위수(중앙값)

(df1.iloc[:,0] >= 10).sum() # 조건에 만족하는 개수 확인