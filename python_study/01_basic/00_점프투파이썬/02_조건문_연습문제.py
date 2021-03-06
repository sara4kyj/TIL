# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:42:02 2022

@author: sara
"""

# Q1. 다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# >>shirt
# 3번째 조건문에 해당되므로 shirt만 출력

# Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
i=1
result=0
while i < 1001:
    if i % 3 == 0:
        result = result + i
    i = i + 1
print(result)

# Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****

a='*'
i=1
while i <= 5:
    print(a*i)
    i=i+1

# Q4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

i_sum=0
for i in range(1,101):
    i_sum = i_sum + i
print(i_sum)
# >>5050

# Q5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
a_sum=0
for i in a:
    a_sum = a_sum + i
    i = i + 1
print(a_sum/len(a))    
# >> 79.0

# Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# 아래 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
numbers = [1, 2, 3, 4, 5]
result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
result = [n*2 for n in numbers if n % 2 == 0]
print(result)
