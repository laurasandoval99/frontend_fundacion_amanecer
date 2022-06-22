import pandas as pd
import numpy as np

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






