# %%
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split


import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
import os
# %%
# 깃허브에 준비된 데이터를 가져옵니다.
!git clone https://github.com/taehojo/data.git
# %%
# 집 값 데이터를 불러옵니다.
df=pd.read_csv('./data/house_train.csv')
df
# %%
df.dtypes
# %%
df.isna().sum().sort_values(ascending=False).head(20)
# %%
# 카테고리형 변수를 0과 1로 이루어진 변수로 바꾸어 줍니다.
df=pd.get_dummies(df)
df
# %%
# 결측치를 평균값으로 채우기
df=df.fillna(df.mean())
df
# %%
df.isna().sum().sort_values(ascending=False).head(20)
# %%
df_corr = df.corr()  # 데이터 간의 상관관계
df_corr_sort=df_corr.sort_values('SalePrice',ascending=False)  # 타겟과의 상관관계를 순서대로 정렬
df_corr_sort['SalePrice'].head()  # 타겟값에 대해서만 보기
# %%
df_corr_sort.index.tolist()
# %%
cols=['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF',]
sns.pairplot(df[cols])
plt.show()
# %%
cols_train=['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF']
X_train_pre=df[cols_train]
y=df['SalePrice'].values

X_train,X_test,y_train,y_test = train_test_split(X_train_pre,y,test_size=0.2)
# %%
X_train.shape
# %%

model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(1))
# %%
