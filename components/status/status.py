import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import rcParams
from scipy import stats


class infocard:
    def __init__(self,info,label, cardcolor):
        self.info = info
        self.label = label
        self.cardcolor = cardcolor

        if cardcolor=='Danger':
            self.color = "danger"
        elif cardcolor=='Success':
            self.color = "success"
        else:
            self.color = "warning"

    def display(self):
        layout = html.Div(children=[
            dbc.Card(children=[
                dbc.CardHeader(self.label),
                dbc.CardBody(
                    [
                        dcc.Markdown(dangerously_allow_html=True,
                                     children=["{0}<br>".format(self.info)])
                    ]
                )
            ], outline=True, color=self.color, style={'text-align': 'center', 'fontFamily': 'Times New Roman','border':'2px solid'})
        ])

        return layout
    