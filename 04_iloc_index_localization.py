import pandas as pd

ENCODING = 'ISO-8859-1'

dataframe = pd.read_csv('datasets/car_crashes.csv', encoding=ENCODING)

print(dataframe.size)

print(dataframe.iloc[5000])

print(dataframe.columns)