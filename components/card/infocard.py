import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

class infocard:
    def __init__(self,info,fecha,label, cardcolor):
        self.info = info
        self.label = label
        self.fecha = fecha
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
                    children=["{}<br>fecha ultimo cierre de cartera<br>{}".format(self.info, self.fecha)])
                    ]
                )
            ], outline=True, color=self.color, style={'text-align': 'center', 'fontFamily': 'Times New Roman','border':'2px solid'})
        ])

        return layout
    