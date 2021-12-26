``` python
# 자료구조
# 1. 리스트(기본구조) [1,2]
# 2. 튜플(상수, 불변) (1,2)
# 3. 딕셔너리(key, value) <<- json
# 4. 세트(set) : 집합 set()
# 5. 배열(numpy)
# 6. 판다스 구조 (Series, DataFrame)

# 넘파이(numpy)

import numpy as np
# np.array([1,2,3])   
# array([1, 2, 3]) # 1차원 배열

# np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
# 2차원 배열 (수리적 모형 : 행, 열)

# np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],

#        [[ 7,  8,  9],
#         [10, 11, 12]]])
# 3차원 배열

np.arange(1,26)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#        18, 19, 20, 21, 22, 23, 24, 25])

np.arange(1,26).reshape(5,5)  # reshape 사용시 동일한 수만 가능
np.arange(1,26).reshape(5,-1) # reverce indexing(-1) 사용 시 열 개수 계산 안해도 됨
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

a1 = np.arange(1,26)
type(a1)

# 색인
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array[행 선택, 열 선택]
# a2[1,:]
# array([4, 5, 6])

# 정수 색인 ( 두번째 열 선택 : 차원 축소 발생)
# a2[:,1]
# array([2, 5, 8])

# 슬라이스 색인 (두번째 열 선택 : 차원 축소 발생 안함)
# a2[:,1:2]
# array([[2],
#        [5],
#        [8]])

# a2에서 1,3행 선택
a2[0:3:2,:] # start, end, interbal // 0부터 2(=3-1)[0,1,2로 구성됨]까지 2간격으로 1,3 번째 출력
a2[[0,2],:]
# array([[1, 2, 3],
#        [7, 8, 9]])

# a2에서 1,3열 선택
a2[:,[0,2]]
# array([[1, 3],
#        [4, 6],
#        [7, 9]])

a2
a2[1,1] # 5


# 원하는 값의 위치
# array([[5, 6],
#        [8, 9]])
a2[[1,2],[1,2]] #(오류)array([5, 9]) 
# >>> a2[1,1],a2[2,2] 포인트 인덱싱으로 인식(2개의 포인트(점) 출력)

# (해결코드) 
# 색인함수 (ix_()) 사용하여 해결
a2[np.ix_([1,2],[1,2])]
# array([[5, 6],
#        [8, 9]])

# np.ix_? # ----? : ----에 대한 설명

# 조건 색인
a2>5
# array([[False, False, False],
#        [False, False,  True],
#        [ True,  True,  True]])

a2[a2>5]
# array([6, 7, 8, 9]) True 만 출력

a2[:,0]>5 # 첫번째 컬럼 가져와서 5이상인 행만 선택

a2[a2[:,0]>5] 
# array([[7, 8, 9]])
# 조건의 결과를 행방향에 색인 값으로 전달(차원축소발생안함)

# 3. 메서드
dir(a2)

a2.dtype   # numpy 구성 데이터 타입
a2.shape   # numpy 모양(shape)
a2.shape[0] # numpy 행의 수
a2.shape[1]

a2.reshape(1,9)  # array 모양 변경
a2.ndim          # array 차원

# 4. 연산
[1,2,3]+[4,5,6]
# [1, 2, 3, 4, 5, 6]  # value insert

np.array([1,2,3])+np.array([4,5,6])
# array([5, 7, 9])  # size 동일해야함

# 5. 형(데이터 타입) 변환 메서드

a2.astype('float')
# array([[1., 2., 3.],
#        [4., 5., 6.],
#        [7., 8., 9.]])

a2.astype('int')
a2.astype('str')
# array([['1', '2', '3'],
#        ['4', '5', '6'],
#        ['7', '8', '9']], dtype='<U11')

# 6. np.where 함수
# if 문의 축약
# np. where(조건, 참인 값 반환, 거짓인 값 반환)

# sql 문 기본 형태 :: select * from db where

np.where(a2>5,'A','B')

# 7. 산술 연산 메서드

a2.sum()    # 합
a2.mean()   # 평균
a2.var()    # 분산
a2.std()    # 표준편차
a2.min()    # 최소값
a2.max()    # 최대값

a2>5
# array([[False, False, False],
#        [False, False,  True],
#        [ True,  True,  True]])
(a2>5).sum() # a2메서 5보다 큰 값(true)의 개수(합)
(a2>5).any() # a2에서 5보다 큰 값이 하나라도 있을 경우 참
(a2>5).all() # a2에서 5보다 큰 값이 모두 있을 경우 참

a2.sum(axis=0)  
a2.sum(axis=1)  
# axis 뜻은 축으로 차원의 수로 해석 0 : 1차원(행) / 1 : 2차원(열) / 2 : 3차원(층)

# 8. 전치 메서드
# 1) T : 행과 열을 전치
np.arange(1,9)
a1 = np.arange(1,9).reshape(4,2)
a1
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
a1.T
# array([[1, 3, 5, 7],
#        [2, 4, 6, 8]])

# 2) swapaxes : 두 축을 전달 받아서 두 축을 서로 전치, 전달 순서는 중요하지 않음
a1
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
a1.swapaxes(0,1)
a1.swapaxes(1,0)
# array([[1, 3, 5, 7],
#        [2, 4, 6, 8]])

# 3) transpose
# 원본의 차원에 맞는 축번호를 인수에 차례대로 전달. 그리고 그대로 전치 전달되는 순서 중요
a1.transpose(0,1) # 원본 그래도 출력
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
a1.transpose(1,0) # 행과 열 전치
# array([[1, 3, 5, 7],
#        [2, 4, 6, 8]])

# 외부 파일 입출력
# 1) 파일 불러오기
# np.loadtxt(fname,       # 파일명
#            dtype,       # 데이터 타입    
#            delimiter,   # 필드 구분 기호
#            skiprows,    # skip할 행의 수
#            usecols,     # 선택할 컬럼 값(위치)
#            encoding)    # 인코딩 옵션

import numpy as np
np.loadtxt('.\Downloads\\data_bigdata_cert\\file1.txt', delimiter=',',dtype='str')


# 2) 파일 내려쓰기
# np.savetxt(fname,       # 파일명
#            X,           # 객체명
#            delimiter,   # 구분자
#            fmt,         # 출력형식(format)
#            header,      # 헤더 출력 여부(file 첫 문자열)
#            encoding)    # 인코딩 옵션
a2 = np.arange(0.0,5.0,1.0)
np.savetxt('.\Downloads\\data_bigdata_cert\\file2.txt', a2, delimiter=',', fmt='%s')

# [참고] fmt 전달/변경 방식
# %s : 문자열
# %f : float(실수)
# %d : int(정수)
'%s' % 123
'%f' % 123
'%10.4f' % 123
'%d' % 123
'%7d' % 123
```

