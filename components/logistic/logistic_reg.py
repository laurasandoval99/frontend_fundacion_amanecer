from dataclasses import dataclass
import pandas as pd
import dash_bootstrap_components as dbc
from components.table.table import table
import numpy as np
import joblib 

# Global variables
model = 'Models/modelo_reglog1.data'
#loading the model
modelo_reglog= joblib.load(model)
p_optimo= 0.1304755233950338

def predictor(   v1,v2,v3,v4,v5,v6,v7,
                v8,v9,v10,v11,v12,v13,v14,
                v15,v16,v17,v18,v19,v20,v21,
                v22,v23,v24,v25,v26,v27,v28,v29,
                model,
                P): # entradas del modelo
    
    l = model.params  # coeficientes del modelo
    v = [v1,v2,v3,v4,v5,v6,v7,
        v8,v9,v10,v11,v12,v13,v14,
        v15,v16,v17,v18,v19,v20,v21,
        v22,v23,v24,v25,v26,v27,v28,v29]  # lista de las entradas
    b = l[0] #intercepto
     
    c=np.log(P/(1-P))
    
    for x in range(1,len(model.params)):
       
    
        b = b + (l[x]*v[x-1])
    
    d = b > c
    
    return d


def prediccion(data):
    df_PRE = data
    modelo = modelo_reglog
    p_val = p_optimo

    df_PRE["INCUMPLIMIENTO_PREDICT"] = df_PRE[['UBICACIO_CLIENTE',
                                               'MONTO',
                                               'CUOTAS_PACTADAS',
                                               'CUOTAS_PENDIENTES',
                                               'SALDO_OBLIGACION',
                                               'TASA_NOM_ANUAL',
                                               'GENERO',
                                               'EDAD',
                                               'REGION_REGION CENTRO',
                                               'REGION_REGION CENTRO BOYACA',
                                               'REGION_REGION CENTRO NORTE',
                                               'REGION_REGION META',
                                               'REGION_REGION NORTE',
                                               'REGION_REGION SUGAMUXI',
                                               'REGION_REGION SUR',
                                               'REGION_REGION TUNDAMA',
                                               'REGION_REGION VILLAVICENCIO',
                                               'CALIFICACION_CIERRE_B',
                                               'CALIFICACION_CIERRE_C',
                                               'CALIFICACION_CIERRE_D',
                                               'CALIFICACION_CIERRE_E',
                                               'TIPO_CREDITO_PARALELO',
                                               'TIPO_CREDITO_RENOVADO',
                                               'TIPO_CREDITO_RETANQUEADO',
                                               'TIPO_CREDITO_SIN_PERFIL',
                                               'NIVEL_DE_ESTUDIOS_NEW_Desconocido',
                                               'NIVEL_DE_ESTUDIOS_NEW_Media',
                                               'NIVEL_DE_ESTUDIOS_NEW_Ninguno',
    'NIVEL_DE_ESTUDIOS_NEW_Superior']].apply(lambda x: predictor(x[0], x[1], x[2], x[3], x[4], x[5], x[6],
                                            x[7], x[8], x[9], x[10], x[11], x[12], x[13],
                                            x[14], x[15], x[16], x[17], x[18], x[19], x[20],
                                            x[21], x[22], x[23], x[24], x[25], x[26], x[27], x[28], modelo, p_val), axis=1)

    pred = df_PRE[["INCUMPLIMIENTO_PREDICT", 'INCUMPLIMIENTO']].reset_index()
    pred.rename(columns={'index':'COD_CLIENTE'}, inplace=True)
    pred
    columnas = list(pred.columns)
   
    # devolviendo la tabla
    params1 = {
    'title': 'Predicción de incumplimiento de pago usando regresión logística',
    'description': 'prediccion para 20 clientes aleatorios',
    'columns': columnas
    }
    tabla_prediccion = table(pred, params1)

    layout = dbc.Row(children=[
        tabla_prediccion.display()
    ],className='card border-success', style={'offset':2})

    return layout
