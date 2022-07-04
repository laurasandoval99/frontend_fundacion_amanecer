import pandas as pd
from datetime import datetime
import numpy as np

#cargando el data frame
df = pd.read_csv('data/Data_Final.csv', sep=",",encoding="utf-8",low_memory=False,index_col=0)

# Dar formato de fecha
df['FECHA'] = pd.to_datetime(df['FECHA'], format = "%Y-%m" )

# df para prueba de la reg logistica
df_prueba = pd.read_csv('data/prueba_reglog.csv')


# calculando indicadores ultimo mes de carga
def ind_ult_mes():

    # Dataframe ultimo mes registrado
    df_ultimo = df[df['FECHA'] == df['FECHA'].max()]

    x = str(df['FECHA'].max())
    j = x.rsplit(" ")
    f_cierre = j[0]

    # Indicador 1: Total capital vencido en el ultimos mes registrado
    cap_ven = df_ultimo['CAPITAL_VEN'].sum()

    # Indicador 2: porcentaje de clientes que estan en mora en el ultimos mes registrado
    por_mora = round(df_ultimo['DEUDOR'].sum()/df_ultimo['DEUDOR'].count(),2)*100

    # Indicador 3: Total por pagar en el ultimo mes registrado
    tot_saldo = df_ultimo['SALDO_OBLIGACION'].sum()

    return cap_ven, por_mora, tot_saldo, f_cierre


# Agrupar por fecha y variables de interes para los graficos de serie de tiempo
def inicio_graph(filter2):

    df_tiempo = df.groupby(['FECHA',filter2],as_index=False).agg(CAPITAL_VENCIDO= ('CAPITAL_VEN','sum'),
                                     DEUDOR_SUMA = ('DEUDOR','sum'),
                                     DEUDOR_COUNT= ('DEUDOR','count'),
                                     SALDO_TOTAL= ('SALDO_OBLIGACION','sum'))

    #Poner clientes en mora en porcentajes
    df_tiempo['CLIENTES_MORA'] = df_tiempo['DEUDOR_SUMA']/df_tiempo['DEUDOR_COUNT']

    return df_tiempo