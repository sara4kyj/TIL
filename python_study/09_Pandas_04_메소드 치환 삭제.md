```python
# replace 메서드_치환, 삭제

# replace 메서드
# 치환(찾을 문자열, 바꿀 문자열)

# 1. 기본 문자열 메서드
# - 파이썬에서 기본제공
# - 문자열에서 호출 가능
# - 벡터 연산(각 원소별 반복 처리) 불가
# - 오직 문자열 치환만 가능(숫자치환, NA 치환 불가)

'abcd'.replace('a','A')     # >> 'a'를 'A'로 치환
'abcd'.replace('a','')      # >> 'a'를 공백으로 치환
'abcd1'.replace('1','')     # must be str

['abcd','abcde','aabb'].replace(',','')     # list no attribute >> use map

# for 문 활용
outlist=[]
for i in ['abcd','abcde','aabb']:
    outlist.append(i.replace('a','A'))
    
print(outlist)

# map
f1 = lambda x : x.replace('a','A')
list(map(f1,['abcd','abcde','babb']))

from pandas import Series, DataFrame
['abcd','abcde','aabb'].map(f1) # 호출불가
Series(['abcd','abcde','aabb']).map(f1)

import numpy as np
Series(['abcd','abcde','aaaab', np.nan]).map(lambda x : x.replace(np.nan, ''))
# >> TypeError: replace() argument 1 must be str, not float
# 문자열(str)이어야 함

# 2. str.replace
# - pandas 제공(Series 객체만 호출 가능)
# - 벡터화 내장된 문자열 메서드
# - 문자열 호출 가능
# - 벡터 연산(각 원소별 반복 처리) 가능
# - 오직 문자열 치환만 가능(숫자치환, NA 치환 불가)
# - 숫자로 구성된 Series 적용 불가

Series(['abcd','abcde','aaaab']).str.replace('a', 'A')
DataFrame(['abcd','abcde','aaaab']).str.replace('a', 'A')       
# >> error / 데이터의 형태가 DataFrame이기 때문에 str.repalce 사용불가
['abcd','abcde','aaaab'].str.replace('a', 'A')                 
# >> error / 데이터의 형태가 list이기 때문에 str.replace 사용 불가

# pandas replace
# - pandas 제공
# - 값 치환 메서드(똑같은, 완전히 일치하는 값을 다른 값으로 대체, 삭제)
# - Series, DataFrame 호출 가능
# - 숫자, NaN 치환 가능
# - 동시에 여러 대상 수정 가능

df1 = DataFrame([['1,200', '1,300'],['1,400', '1,500']])

df1.replace(',','')     # >> 변화없음 / why 완전히 일치하는 값을 다른 값으로 대체하는 것이기 때문에

df2 = DataFrame([['1,200', ','],['1,400', '1,500']])
df2.replace(',','')     # >> 변화없음 

df3 = DataFrame([['1200', '1300'],['1400', '.']], columns = ['a','b'])
df3
df3.replace(['.','1400','?','!'], np.nan)

# [연습문제]
# df1에 천단위 구분기호 제거 후 모두 숫자(int형)로 변경
df1 = DataFrame([['1,200', '1,300'],['1,400', '1,500']])

# applymap 함수 사용
# scala에서는 문자열이 아닌 숫자로 변경해야함
df1.applymap(lambda x: int(x.replace(',',''))).sum()

df.applymap?

df1 = DataFrame([['1,200', '1,300'],['1,400', '1,500']])
copy_df1=df1
for i in range(0,len(df1)):
    copy_df1[i] = df1[i].str.replace(',','').astype('int')
print(copy_df1)
```

