import dash
import os 
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
import dash_labs as dl
from dash_labs.plugins.pages import register_page
from components.card.infocard import infocard
from components.dataframe.data import *
from components.graphs.linegraph import linegraph

# dash-labs plugin call, menu name and route
register_page(__name__, path="/")

# trayendo datos externos

capital_ven = ind_ult_mes()[0]
por_mora = ind_ult_mes()[1]
total_saldo = ind_ult_mes()[2]
fecha_ult = ind_ult_mes()[3]

card1 = infocard('${:,.2f}'.format(capital_ven),fecha_ult,'CAPITAL VENCIDO','Danger')
card2 = infocard('${:,.2f}'.format(total_saldo),fecha_ult,'CAPITAL PENDIENTE','Success')
card3 = infocard('%{}'.format(por_mora),fecha_ult,'PORCETAJE DE DEUDORES','Warning')

# trayendo df tiempo para graficar las lineas de tiempo
df_tiempo
color = df_tiempo['GENERO']
x = df_tiempo['FECHA']
y = df_tiempo['CAPITAL_VENCIDO']
y1 = df_tiempo['SALDO_TOTAL']
y2 = df_tiempo['CLIENTES_MORA']


# instanciado un objetos de la clase linegraph
grafico1 = linegraph('Capital vencido','Año','capital vencido',df_tiempo,x,y,color)
grafico2 = linegraph('Saldo total','Año','Saldo total',df_tiempo,x,y1,color)
grafico3 = linegraph('Porcentaje de clientes en mora','Año','Clientes en  mora',df_tiempo,x,y2,color)


# specific layout for this page
layout = dbc.Container(children=[
    dbc.Row(children = [
        dbc.Col([
            html.H2(children='Clients statistics'),
        ], lg=12, className='mb-3', style={'text-align': 'center', 'fontFamily': 'Times New Roman'}),
    ]),
    dbc.Row([
        dbc.Col([
            card1.display()
        ]),
        dbc.Col([
            card2.display()
        ]),
        dbc.Col([
            card3.display()
        ]),
    ]),
    html.Br(),
    
    dbc.Row([
        grafico1.display()
    ]),
    html.Br(),

    dbc.Row([
        grafico2.display()
    ]),
    html.Br(),

    dbc.Row([
        grafico3.display()
    ])


])

