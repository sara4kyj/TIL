# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:37:02 2021

@author: sara
"""

# 조건문과 반복문

# 논리연산자
# and
# or
# not

v1=1
(v1>=3) and (v1<=7) # 3과 7 사이
(v1>=3) & (v1<=7) # 3과 7 사이

(v1<=3) or (v1>=7) # 3보다 작거나 7보다 큼
(v1<=3) | (v1>=7) # 3보다 작거나 7보다 큼

not(v1==1)

# 조건문 if

# 형식
# if 조건 : 
#     참(True)일 때 실행
# else:
#     거짓(False)일 때 실행

# if 조건1 : 
#     조건1이 (True)일 때 실행
# elif 조건2 : 
#     조건1이 거짓(False)이면서 조건2가 참일 때 실행 문장
# else:
#     조건1, 2가 모두 거짓(False)일 때 실행

v1=4

if v1>5:
    print('A')
else:
    print('B')

# 리스트는 불가
l1 = [1,3,5,7,8]
if l1>5:
    print('A')
else:
    print('B')

# 반복문
# 객체의 각 원소에 동일한 연산처리 진행할 경우 사용
# 1. for 문 : 정해진 횟수, 대상이 있을 경우

# for 반복변수 in 반복할 대상(범위):
#     반복 실행할 문장

# 1~10 까지 출력하세요
for i in range(1,11):
    print(i)

# 예제
# 다음의 리스트를 선언하고 5보다 클 경우, 'A', 작거나 같을 경우 'B'
l1 = [1,3,5,15,25]
for i in range(len(l1)):
    if l1[i]>5:
        print('A')
    else:
        print('B')
# or
for i in l1:
    if i>5:
        print('A')
    else:
        print('B')

# l1 리스트에서 각 원소에 10을 더해서 출력
for i in l1 :
    print(i+10)

# l1 리스트에서 각 원소에 10을 더해서 저장해서 출력
l2 = []
for i in l1 :
    l2.append(i+10)
print(l2)


#whie 문 : 조건에 따른 반복을 실행하는 경우

# while 조건:
#     조건이 참일 때 반복 문장
    
# 예제
# while 문으로 1~10까지 출력
i=1
while i<=10:
    print(i)
    i+=1

# 문제
# 1~100 까지 총합
vsum=0
for i in range(1,101):
    vsum+=i # vsum=vsum+i
print(vsum)

vvv=sum(i for i in range(1,101))
print(vvv)

# 1~100 까지 짝수 총합
vsum=0
for i in range(1,101):
    if i%2==0:
        vsum+=i
print(vsum)

vsum=print(sum(i for i in range(0,101,2)))

vsum=0
for i in range(0,101,2):
    vsum+=i
print(vsum)

# 반복제어문
# 1. continue : 특정 조건일 경우 반복문 스킵
# 2. break : 특정 조건일 경우 반복문 종료(정지조건)
# 3. exit : 특정 조건일 경우 프로글매 종료
# 4. pass : 문법적으로 오류가 발생시키지 않기 위해 자리를 채우는 역할

# 예제
# 1~10 출력, 5 제외
for i in range(1,11):
    if i==5:
        continue
    print(i)
    
# break 5    
for i in range(1,11):
    if i==5:
        break
    print(i)
    
# # exit 5    
# for i in range(1,11):
#     if i==5:
#         exit(0)
#     print(i)

# pass test      
v1=1
if v1 > 10:
    pass
else:
    print('b')    
 
# 문제
# 1부터 100까지 누적합이 최초 2000 이상이 되는 시점의 k 값과 총 합을 출력하세요.
vsum=0
for k in range(1,101):
    vsum+=k
    if vsum>=2000:      # 누적합이 2000이상일때 break
        break
print("합은",vsum,"k=",k)
 
    
 
    