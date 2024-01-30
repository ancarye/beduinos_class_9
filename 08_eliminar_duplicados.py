import pandas as pd

data = {'A': [1, 2, 2, 3, 4], 'B': ['x', 'y', 'y', 'z', 'z']}
dataframe = pd.DataFrame(data)

print(dataframe.head())
print('-----------------------')

duplicates_in_A = dataframe[dataframe.duplicated(subset='A')]
print(duplicates_in_A)

print('---------------------------')

no_duplicates_in_A = dataframe.drop_duplicates(subset='A')
print(no_duplicates_in_A)