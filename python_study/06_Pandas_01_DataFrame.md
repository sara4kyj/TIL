```python
#  07. Pandas _ Series, DataFrame  # 2차원 정형데이터 분석에 주로 사용

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# pandas : 2차원 정형데이터(테이블, 표, 데이터프레임)
# 기본단위 : Series
# - 1차원 자료구조
# - 하나의 데이터 타입 허용

s1 = Series([1,2,3,4])
s2 = Series([1,2,3,'4'])
s3 = Series([1,2,3,4], index = ['a','b','c','d'])

Series(s3, index=['A','B','C','D']) # 이미 index가 존재하는 경우

# 색인 (indexing)
s1[0]   # 1 (차원축소 일어남 >> scalar)
s1[0:1] # 차원축소x >> Series로 반환
# 0    1
# dtype: int64

s1[[0,3]]  # 차원축소x >> Series로 반환
# 0    1
# 3    4
# dtype: int64

s3['a']
s3[['a','c']]

s3['a':'c']     # 문자열의 연속 추출은 마지막 범위 포함
# a    1
# b    2
# c    3
# dtype: int64

# s1 > 2
# Out[39]: 
# 0    False
# 1    False
# 2     True
# 3     True
# dtype: bool
s1[s1 > 2]      # trun만 반환       
# 2    3
# 3    4
# dtype: int64

s3.b            # 2 >> key indexing

# 연산 
s1+1

s4 = Series([10,20,30,40])
s5 = Series([10,20,30,40], index=['c','d', 'e', 'f'])
s1
s4
s1 + s4     # 동일한 index(key) 끼리 합산
s3
s5
s3 + s5     # key가 다른 경우 모두 NAN 반환  NAN: not a number
s3.add(s5, fill_value=0)    # 양쪽 모두 존재하지 않는 key일 경우
                            # NA가 반환되는 것을 방지하기 위해 fill_value 옵션 사용 적극 추천
s3.sub(s5, fill_value=0)    # - 연산
s3.mul(s5, fill_value=1)    # * 연산
s3.div(s5, fill_value=1)    # / 연산

# 기본 메소드
s1.dtype        # dtype('int64') 데이터 타입 출력
s1.index        # RangeIndex(start=0, stop=4, step=1) 인덱스 출력
s3.values       # array([1, 2, 3, 4], dtype=int64) 값(value) 출력

s3[['c','d','a','b']]       # 색인 사용, 배치 순서 변경
s3.reindex(['c','d','a','b'])   # 메소드로 배치 순서 변경

s3.index = ['A', 'B', 'C', 'D']     # index 수정
s3
s3[0] = 10      # 값 수정
s3

# DataFrame
# 2차원 자료구조 (행과 열 구조)
# 생성
d1 = {'name': ['smith', 'will'], 'sol':[900,1800]}
d1

d2 = DataFrame(d1)
d2

import numpy as np
d3 = DataFrame(np.arange(1,7).reshape(2,3), index=['a','b'], columns=['col1','col2','col3'])
d3

# 색인 (indexing) *****

# 컬럼 선택
d3.col1

d3['col1']

# iloc, loc ***
# iloc : positonal indexing
# loc : label indexing
d3
d3.iloc[:,0]
d3.iloc[:,0:3]
d3.iloc[:,[0,-1]]

d3.loc[:,['col1','col2']]

# 조건 색인 처리
d3.loc[d3.col1 == 1, :]

# 기본 메서드
d3.dtypes       # 각 컬럼 별 데이터 타입 확인
d3.index
d3.columns
d3.values

d3.columns = ['A','B','C']
d3

# 연산
d3 + 10

d4 = DataFrame({'A':[10,40], 'B':[20,30], 'C':[30,80]}, index=['a', 'b'])
d5 = DataFrame({'A':[10,40], 'B':[20,30]}, index=['a', 'b'])
d3
d4 
d5
d3 + d5
d3.add(d5, fill_value=0)		# NaN 값 반환으로 인한 오류를 방지하기 위해 fill_value=0를 사용
```
