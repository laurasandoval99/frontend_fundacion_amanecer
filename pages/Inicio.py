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
import graficos as gr

# dash-labs plugin call, menu name and route
register_page(__name__, path="/")

# trayendo datos externos
df = gr.load_data()
capital_pend = gr.cap_pendiente()
capital_ven = gr.cap_vencido()
deudores_pen = gr.deudores_pen()

card1 = infocard('${:,.2f}'.format(capital_ven),'CAPITAL VENCIDO','Danger')
card2 = infocard('${:,.2f}'.format(capital_pend),'CAPITAL PENDIENTE','Success')
card3 = infocard('%{}'.format(deudores_pen),'PORCETAJE DE DEUDORES','Warning')


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
])

