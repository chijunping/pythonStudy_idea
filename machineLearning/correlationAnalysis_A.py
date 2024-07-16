"""
@author: chizi
@software: idea
@file: correlationAnalysis.py
@time: 2022/05/26 23:21
@desc: 机器学习：相关性分析
"""
import pandas as pd
import numpy as np
import pandasql
import pendulum as pendulum
import sklearn.datasets as skld
import scipy.stats as st
import os
import pendulum

import datetime

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 300)
path_project = os.path.abspath(os.path.join(os.getcwd(), ".."))
data = pd.read_csv(path_project + '/data/000001.csv')

if __name__ == '__main__':
    data_with_pct_change = pd.DataFrame()
    data_with_pct_change['weekday'] = data['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime("%A"))
    data_with_pct_change['weekday_num'] = data['date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').weekday())


    data_with_pct_change['close_pct_1d'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)
    # data_with_pct_change['close_pct_3d'] = (data['close'] - data['close'].shift(3)) / data['close'].shift(3)
    # data_with_pct_change['close_pct_5d'] = (data['close'] - data['close'].shift(5)) / data['close'].shift(5)
    # data_with_pct_change['close_pct_7d'] = (data['close'] - data['close'].shift(7)) / data['close'].shift(7)
    # data_with_pct_change['close_pct_9d'] = (data['close'] - data['close'].shift(9)) / data['close'].shift(9)
    # data_with_pct_change['close_pct_10d'] = (data['close'] - data['close'].shift(10)) / data['close'].shift(10)
    # data_with_pct_change['close_pct_20d'] = (data['close'] - data['close'].shift(20)) / data['close'].shift(20)
    # data_with_pct_change['close_pct_30d'] = (data['close'] - data['close'].shift(30)) / data['close'].shift(30)
    #
    data_with_pct_change['close_pct_yes_is_add'] = data_with_pct_change.shift(1).close_pct_1d.apply(lambda row: -1 if row<0 else 1)
    data_with_pct_change['close_pct_1d_is_add'] = data_with_pct_change.close_pct_1d.apply(lambda row: -1 if row<0 else 1)
    weekday_group=pandasql.sqldf("select weekday,count(1) from data_with_pct_change where close_pct_1d_is_add=1 group by weekday ")
    weekday_group_num=pandasql.sqldf("select weekday_num,count(1) from data_with_pct_change where close_pct_1d_is_add=1 group by weekday_num ")


# 2 使用pandas中corr()来计算相关性
    coor_pearson = pd.DataFrame(data_with_pct_change).corr(method="pearson")
    print(coor_pearson)
    coor_kendall = pd.DataFrame(data_with_pct_change).corr(method="kendall")
    print(coor_kendall)
    coor_spearman = pd.DataFrame(data_with_pct_change).corr(method="spearman")
    print(coor_spearman)
