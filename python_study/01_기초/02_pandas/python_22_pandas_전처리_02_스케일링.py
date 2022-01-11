# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:19:35 2021

@author: sara
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
from pandas.tseries.offsets import Day, Hour, Second
from datetime import timedelta
import matplotlib.pyplot as plt
from numpy import nan as NA
import math


# 22. scailing 스케일링

# 변수 스케일링(표준화)

# 설명변수의 서로 다른 범위를 동일한 범주 내 비교하기 위한 작업 
# - 거리 기반 모델
#   ex) knn, clustering, PCA, SVM, NN 모델 등에 필요
# - 각 설명변수의 중요도를 정확하게 비교하기 위해 요구됨 
# - 이상치에 덜 민감하게 조정

# 스케일링의 종류 

# 1) Standard Scailing
# - 평균을 0, 표준편차 1 로 맞추는 작업

# 2) MinMax Scailing
# - 최소값 0, 최대값 1 로 맞추는 작업

# 3) Robust Scailing
# - 중앙값 0, IQR 1 로 맞추는 작업

# scailing module 불러오기
from sklearn.preprocessing import StandardScaler as standard
from sklearn.preprocessing import MinMaxScaler as minmax

from sklearn.datasets import load_iris

iris_x = load_iris()['data']
iris_y = load_iris()['target']

# 1) standard scailing (표준화) : (x-xbar) / sigma
df1 = (iris_x - iris_x.mean(axis=0)) / iris_x.std(axis=0)
df1.min()
df1.max()

# 함수 사용
m_sc = standard()
m_sc.fit(iris_x)        # fit : 데이터를 모델에 적합하게 해주는 함수
m_sc.transform(iris_x)  # transform : 변환

_df1 = (iris_x - iris_x.mean()) / iris_x.std()
_df1.min()
_df1.max()

# 2) min max scailing (x - x.min())/(x.max()-x.min())
df2 =  (iris_x - iris_x.min(0))/(iris_x.max(0) - iris_x.min(0))
df2.max()
df2.min()

# 함수 사용
m_sc1 = minmax()
m_sc1.fit(iris_x)       # MinMaxScaler() 적합하게 만든다
df2 = m_sc1.transform(iris_x)

df2.max()
df2.min()

# train/test 로 분리되어진 데이터를 표준화
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)

# [시험출제] 1) train_x, test_x 동일한 기준으로 스케일링 (best))
m_sc1 = minmax()

m_sc1.fit(train_x)      # train data set으로만(test set 안건드림) **중요

train_sc1 = m_sc1.transform(train_x)
test_sc1 = m_sc1.transform(test_x)

# 훈련용 데이터에 적용
train_sc1.min(0)
train_sc1.max(0)

# 검증용 데이터에 적용
test_sc1.min(0)     # array([0.02777778, 0.09090909, 0.05263158, 0.        ])
test_sc1.max(0)     # array([0.94444444, 1.09090909, 1.03508772, 0.95833333])

#----------------------------------------------------------------------------------
# >> train과 test의 결과값이 크게 다름 -> 서로 다른 기준으로 스케일링 (bad)
m_sc2 = minmax()
m_sc3 = minmax()

m_sc2.fit(train_x)
m_sc3.fit(test_x)

train_m_sc2 = m_sc2.transform(train_x)
test_m_sc2 = m_sc3.transform(test_x)

train_m_sc2.min(0)
train_m_sc2.max(0)

test_m_sc2.min(0)
test_m_sc2.max(0)
# >> 아래 시각화 이미지를 확인해 보면 변하면 안되는 test값이 바뀌기때문에
#    해당 스케일링은 사용하면 안됨


# scaling 시각화
# 1) figure, subplot 생성
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,3)

# 2) 원본 data의 산점도
import mglearn

ax[0].scatter(train_x[:,0], train_x[:,1], c=mglearn.cm2(0), label='train')
ax[0].scatter(test_x[:,0], test_x[:,1], c=mglearn.cm2(1), label='test')
ax[0].legend()
ax[0].set_title('raw data')


# 3) 올바른 스케일링 data의 산점도(train_sc1, test_sc1)
ax[1].scatter(train_sc1[:,0], train_sc1[:,1], c=mglearn.cm2(0), label='train')
ax[1].scatter(test_sc1[:,0], test_sc1[:,1], c=mglearn.cm2(1), label='test')
ax[1].legend()
ax[1].set_title('good scaing data')


# 4) 잘못된 스케일링 data의 산점도(train_m_sc2, test_m_sc2)

ax[2].scatter(train_m_sc2[:,0], train_m_sc2[:,1], c=mglearn.cm2(0), label='train')
ax[2].scatter(test_m_sc2[:,0], test_m_sc2[:,1], c=mglearn.cm2(1), label='test')
ax[2].legend()
ax[2].set_title('bad scaling data')
