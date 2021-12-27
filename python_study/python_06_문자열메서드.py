# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:15 2021

@author: sara
"""

# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')
'a/b/c'.split('/')[1]

l1 = ['abc','def']
l2 = ['a/b/c','d/f/e']

l1.upper() # 불가
l2.split() # 불가

# >> 해결 map
list(map(lambda x: x.upper(),l1))
list(map(lambda x: x.split('/'),l2))


list(map(lambda x: x.split('/')[1],l2)) # 불가

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split

from pandas import Series, DataFrame

l1

s1=Series(l1)
s2=Series(l2)

s2.str.split('/')

# 2) 대소 치환
s1.str.upper()
s1.str.lower()
s1.str.title()

# 3) replace
s1.str.replace('a','A')
s1.str.replace('a',' ') 


# 예제 - 천단위 구분기호 처리 s3의 합을 출력

s3=Series(['1,200','3,000','4,000'])
s3.str.replace(',','').astype('int').sum()


# 4) 패턴 확인 : startswith, endswith, contains
s1.str.startswith('a')  # s1의 문자열 중 a 여부에 따라 true/false 출력
s1[s1.str.startswith('a')]  # s1의 문자열 중 a로 시작하는 원소 추출
s1[s1.str.endswith('c')]  # s1의 문자열 중 c로 끝나는 원소 추출
s1[s1.str.contains('e')]  # s1의 문자열 중 e를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()

# count 포함 개수
Series(['aabbbb','abcdadd']).str.count('a')

# 제거 함수 (공백, 문자)
Series(['      cd         ','              df          '])
Series(['      cd         ','              df          ']).str.strip()
Series(['      cd         ','              df          ']).str.strip().str.len()

s1.str.strip('a')
Series(['aaaadbadcd','adbdadcdda']).str.strip('a')
# >> 중간값 제거 안됨
Series(['aaaadbadcd','adbdadcdda']).str.replace('a','')
# >> 문자열 중간값 제거 가능

# find(위치값 return)
s3 = Series(['abcde@hanmail.com','abseghd@gmail.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcde'[0:3]
s3[0:3]
s3.str[0:3]

# 이메일 아이디 추출
s4 = Series(['drwill@naver.com','zzuyu11@drwill.kr'])
# 1.
list(map(lambda x,y: x[0:y], s4, s4.str.find('@')))
# 2.
s4.map(lambda x:x[:x.find('@')])


# pad : 문자열 삽입
s1.str.pad(5,       # 총 자리수
           'left',  # 삽입 방향
           '!')     # 삽입 글자 

s1.str.pad(5,'left','!')
# 0    !!abc
# 1    !!def
# dtype: object

s1.str.pad?

s5 = Series(["I Love you","You know"])
s5.str.pad(20,'right','^')

# 문자열 결합
s4=Series(['abc','def','123'])
s4.str.cat()
s4.str.cat(sep='/')

# Series(['a','b','c'],index = ['drwill','zzuyu','hyory'])
# Series(['a','b','c'],['drwill','zzuyu','hyory'])
s6 = Series([['a','b','c'],['d','e','f']])
s6
s6.str.join(sep='/') # Series 내 각 원소 내부의 문자열을 결합 (/)


