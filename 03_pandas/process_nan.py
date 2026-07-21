import pandas as pd
import numpy as np

dates = pd.date_range('20260101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)

# drop the row or column which contain NaN
print(df.dropna())      # default: axis=0, how='any'
print(df.dropna(axis=0, how='any'))
print(df.dropna(axis=0, how='all'))
print(df.dropna(axis=1, how='any'))
print(df.dropna(axis=1, how='all'))

# fill elements which is NaN
print(df.fillna(value=0))

# 判断是否包含 NaN
print(df.isnull())
print(np.any(df.isnull()) == True)
