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
import graficos as gr

# dash-labs plugin call, menu name and route
register_page(__name__, path="/status")

#Load data
df2 = gr.load_data2()
df_tiempo = gr.porcentajes()

#charts


# specific layout for this page
layout =  dbc.Container([
    dbc.Row([dbc.Col([html.H1(id = "H1", children = "Status")],xl= 6,lg=6,md=12,sm=12,xs=12)], style={"textAlign":"center", "marginTop" : 30, "marginBottom":30}),
    dbc.Row([dbc.Col([html.Div([html.H4("Select charts"),
    dcc.Graph(id = "line_chart_cap_vencido"),html.P("Select chart:"),
    dcc.Dropdown(
        id="ticker",
        options=["CAPITAL_VENCIDO", "SALDO_TOTAL", "CLIENTES_MORA"],
        value="CAPITAL_VENCIDO",
        clearable=False,
    ),])],xl= 6,lg=6,md=12,sm=12,xs=12)], style={"textAlign":"center", "marginTop" : 30, "marginBottom":30})
    
],fluid = True)

@callback(
    Output("line_chart_cap_vencido","figure"),
    Input("ticker","value"))
def line_chart_cap_vencido(ticker):
    df_tiempo = gr.porcentajes()
    fig = px.line(df_tiempo, x = "FECHA", y = ticker)
    fig.update_layout(
        {
            'paper_bgcolor' : 'rgb(233,233,233)'
        }
    )
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
    )
    return fig 