import pandas as pd 

diccionarios = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

dataframe = pd.DataFrame.from_dict(diccionarios)
print(type(dataframe))
print(dataframe)