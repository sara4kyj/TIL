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
