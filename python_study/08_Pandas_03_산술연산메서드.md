```python
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))

dir(df1)    # 도움말

df1
df1.sum(axis=0) # 행별(서로 다른 행끼리)
df1.sum(axis=1) # 컬럼별(서로 다른 열끼리)

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()

df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()
# skipna = True (default) 자동으로 NaN 무시하고 연산

# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].mean()
df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()		# df1의 1번째열의 모든 값들 중 NaN이 있다면 df1의 1번째열의 평균으로 저장
df1

df1[df1.isnull()]   # 데이터 프레임 전체에서 NaN 값 확인

df1.iloc[:,0].var() # 분산
df1.iloc[:,0].std() # 표준편차
df1.iloc[:,0].min() # 최소값
df1.iloc[:,0].max() # 최대값
df1.iloc[:,0].median() # 중위수(중앙값)

(df1.iloc[:,0] >= 10).sum() # 조건에 만족하는 개수 확인
```

