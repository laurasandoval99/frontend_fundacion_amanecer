import pandas as pd
import numpy as np

def show_data():
  df2 = pd.read_csv('Cartera_Final_2.csv',low_memory=False,nrows = 100000)
  df2.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1, inplace = True)
  df2.reset_index()
  df2 = df2[["OBLIGACION",'NRO SOLICITUD','MUNICIPIO CLIENTE', 'MONTO', 'VALOR CUOTA', 'CUOTAS PACTADAS','CUOTAS PENDIENTES', 'CALIFICACION CIERRE', 'VENCIDA', 'DIAS VENCIDO','CAPITAL VEN','MORA', 'FEC ULT.PAGO','FEC PROXIMO PAGO', 'VENCIMIENTO FINAL', 'Fecha']] 
  df2 = df2.groupby("NRO SOLICITUD").max()
  return df2
df2 = show_data()

def load_data():
   df = pd.read_csv('Cartera_Final_2.csv',low_memory=False, nrows=10000)
   df.drop(['Unnamed: 0','Unnamed: 0.1'], axis=1, inplace = True)
   df.reset_index()
   return df

df = load_data()

def cap_vencido():
    cap_ven = df['CAPITAL VEN'].sum()
    return cap_ven

def cap_pendiente():
    cap_pen = df['CP'].sum()
    return cap_pen

pen_pago = list(df['PP'].value_counts())[1]

def deudores_pen():

    total = df['PP'].count()
    por_deudores = (pen_pago/total)*100
    return round(por_deudores,2)






