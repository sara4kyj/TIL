# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:22:28 2021

@author: sara
"""

# 17. 날짜표현
# - 월별, 일별, 요일별 집계
# - 현재날짜 - 입사일자 = 근무 일자

# 현재날짜
run my_modules

from datetime import datetime

d1 = datetime.now()
type(d1)

d1.year     # 연
d1.month    # 월
d1.day      # 일

# 2. 날짜 파싱
d2 = '2022/01/01'   # type : string
d2.year             
# AttributeError: 'str' object has no attribute 'year'

# str -> datetime 변환 : datetime.strptime(date_string, format)      # 벡터연산 안됨

datetime.strptime(d2, '%Y/%m/%d')
datetime.strptime('09/12/25', '%d/%m/%y')

# Series 벡터 연산 안됨
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
datetime.strptime(s1, '%Y/%m/%d')
#TypeError: strptime() argument 1 must be str, not Series

# 해결방안
s1.map(lambda x: datetime.strptime(x, '%Y/%m/%d'))

# 2) pd.to_datetime
# 벡터연산가능
s1
s2 = pd.to_datetime(s1)
# 0   2022-01-01
# 1   2022-01-02
# 2   2022-01-03
# dtype: datetime64[ns]

s2
pd.to_datetime(s2, format = '%Y/%m/%d')

# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을 return하도록 날짜 출력 형식 변경)
# (연/월/일) -> (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경한 후 return 데이터 타입은 무조건 str타입

d1 = datetime.now()
d1
datetime.strftime(d1, '%a')         # 요일 리턴 (축약형) : 'Wed'
datetime.strftime(d1, '%A')         # 요일 리턴 (완전체) : 'Wednesday'
datetime.strftime(d1, '%m-%d, %Y')  # '%m-%d, %Y' 형태의 str로 리턴 : '12-29, 2021'
datetime.strftime(d1, '%m-%d, %y')  # '%m-%d, %Y' 형태의 str로 리턴 : '12-29, 21'

datetime.strftime(d1, '%Y')         # 연도 리턴 (완전체) : '2021'
datetime.strftime(d1, '%y')         # 연도 리턴 (축약형) : '21'

s2
datetime.strftime(s2, '%Y')         # 벡터연산 불가
# TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object

#  >> 벡터연산을 위해 map 사용
s2
s2.map(lambda x: datetime.strftime(x, '%Y'))

# 4) 날짜 연산 ***
d1              # 현재시간
d1+100          

# a) offset
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)

# b) timedelta (날짜와의 차이)
from datetime import timedelta
d1 + timedelta(100)

# c) (실무용) DateOffset *** (추천)
d1 + pd.DateOffset(months = 4)

# 5. 날짜 - 날짜
d1 - datetime.strptime(d2, '%Y/%m/%d')

d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
d3.days
d3.seconds

# [연습문제]
# 요일별 통화건수 총합
deli = pd.read_csv('./data/delivery.csv', encoding='cp949')
deli.dtypes         # 모든 column의 datatype 출력
deli.head()         # head 확인 / 0-4행 출력
deli.info()         # column의 정보 출력

deli.describe()     # 개수, 평균, 표준편자, 최소값, 사분위수, 최대값 출력
deli.boxplot()

# 날짜 파싱
deli
deli['일자']
type(deli['일자'])
deli['일자'] = pd.to_datetime(deli['일자'], format = '%Y%m%d')
type(deli['일자'])

deli['요일'] = deli['일자'].map(lambda x: datetime.strftime(x, '%A'))
deli

# 요일별 통화건수
total = deli.groupby('요일')['통화건수'].sum()
total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]    
# 월화수목금토일 순으로 재배치
# 아직까지 정렬로 배치 안됨, 색인으로 처리해야함
