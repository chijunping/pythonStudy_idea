"""
@author: chizi
@software: idea
@file: correlationAnalysis.py
@time: 2022/05/26 23:21
@desc: 机器学习：相关性分析
"""
import pandas as pd
import numpy as np
import sklearn.datasets as skld
import scipy.stats as st

X = skld.load_iris().data
print(X)
# 1 使用numpy来求皮尔森相关系数
# rowvar=False时计算的是列与列之间(即随机变量)的相关性
result_1 = np.corrcoef(X, rowvar=False)

# 2 使用pandas中corr()来计算相关性
result_2 = pd.DataFrame(X, columns=['col1', 'col2', 'col3', 'col4']).corr()

# 3 按照皮尔森计算公式来求
result_3 = np.zeros((X.shape[1], X.shape[1]))
for i in range(X.shape[1]):
    for j in range(X.shape[1]):
        std_i, std_j = np.std(X[:, i]), np.std(X[:, j])
        cov_ij = np.mean(X[:, i] * X[:, j]) - X[:, i].mean() * X[:, j].mean()
        result_3[i, j] = cov_ij / (std_i * std_j)

# 4 使用scipy.stats.pearsonr来实现。该函数不仅返回相关系数，还会返回p-value值。
result_4 = np.zeros((X.shape[1], X.shape[1]))
for i in range(X.shape[1]):
    for j in range(X.shape[1]):
        result_4[i, j], _ = st.pearsonr(X[:, i], X[:, j])
