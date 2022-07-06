from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_labs.plugins.pages import register_page
from components.logistic.logistic_reg import prediccion
from components.dataframe.data import df_prueba

# dash-labs plugin call, menu name and route
register_page(__name__, path="/predictor")

# specific layout for this page
layout = dbc.Container(children = [
    dbc.Row(children=[
        dbc.Col([
            html.H2(children='Prediccion usando modelo de regresión logística',
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


# call backs
@callback(
    Output('display-div','children'),
    Input('button1','n_clicks')
    )
def display(n_clicks):
    sample = df_prueba
    result = ''
    if n_clicks is not None:
        if n_clicks>0:
            result = prediccion(sample)
    return result

  