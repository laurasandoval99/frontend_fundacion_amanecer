import pandas as pd

# dataset de prueba para el mapa
df = pd.read_csv('data/Data_Final.gzip',sep=",", encoding="utf-8", low_memory=False, index_col=0, compression='gzip', 
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

# df=df.drop(columns=['Unnamed: 0'])
dm=pd.read_csv('data/municipios_y_departamentos.csv',
sep=",", encoding="utf-8", low_memory=False, index_col=0)

#dm=dm.drop(columns=['Unnamed: 0'])
df_completo=df.merge(dm, on='MUNICIPIO_CLIENTE',how="left")
depto_en_mora=df_completo.drop_duplicates(subset=['ID'])
depto_en_mora=depto_en_mora[(depto_en_mora['MORA_STATUS']==1)]
depto_en_mora=depto_en_mora["DEPARTAMENTO"].value_counts()
depto_en_mora=depto_en_mora.to_frame().reset_index()
depto_en_mora.columns=['DEPARTAMENTO','COUNT']
depto_en_mora=depto_en_mora.merge(df_completo[['DEPARTAMENTO','COD_DPTO']].drop_duplicates(subset=['COD_DPTO']), on='DEPARTAMENTO',how="left")
depto_en_mora.columns=['DEPARTAMENTO','CLIENTES_EN_MORA','CODIGO_DEPARTAMENTO']
total= depto_en_mora['CLIENTES_EN_MORA'].sum()
depto_en_mora["PORCENTAJE"] = (100*depto_en_mora['CLIENTES_EN_MORA'])/total
depto_en_mora["PORCENTAJE"]=depto_en_mora["PORCENTAJE"].astype(int)

df_maptest = depto_en_mora

mpio_en_mora=df_completo.drop_duplicates(subset=['ID'])
mpio_en_mora=mpio_en_mora[(mpio_en_mora['MORA_STATUS']==1)]
#depto_en_mora=depto_en_mora["DEPARTAMENTO"].value_counts()
mpio_en_mora=mpio_en_mora["MUNICIPIO_CLIENTE"].value_counts()
mpio_en_mora=mpio_en_mora.to_frame().reset_index()
mpio_en_mora.columns=['MUNICIPIO_CLIENTE','CLIENTES_MORA']
mpio_en_mora=mpio_en_mora.merge(df_completo[['MUNICIPIO_CLIENTE','COD_MUN','COD_DPTO','DEPARTAMENTO']].drop_duplicates(subset=['COD_MUN']), on='MUNICIPIO_CLIENTE',how="left")
total1= mpio_en_mora['CLIENTES_MORA'].sum()
mpio_en_mora["PORCENTAJE"] =  (100*mpio_en_mora['CLIENTES_MORA'])/total1
mpio_en_mora["PORCENTAJE"]=mpio_en_mora["PORCENTAJE"].astype(int)