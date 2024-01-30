import pandas as pd

def convertir_a_datetime(fecha_cadena):
    return pd.to_datetime(fecha_cadena, format='%Y-%m-%d')

data = {
    'fechas_nacimiento': [
        '1998-07-20',
        '1994-01-10',
        '1996-02-07',
        '1992-02-08',
        '1995-09-20',
        '1996-02-17',
        '1997-11-27',
        '1997-09-16',
        '1989-07-24'
    ]
}

dataframe = pd.DataFrame(data)
print(dataframe.head())
print('-------------------')

dataframe['fecha_datetime'] = dataframe['fechas_nacimiento'].map(convertir_a_datetime)
print(dataframe.dtypes)







