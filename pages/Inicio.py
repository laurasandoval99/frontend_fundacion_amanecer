import dash
import os 
from dash import dcc, html, dash_table, callback
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
card3 = infocard('{}%'.format(por_mora),fecha_ult,'PORCETAJE DE DEUDORES','Warning')


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
    dbc.Row(children=[
        dbc.Col(children=[
            html.Div(children=[
                html.H4("Seleccione las opciones para el grafico"),
                dbc.Col(children=[
                    dcc.Dropdown(
                    id="ticker",
                    options=["CAPITAL_VENCIDO", "SALDO_TOTAL", "CLIENTES_MORA"],
                    value="CAPITAL_VENCIDO",
                    clearable=False,
                    style = {'width':'60%','display':'inline-block'}
                ),
                dcc.Dropdown(
                    id="ticker2",
                    options=['GENERO','REGION','LINEA', 'TIPO_CREDITO','NOM_TIPOCLIENTE','UBICACIO_CLIENTE','PERIODICIDAD',
                    'TIPO_CREDITO','NIVEL_DE_ESTUDIOS_NEW','SUCURSAL','ESTRATO','DESTINACION','TIPO_VIVIENDA'],
                    value='GENERO',
                    clearable=False,
                    style = {'width':'60%','display':'inline-block'}
                ),

                ]),

                dbc.Col(id="line_chart_cap_vencido") 
            ])
        ],className='col align-self-center')
    ],style={'textAlign': 'center','margin':30})


# close container
], fluid=True)

# call backs
@callback(
    Output('line_chart_cap_vencido','children'),
    Input('ticker','value'),
    Input('ticker2','value')
    )
def line_chart_cap_vencido(ticker,ticker2):
    df_tiempo = inicio_graph(ticker2)
    x = df_tiempo['FECHA']
    color = ticker2
    grafico1 = linegraph(ticker,'Año',ticker,df_tiempo,x,ticker,color)
    return grafico1.display()

