# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:22:29 2021

@author: sara
"""

# 함수와 메소드
# 함수 : 함수(대상)
# 메서드 :  대상.메소드

# 대소 치환
v1='abcde' # string
v1.upper() # 대문자 치환
'ABCDE'.lower() # 소문자 치환
'abc def'.title() # caml 표기법 (단어의 첫글자만 대문자로 표시)

# 색인(문자열 추출)
'abcd'[0]
'abcd'[-2]
'abcd'[0:3]

'abcd'[:3]
'abcd'[2:]


number = 3
"number is %d" % 3

"hello %s" %"world"
"hello worl%c" %"d"
"%10.4f" % 3.43219876

"number is {0}".format(12)
"number1 is {0}, number2 is {1}".format(11,12)
"number1 is {1}, number2 is {0}".format(11,12)
number1 = 11
number2 = 12
"number1 is {0}, number2 is {number}".format(number1,number=1)
"{0:<10}".format("hi")
"{0:^10}".format("hi")
"{0:>10}".format("hi")
"{0:=^10}".format("hi")
"{0:10.4f}".format(3.43214321)

age = 30
f'나는 내년이면 {age+1}살이 된다.'

 d = {'name':'홍길동', 'age':30} # 딕셔너리
 f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
 
 f'{"hi":<10}'   # 왼쪽 정렬
 f'{"hi":>10}'   # 오른쪽 정렬
 f'{"hi":^10}'   # 가운데 정렬

f'{"hi":=^10}'   # 가운데 정렬하고 "=" 문자로 공백 채우기
f'{3.43214321:10.4f}'   # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

'apple'.count('p')
'apple'.find('e')
'apple'.find('b')
'apple'.index('e')
'apple'.index('b')

",".join('abcd')
",".join(['a','b','c','d'])

'abcd'.upper()
'ABCD'.lower()

'  hi  '.lstrip()
'  hi  '.rstrip()
'  hi  '.strip()

'  hi  '.replace(" ","")
'a:b:c:d'.split(":")

l1 = [1, 2, 3, 4]
l1

a = [1,2,3,['a','b','c']]
a[-1][0]

a=[1,2,['a','b',['life','is']]]
a[2][2][0]

a=[1,2,3,['a','b','c'], 4,5]
a[3][:2]
a[2:5]
# ex) '031)345-0834' 에서 지역번호만 추출
vtel = '031)345-0834'
vtel[0:3]

# 문자열의 시작, 끝 여부 확인
# v1.startwith(prefix,  # 시작 값 확인 문자
#              start,   # 확인할 시작 위치
#              end)     # 확인할 끝 위치    

v1
v1.startswith('b')
v1.startswith('b',1)
v1[1:].startswith('b',1)

# v1.endswith(suffix,
#             start,
#             end)

v1
v1.endswith('e')
v1.endswith('E')

# 앞 뒤 공백 또는 문자 제거
'abc' == 'abc'
' abc '.strip() # 양쪽 공백 제거
'abc'.strip('a') # 문자 제거
'abaca'.strip('a') # 양쪽 끝 문자 제거(중간 글자 삭제 불가)

' abcd '.lstrip() # 왼쪽 공백 또는 글자 제거
' abacd '.rstrip() # 오른쪽 공백 또는 글자 제거

# 치환
# 'abcabc'.replace(old,  # 찾을 문자열
#                  new)  # 바꿀 문자열
'abcabc'.replace('a','A')
'abcabc'.replace('ab','AB')
'abcabc'.replace('ab','')

# 문자열 분리
# v1.split(sep) # 분리 구분기호
'a/b/c/d'.split('/')
'a/b/c/d'.split('/')[1]
'a/b/c/d'.split('/')[0:1]

# 위치값 리턴
# 'abcd'.find(sub,    # 위치값을 찾을 대상
#             start,  # 찾을 위치(시작점)
#             end)    # 찾을 위치(끝점)

v1
v1.find('b')

# ex. 전화번호에서 지역번호 추출
# ')' 위치를 확인해서 그 이전까지 추출
vtel
vnum = vtel.find(')')
vtel[:vnum]

# 포함 횟수
'abcabcabc'count('a')

# 형(type) 확인
type(v1)    # date type 확인
v1.isalpha()    # 문자 확인
v1.isnumeric()  # 숫자 확인
v1.isupper()    # 대문자 확인
v1.islower()    # 소문자 확인

# 문자열 결합
'a'+'b'
a = [1,2,3]
b = [4,5,6]
a+b
a = [1,2,3]
a*3

a = [1,2,3]
len(a)

a=[1,2,3]
a[2]+"hi"

str(a[2])+"hi"

#문자열 길이
len(v1)
3/len(v1)

# 연습문제
vname='deokku'
vmail='deokku04@gmail.com'
jumin='900101-2222222'

# 1. 이름의 두번째 글자가 m인지 여부 확인
vname[1]=='m'
vname[1]=='e'

# 2. vemail에서 이메일 아이디만 추출
vmailnum=vmail.find('@')
vmail[:vmailnum]

# 3. 주민번호에서 여자인지 확인 (참고 : 1남자 2여자 )
# jumin[7]=='2'
jumin
jumin.split('-')[1][0] == '2' 
# >> '-' 기준으로 나눠서 [1]열의 [0]의 값과 '2'가 같은가