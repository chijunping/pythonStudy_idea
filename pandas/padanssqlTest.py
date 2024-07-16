import pandas as pd
import pandasql as psql
import os

# 定义数据路劲
data_path = os.path.abspath(os.path.join(os.getcwd(), "../data"))
df_csv_source = pd.read_csv(data_path + "/test_data.csv")

# 打印df信息
df_csv_source.info()
print(df_csv_source.head())

# 使用pandasql对df进行sql查询
df_sql = psql.sqldf("select date,open,close,high,low,volume,money from df_csv_source limit 10")
print(df_sql)
