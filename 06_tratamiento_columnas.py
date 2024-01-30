import pandas as pd 

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

dataframe = pd.DataFrame(data)
print(dataframe.head())

print('=========================')

dataframe.columns = ['x','y']

