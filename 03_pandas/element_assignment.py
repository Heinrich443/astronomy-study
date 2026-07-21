import pandas as pd
import numpy as np

dates = pd.date_range('20260101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)

df.iloc[2, 2] = 1111
print(df)

df.loc['20260103', 'B'] = 2222
print(df)

df[df.A > 8] = 9
print(df)

# 链式赋值，会触发 SettingWithCopyWarning，应避免
# df.A[df.A > 8] = 10
# df[df.A > 8]['A'] = 10

# 正确写法
df.loc[df.A > 8, 'A'] = 10
print(df)

df.loc[df.A > 8, 'B'] = 2
print(df)

# add an empty column
df['F'] = np.nan
print(df)

# add a new column
df['E'] = pd.Series([11, 22, 33, 44, 55, 66], index=dates)
print(df)