# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:26:49 2021

@author: sara
"""
run my_modules

# 15. stack, unstack, pivot_table
# 자료구조 (데이터타입) 형태
# - long data(tidy data)
# - 각 속성을 컬럼으로 표현

# 지점
# A
# B
# C

# -wide data(cross table : 교차표)
# - 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열함

#            A           B           C
# 판매량

# stack / unstack

# 1. stack
# wide -> long

# 2. unstack
# long -> wide

kimchi = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')


# kimchi 데이터를 연도별, 제품별 수량의 총합
df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()

# 멀티인덱스
# 인덱스나 컬럼이 여러 레벨로 표현
# 상위레벨 : 0, 하위레벨로 갈수록 숫자 증가

df2 = df1.unstack()
df2.stack()             # df2를 wide -> long

df1.unstack(level=0)    # df1를 long -> wide

# pivot_table
# 교차표 작성

kimchi.pivot_table(index = '판매월',               # index 방향에 배치할 컬럼명
                   columns = '판매처',             # column 방향에 배치할 컬럼명
                   values = '수량',                # 교차표에 작성할 값을 갖는 컬럼명
                   aggfunc = 'sum')               # 그룹 함수

# 예제 : kimchi데이터를 이용하여 연도별, 제품별 판매금액의 총 합을 교차표로 작성
kimchi.pivot_table(index='판매년도', columns='제품',values='판매금액', aggfunc='sum')

