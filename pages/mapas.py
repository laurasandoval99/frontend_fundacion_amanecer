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
register_page(__name__, path="/maps")

# specific layout for this page
layout = dbc.Container( children=[
    dbc.Row([
        dbc.Col([
            html.H1(children='Aquí irian los mapas'),
        ], lg=12),
    ]),
])