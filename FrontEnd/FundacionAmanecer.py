import dash
import os 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
# from plotly.offline import init_notebook_mode,  plot

#os.chdir("C://Users//MIPC//Desktop//DS4A//FUNDACIÓN AMANECER//Visualización//FrontEnd")



app= dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df= pd.read_csv('Cartera_Final_2.csv',low_memory=False, nrows=10000)
df.drop(['Unnamed: 0'], axis=1, inplace = True)
df.reset_index()
df = df[["NRO SOLICITUD","OBLIGACION","PAGARE","REGION","MONTO","FEC SOLICITUD","VALOR CUOTA"]]


#df=px.data.iris()
app.layout = html.Div(dbc.Container([
    dbc.Row([
        html.Div([
            
            html.Div([html.H1("Fundación Amanecer")
            ]),
                
            html.Div([(html.Img(src=app.get_asset_url('amanecer.jpg')))
            ])
        ])

    ],id="header1"),

    html.Div(
        dbc.Row([
            dcc.Tabs(id="header_tabs", value='Clients_graph', children=[
                dcc.Tab(label='Client Statistics', value='Clients_graph', className="custom_tab", selected_className="custom_tab_selected"),
                dcc.Tab(label='Predictor', value='Clients_predictor', className="custom_tab", selected_className="custom_tab_selected"),
            ]),
            html.Div(id='Header_Graph')
        ]),
    )

    ]),
)

@app.callback(Output('Header_Graph', 'children'),
              Input('header_tabs', 'value'))

def render_content(tab):
    html.Hr(),
    if tab == 'Clients_graph':
        fig= px.scatter(df,x='DIAS VENCIDO', y= 'CP')

        return html.Div([

            dbc.Row(children = [
                dbc.Col(width={"size": 8, "offset": 2}, children =[

                html.H2('Dataset Introduction', style={'textAlign':'center'}),

                dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df.columns],
                page_size=8,
                fixed_rows={'headers': True},
                style_cell={'minWidth': 95, 'maxWidth': 100, 'width': 95}
            ),
        ]),
       ]),
       html.Br(),
        html.H3('Capital Vencido vs Dias vencidos', style={'textAlign':'center'}),
        dcc.Graph(
            figure= fig
        )
        ])
       
    elif tab == 'Clients_predictor':
        return html.Div([
            html.Hr(),
            html.H3('Predictor'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])


if __name__ == '__main__': 
    app.run_server()