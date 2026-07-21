import pandas as pd

# import
data = pd.read_csv('xxx.csv')
print(data)

# export
data.to_pickle('xxx.pickle')