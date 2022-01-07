# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:01:08 2022

@author: sara
"""

# 다차원 척도법(MDS)
# - 개체들 사이의 유사성, 비유사성을 거리로 측정하여 2차원/3차원 공간상에
#   점으로 표현하는 기법
# - 개체들 사이의 집단화를 시각적으로 표현하는 분석방법
# - 차원 축소과정에서 발생하는 오차(stress) 정의 
# - stress 크기로 차원 축소에 대한 적합도 판단
# - stress(0: 완벽, 5: 좋음, 10: 보통, 20: 나쁨)

from sklearn.manifold import MDS 

# 1. data loading 
from sklearn.datasets import load_iris
iris_x = load_iris()['data']
iris_y = load_iris()['target']

iris_x  # 변수가 4개 -->> 4차원 

# 2. Scailing 정규화
from sklearn.preprocessing import StandardScaler as standard
m_sc = standard()
iris_x_sc = m_sc.fit_transform(iris_x)
# PCA 적용 전 스케일링 변환 

m_mds2 = MDS(n_components=2)
m_mds3 = MDS(n_components=3)


# 3. 데이터 변환
iris_x_mds1 = m_mds2.fit_transform(iris_x_sc)
iris_x_mds2 = m_mds3.fit_transform(iris_x_sc)

# 4. 유도된 인공변수 확인
m_mds2.stress_          # 적합도 평가(.stress_)
m_mds2.embedding_       # 변환된 데이터셋 값

# 변환된 데이터 셋 값 ---> points 변수에 담기
points = m_mds2.embedding_


# 5. 크루스칼 스트레스 계산

import numpy as np
from sklearn.metrics import euclidean_distances

DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)         # 실제 거리

stress = 0.5*np.sum((DE-DA)**2)
stress1 = np.sqrt(stress/(0.5*np.sum(DA**2)))

print('stress : ', stress)
print('stress1 : ', stress1)
# stress :  3530.715857794239
# stress1 :  0.18586347781890689

# 3차원
m_mds3.stress_          # 적합도 평가(.stress_)
m_mds3.embedding_       # 변환된 데이터셋 값

points2 = m_mds3.embedding_

DE2 = euclidean_distances(points2)
DA2 = euclidean_distances(iris_x)  

stress_2 = 0.5*np.sum((DE2-DA2)**2)
stress1_2 = np.sqrt(stress_2/(0.5*np.sum(DA2**2)))

print('stress_2 : ', stress_2)
print('stress1_2 : ', stress1_2)
# stress_2 :  3381.6129873339823
# stress1_2 :  0.18189661894886347