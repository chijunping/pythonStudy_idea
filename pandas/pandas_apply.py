import numpy as np
import pandas as pd


def apply_col5(row, df):
    row_index = row.name
    index_from = 0 if (row_index - 5) < 0 else (row_index - 5)
    df_sub = df.iloc[index_from:row_index + 1]
    df_sub[df_sub['col4'] > df_sub['col3']].count().col1
    return df_sub.tail(3)['col4'].max()


df = pd.DataFrame(np.arange(40).reshape(10, 4))
df.columns = ['col1', 'col2', 'col3', 'col4']
print(df)
#
df['col5'] = df.apply(lambda row: apply_col5(row, df), axis=1)
print(df)
exit()
