# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def add(a,b):
    return a+b  # 함수 이름은 add이며 입력받은 2개의 값을 합산하여 반환
add(1,3)

def add(a,b):
    return a+b  # a,b는 매개변수
add(1,3)        # 1,3는 인수


def say():
    return 'Hi'
print(say())
# Hi

def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
a = add(3,4)
print(a)
# 3, 4의 합은 7입니다.

def say():
    print('HI')
say()

def add(a,b):
    return a+b  # 함수 이름은 add이며 입력받은 2개의 값을 합산하여 반환
result = add(a=3,b=7)
print(result)
# 10

result = add(b=5,a=3)
print(result)
# 8

def add_many(*args):
    result=0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,5,6,7,8,9,10))
# 55


def add_mul(choice, *args):
    if choice == 'add':
        result=0
        for i in args:
            result+=i
    elif choice == 'mul':
        result=1
        for i in args:
            result*=i
    return result

print(add_mul('add',1,2,3,4,5,6))
# 21
print(add_mul('mul',1,2,3,4,5,6))
# 720

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)                   # 딕셔너리로 출력
# {'a': 1}
print_kwargs(name='foo', age=3)     # 딕셔너리로 출력
# {'name': 'foo', 'age': 3}

