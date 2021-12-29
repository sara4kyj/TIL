# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:17:15 2021

@author: sara
"""

# pandas example

run my_modules

df1 = pd.read_csv('./data/cancer_test.csv')
df1.columns
df1.dtypes

df1.head()
df1.info()
df1.describe()


# 'radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'
# NA인 행을 제거한 후 총 행의 수 리턴

df1['radius_mean'].isnull().sum()       # NA -> 4
df1['texture_mean'].isnull().sum()      # NA -> 4
df1['texture_se'].isnull().sum()        # NA -> 4
df1['smoothness_se'].isnull().sum()     # NA -> 4

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() & df1['smoothness_se'].isnull()
vbool.sum()     # 컬럼 4개가 모두 NA인 행의 수

df1
df1.loc[vbool, :]   # 컬럼 4개가 모두 NA인 행 확인

df1.shape   # (569, 32)
df1.shape[0]    # 행의 갯수
df1.shape[1]    # 열의 갯수

df1.shape[0]-vbool.sum()

print(df1.shape[0]-vbool.sum())

# dropna
df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all')
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all').shape[0]
print(nrow)

# 2. concavity_mean의 standard scaling(표준화) 후, 결과가 0.1 이상인 값의 개수 출력
# standard scaling(표준화) = (원 데이터 - 평균) / 표준편차
# minmax scaling = (원데이터 - 최소)/(최대-최소)

df1.columns
vscale = (df1['concavity_mean']-df1['concavity_mean'].mean()) / df1['concavity_mean'].std()

(vscale>0.1).sum()

# 이상치 건 수 확인
# 3. textur_se의 상위 10% 값(NA를 제외한 건수의 10%)을 이상치로 가정한다.
#       10% 제외한 값을 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력
df1 = pd.read_csv('./data/cancer_test.csv')

# 이상치 건수 확인
df1['texture_se'].dropna()

df1['texture_se'].shape[0]                                          # 569
df1['texture_se'].dropna().shape[0]                                 # 565
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1))       # 56
type(nx)

# 이상치를 제외한 나머지 >> 평균
df1['texture_se'].rank(ascending = False, method='first')
vrank = df1['texture_se'].rank(ascending = False, method='first')
vrank

df1.loc[vrank > nx, 'texture_se']                   # 정상치 데이터
vmax = df1.loc[vrank > nx, 'texture_se'].max()      # 정상치 데이터 최대값

# 이상치 데이터를 vmax(정상치 데이터 최대값)으로 치환
df1.loc[vrank <= nx, 'texture_se'] = vmax

round(df1['texture_se'].mean(), 2)          # texture_se의 평균을 소수점 2자리까지 반올

df1.loc[vrank <= nx, 'texture_se']          # 이상치 데이터

# 4. symmetry_mean의 결측치를 최솟값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력해주세요.
from numpy import nan as NA

df1 = pd.read_csv('./data/cancer_test.csv')

df1['symmetry_mean'].min()      

# string 존재 >> 예외처리
df1['symmetry_mean'] = df1['symmetry_mean'].replace('-',NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('.',NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('pass',NA)
df1['symmetry_mean'] = df1['symmetry_mean'].replace('<=',NA)

df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')
vmin = df1['symmetry_mean'].min() 

# 결측치 수정
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

print(round(df1['symmetry_mean'].mean(),2))
