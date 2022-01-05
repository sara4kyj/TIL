# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:18:12 2021

@author: sara
"""

# 판다스_문자열 메소드
# 기본 메소드 : 벡터 연산 불가능 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')[1]

l1 = ['abc', 'def']
l2 = ['a/b/c', 'd/e/f']

l1.upper()
l2.upper()

list(map(lambda x: x.upper(),l1))
list(map(lambda x: x.split('/'),l2))

# pandas 메서드 : 벡터화 내장 (매 원소마다 반복 가능)
# Series, DataFrame 적용 가능

from pandas import Series, DataFrame

# 1) split
s1 = Series(l1)
s2 = Series(l2)

s2.str.split('/')

# 대소치환
s1.str.upper()
s1.str.lower()
s1.str.title()

# replace (치환)
s1.str.replace('a','A') # 문자열 치환
s1.str.replace('a','')  # 문자열 삭제



# 예제 : 천단뒤 구분기호 처리
s3 = Series(['1,200', '3,000','10,000'])
s3.str.replace(',','').astype(int).sum()

# 패턴확인 : startswith, endswith, contains
s1
s1[s1.str.startswith('a')]      # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')]      # s1 각 원소에서 'c'로 끝나는 원소 추출
s1[s1.str.contains('e')]      # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()        # 각 원소의 크기

# count 포함되어 있는 개수
Series(['aabca','abcdsa']).str.count('a')

# 문자열 제거 (제거함수 : 공백, 문자)
Series(['             cd       ','     df        ']).str.strip()
Series(['             cd       ','     df        ']).str.strip().str.len()
s1
s1.str.strip('a')       # 문자열 제거
Series(['aaaabaaca','abcda']).str.strip('a')    # 문자열 제거 (중간값 삭제 불가)
Series(['aaaabaaca','abcda']).str.replace('a','')   # 문자열 제거 (모든 a 삭제)

# find : 위치값 리턴
s3 = Series(['abc@abc.com','abcde@acde.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcded'[0:3]
s3[0:1]     # Series에서 1번째 원소 추출
s3.str[0:3] # Series에서 각 원소마다 1-3번재까지의 문자열 추출

# 예제 : 이메일 아이디 추출
s3 = Series(['abc@abc.com','abcde@acde.com'])
1.
s3.map(lambda x:x[:x.find('@')])
2.
list(map(lambda x,y: x[0:y], s3, s3.str.find('@')))
3.
list(s3.map(lambda x: x[:x.find('@')]))

# 문자열 삽입 pad
s1.str.pad(5,'left','!')
s1.str.pad(5,'right','!')

# 문자열 결합 cat
'a'+'b'
'a'*3
s4 = Series(['abc','def', '123'])
s4.str.cat()                     # >>Series 내 서로 다른 원소 결합
s4.str.cat(sep='/')              # >> Series 내 서로 다른 원소를 구분기호 '/'와 함께 결합

s5 = Series([['a','b','c'],['d','e','f']])
s5.str.join(sep='')              # >> Series 내 같은 원소 내부의 문자열 결합
s5.str.join(sep=',')              # >> Series 내 같은 원소 내부의 문자열 결합할때 구분기호','로 구분

