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
import graficos as gr

# dash-labs plugin call, menu name and route
register_page(__name__, path="/status")

#Load data
df2 = gr.load_data2()
df_tiempo = gr.porcentajes()

#charts
def line_chart_cap_vencido(df_tiempo):
    fig = go.Figure(data = [go.Scatter( x = df_tiempo["FECHA"], y = df_tiempo["CAPITAL_VENCIDO"],\
        line = dict(color="#EF553B",width=4), text = df_tiempo["CAPITAL_VENCIDO"],name = "Capital Vencido")])
    fig.update_layout(title= "Capital vencido",
                      xaxis_title = "Fecha",
                      yaxis_title = "Capital Vencido")
    return fig

# specific layout for this page
layout =  dbc.Container([
    dbc.Row([dbc.Col([html.H1(id = "H1", children = "Status")],xl= 6,lg=6,md=12,sm=12,xs=12)], style={"textAlign":"center", "marginTop" : 30, "marginBottom":30}),
    dbc.Row([dbc.Col([dcc.Graph(id = "line_chart_cap_vencido", figure=line_chart_cap_vencido(df_tiempo))],xl= 6,lg=6,md=12,sm=12,xs=12)], style={"textAlign":"center", "marginTop" : 30, "marginBottom":30})
    
],fluid = True)