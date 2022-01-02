# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 함수의 구조
def add(a,b):
    return a+b  # 함수 이름은 add이며 입력받은 2개의 값을 합산하여 반환
add(1,3)


# 매개변수와 인수
def add(a,b):
    return a+b  # a,b는 매개변수
add(1,3)        # 1,3는 인수

# 입력값과 결과값에 따른 함수의 형태
# - 입력값이 없는 함수
def say():
    return 'Hi'
print(say())
# Hi

# 결과값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
a = add(3,4)
print(a)
# 3, 4의 합은 7입니다.

# 입력값도 결과값도 없는 함수
def say():
    print('HI')
say()

# 매개변수 지정하여 호출하기
def add(a,b):
    return a+b  # 함수 이름은 add이며 입력받은 2개의 값을 합산하여 반환
result = add(a=3,b=7)
print(result)
# 10

result = add(b=5,a=3)
print(result)
# 8

# 여러개의 입력값을 받는 함수
def add_many(*args):
    result=0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,5,6,7,8,9,10))
# 55

# 하나의 매개변수와 여러개의 입력값을 받는 함수
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

# 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)                   # 딕셔너리로 출력
# {'a': 1}
print_kwargs(name='foo', age=3)     # 딕셔너리로 출력
# {'name': 'foo', 'age': 3}

# return이 두가지 반환값을 가지는 경우
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result, type(result))        # tuple로 저장됨
result1, result2 = add_and_mul(3,4)     # return값에 각각의 변수를 지정하여 int로 저장
print(result1, type(result1), result2, type(result2))

# 두개의 return을 가지는 경우
def add_and_mul(a,b):
    return a+b          # 함수는 return문을 만나면 결과값을 반환 후 함수 탈출
    return a*b          # 따라서 위에서 이미 함수는 끝났으므로 해당 return문은 무소용
result = add_and_mul(2,3)
print(result)

# 함수 내부의 구문안에 return을 가지는 경우
def say_nick(nick):
    if nick == '바보':
        return              # '바보'를 입력하면  return값 없이 함수 종료
    print('나의 별명은 %s입니다.' % nick)
say_nick('야호')
say_nick('바보')

# 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself('박응용', 27)

# 함수안에서 선언한 변수의 효력범위
def vartest(a):
    a = a + 1

vartest(3)
print(a)        # 여기서 a는 정의된 적이 없으므로 defined error 발생
# NameError: name 'a' is not defined

# return를 사용하여 함수 안에서 함수 밖의 변수 변경
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a)  # a를 vartest의 결과값으로 저장
print(a)

# global를 사용하여 함수 안에서 함수 밖의 변수 변경
a = 1 
def vartest(): 
    global a        # 함수내에서 함수 밖의 a 변수를 직접 사용
    a = a+1

vartest() 
print(a)

# lambda
add = lambda a, b : a+b
print(add(3,4))