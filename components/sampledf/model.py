import pandas as pd

# dataset de prueba para el mapa
df = pd.read_csv('data\Data_final.csv',low_memory=False, 
    dtype = { # indicate categorical variables
        'NRO SOLICITUD':'object',
        'COD MODALIDAD':'object',
        'NOM TIPOCLIENTE': "category",
        "SUCURSAL": "category",
        'REGION': "category",
        'UBICACIO CLIENTE': "category", 
        'PERIODICIDAD': "category",
        'CALIFICACION CIERRE': "category",
        'LINEA': "category",
        'TIPO CREDITO':"category"
    })    
df=df.drop(columns=['Unnamed: 0'])
dm=pd.read_csv('data\municipios_y_departamentos.csv')
dm=dm.drop(columns=['Unnamed: 0'])
df_completo=df.merge(dm, on='MUNICIPIO_CLIENTE',how="left")
depto_en_mora=df_completo.drop_duplicates(subset=['ID'])
depto_en_mora=depto_en_mora[(df_completo['MORA_STATUS']==1)]
depto_en_mora=depto_en_mora["DEPARTAMENTO"].value_counts()
depto_en_mora=depto_en_mora.to_frame().reset_index()
depto_en_mora.columns=['DEPARTAMENTO','COUNT']
depto_en_mora=depto_en_mora.merge(df_completo[['DEPARTAMENTO','COD_DPTO']].drop_duplicates(subset=['COD_DPTO']), on='DEPARTAMENTO',how="left")
depto_en_mora.columns=['DEPARTAMENTO','CLIENTES_EN_MORA','CODIGO_DEPARTAMENTO']
  
df_maptest = depto_en_mora
