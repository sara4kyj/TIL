# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:14:40 2021

@author: sara
"""

a=[1,2,3]
a[2]=4
a

a=[1,2,3,4,5]
del a[2:]
a

a = [1, 2, 3]
a.append(4)
a

a = [1,4,3,2]
a.sort()
a

a = ['a','c','b']
a.reverse()
a

a=[1,2,3]
a.index(3)

a = [4,1,2,3]
a.insert(3,5) # a[3] 위치에 값 5를 삽입
a

a = [1,2,3,1,2,3]
a.remove(3)
a

a = [1,2,3]
a.pop()
a

a = [1,2,3,1]
a.count(1)

a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
a

t1 = (1,2,'a','b')
t1[2]

t1
t1[1:]

t1 = (1,2,'a','b')
t2 = (3,4)
t1+t2

t2*3

t1
len(t1)

a = {1: 'a'}
a[2]=[1,2,3]
a

del a[1]
a

a = {'a':1, 'b':2}
a['a']

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()

for k in a.keys():
    print(k)
    
list(a.keys())

a.values()

a.items()

a.clear()
a

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
a.get('name')
print(a.get('nokey'))  # 여기서 None은 거짓
print(a['nokey'])
a.get('foo','bar')

a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
'name' in a

s1 = set([1,2,3])
s1
s2 = set("hello")
s2
s=set()
s

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
s1&s2
s1.intersection(s2)

s1|s2
s1.union(s2)

s1-s2
s1.difference(s2)

s1 = set([1,2,3])
s1.add(4)
s1

s1 = set([1,2,3])
s1.update([4,5,6])
s1

s1 = set([1,2,3])
s1.remove(2)
s1

a=[1,2,3,4]
while a:
    print(a.pop())

bool('python')
bool('')
bool(0)
bool([])

a=[1,2,3]
id(a) # 저장값 위치 반환

a=[1,2,3]
b=a[:]
a[1]=4
a
b

from copy import copy
a = [1,2,3]
b = copy(a)
b is a

a,b = ('python','life')
print("a is",a,"b is",b)
(a,b)='python1','lefe1'
print("a is",a,"b is",b)
a=b='python'
print("a is",a,"b is",b)
a=3
b=5
a,b=b,a
print("a is",a,"b is",b)


money=3000
cart=True
if money >= 3000 or card:
    print("택시를 타고가라")
else:
    print("걸어가라")
    
'j' not in 'python'

pocket = ['paper','cellphone']
card=False
if 'money' in pocket: print("택시를 타고가라")
elif card: print("택시를 타고가라")
else : print("걸어가라")

prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
number=0
while number != 4:
...     print(prompt)
...     number = int(input())

coffee = 3
money = 300
while money:
     print("돈을 받았으니 커피를 줍니다.")
     coffee = coffee -1
     print("남은 커피의 양은 %d개입니다." % coffee)
     if coffee == 0:
         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
         break
     
        
 a = 0
 while a < 10:
     a = a + 1
     if a % 2 == 0: continue
     print(a)
     
while True:
     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")     
     
test_list = ['one', 'two', 'three'] 
for i in test_list: 
     print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)
     
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)     
     
        
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)     
        
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))  
    
for i in range(2,10):        
     for j in range(1, 10):   
         print(i*j, end=" ") 
     print('')
     
     
result = [x*y for x in range(2,10)
               for y in range(1,10)]
print(result)    
        
     
        
     