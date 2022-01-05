# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:57:55 2022

@author: sara
"""

run my_modules

# 1. 평균점수
a = [80,75,55]
sum(a)/len(a)

# 2. 홀짝 판별
13%2    # 1를 출력하면 홀수, 0을 출력하면 짝수

# 3. 주민번호 슬라이싱
jumin = '881120-1234567'
print("주민 연월일 : ", jumin[:6], "뒷번호 :", jumin[7:])

# 4. 성별을 나타내는 숫자 출력
pin = '881120-1068234'
print(pin[7])

# 5. : -> # 교체
a = "a:b:c:d"
a.replace(':','#')

# 6. 정렬
a = [1,3,5,4,2]
a.sort()
print(a)

# 7. join
' '.join(['Life', 'is', 'too', 'short'])

# 8. tuple 더하기
t1 = (1,2,3)
t2 = 4,
t1+t2

# 9. 오류가 발생하는 경우
a = dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python'       # list가 아니라 dict이기 때문에
a[250] = 'python'

# 10. 'B'에 해당되는 값 추출
a = {'A':90, 'B':80, 'C':70}
a.pop('B')

# 11. 중복숫자 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aset=set(a)     # set 특성 : 중복 금지, 순서가 없음
a = aset
print(a)

# 12.  
a = b = [1, 2, 3]
a[1] = 4
print(b)
# >> a와 b 둘 다 동일한 리스트 객체를 가리키고 있기 때문