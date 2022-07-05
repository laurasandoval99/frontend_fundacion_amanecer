from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_labs.plugins.pages import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path="/predictor2")

# specific layout for this page
layout = dbc.Container(children = [
    dbc.Row(children=[
        dbc.Col([
            html.H2(children='Prediccion usando modelo de arboles de decisión',
            style={'text-align': 'left', 'fontFamily': 'Times New Roman'}),
        ], lg=12),
    ]),
    html.Br(),
    dbc.Row(children=[
        dbc.Button(id='button1', color='success', outline=True, children='Ejercutar prediccion',className='col-6'),
    ], className='col-8'),
    html.Br(),
    html.Div(id='display-div')

],fluid=True)
