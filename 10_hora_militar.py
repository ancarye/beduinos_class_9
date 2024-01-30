#hora milirar
#0700 horas es igual 7 am
#1200 horas son las 12 horas
import pandas as pd 

def convertir_a_date_time(hora_militar):
    hora_militar = hora_militar.zfill(4)
    horas = int(hora_militar[:2])
    minutos = int(hora_militar[2:])
    hora_completa = f'{horas:02d}:{minutos:02d}'

    return pd.to_datetime(hora_completa,format='%H:%M')

data = {
    'hora_militar': ['0700', '0900','1200','1500'],
    'actividades':['desayuno','ejercicio','lectura','comida']
}

dataframe = pd.DataFrame(data)
print(dataframe.head())

print('---------------------')

dataframe['fecha_hora']= dataframe['hora_militar'].map(convertir_a_date_time)
print(dataframe.head())