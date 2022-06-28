import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def load_data():
   df = pd.read_csv('data/Cartera_Final_2.csv',low_memory=False, nrows=10000)
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


def load_data2():
    df2 = pd.read_csv('data/Data_Final.csv', sep=",",encoding="utf-8",low_memory=False,index_col=0)
    # Dar formato de fecha
    df2['FECHA'] = pd.to_datetime(df2['FECHA'], format = "%Y-%m" )
    return df2

df2 = load_data2()

def indicadores():
    df_ultimo  =  df2[df2['FECHA'] == df2['FECHA'].max()]

    # Indicador 1: Total capital vencido
    a = df_ultimo['CAPITAL_VEN'].sum()

    # Indicador 2: Cantidad de clientes que estan en mora
    b = df_ultimo['DEUDOR'].sum()/df_ultimo['DEUDOR'].shape[0]

    # Indicador 3: Total por pagar
    c = df_ultimo['SALDO_OBLIGACION'].sum()
    return df_ultimo

df_ultimo = indicadores()

def porcentajes():
    df_tiempo = df2.groupby('FECHA').agg(CAPITAL_VENCIDO= ('CAPITAL_VEN','sum'),
                                     DEUDOR_SUMA = ('DEUDOR','sum'),
                                     DEUDOR_COUNT= ('DEUDOR','count'),
                                     SALDO_TOTAL= ('SALDO_OBLIGACION','sum'))
    #Poner clientes en mora en porcentajes
    df_tiempo['CLIENTES_MORA'] = df_tiempo['DEUDOR_SUMA']/df_tiempo['DEUDOR_COUNT']
    df_tiempo = df_tiempo.reset_index()
    return df_tiempo

df_tiempo = porcentajes()

#sns.lineplot(x='FECHA',y='CAPITAL_VENCIDO',data=df_tiempo,palette='Set1', ci = None, legend='brief')


