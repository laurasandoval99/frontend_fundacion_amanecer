from turtle import width
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
import graficos as gr
#os.chdir("C://Users//MIPC//Desktop//DS4A//FUNDACIÓN AMANECER//Visualización//FrontEnd")

# inicializing the app
app= dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

df = gr.load_data()
fig= px.scatter(df, x='DIAS VENCIDO', y= 'CP')


def display_card(header, mensaje, informacion):
    card_content = [
        dbc.CardHeader(header),

        dbc.CardBody(
            [
                dcc.Markdown(dangerously_allow_html=True,
                             children=["{0}<br>{1}</br>".format(mensaje, informacion)])
            ]
        )
    ]
    return card_content

<<<<<<< HEAD
df = pd.read_csv('Cartera_Final_2.csv',low_memory=False, nrows=10000)
df = df.drop(['Unnamed: 0'], axis=1, inplace = True)
df = df.reset_index()
df = df[["NRO SOLICITUD","OBLIGACION","PAGARE","REGION","MONTO","FEC SOLICITUD","VALOR CUOTA"]]

=======
>>>>>>> 7c76da085c25addc19c4e9b4765f405870bf3887

# inicialize the app layout
app.layout = html.Div(dbc.Container([
    dbc.Row([
        html.Div([
            html.Div([html.H1("Fundación Amanecer")
                      ]),
            html.Div([(html.Img(src=app.get_asset_url('amanecer.jpg')))
                      ])
        ])

    ], id="header1"),

    html.Div(
        dcc.Tabs(id="header_tabs", value='Clients_graph', children=[
            dcc.Tab(label='Client Statistics', value='Clients_graph', className="custom_tab", selected_className="custom_tab_selected", children=[
                    dbc.Row(children=[
                        dbc.Col(dbc.Card(display_card("HOLA", "capital vencido", '${:,.2f}'.format(gr.cap_vencido())), color='light', style={
                                'text-align': 'center'}, inverse=False), style={'padding': '12px'}),
                        dbc.Col(dbc.Card(display_card("HOLA", "Capital pendiente", '${:,.2f}'.format(gr.cap_pendiente())), color='light', style={
                                'text-align': 'center'}, inverse=False), style={'padding': '12px'}),
                        dbc.Col(dbc.Card(display_card("HOLA", "porcentaje de clientes pendientes", '%{}'.format(gr.deudores_pen(
                        ))), color='light', style={'text-align': 'center'}, inverse=False), style={'padding': '12px'}),

                    ]),
                    dbc.Row(children=[
                        dbc.Col(width={"size": 8, "offset": 2}, children=[
                            html.H2('Dataset Introduction', style={
                                    'textAlign': 'center'}),
                            dash_table.DataTable(
                                data=df.to_dict('records'),
                                columns=[{'id': c, 'name': c}
                                         for c in df.columns],
                                page_size=8,
                                sort_action = 'native',
                                export_format="xlsx",
                                style_header={'backgroundColor': 'rgb(224,224,224)',
                                              'fontWeight': 'bold',
                                              'border': '4px solid white',
                                              'fontSize': '12px'
                                              },
                                style_data_conditional=[
                                    {
                                        'if': {'row_index': 'odd',
                                               # 'column_id': 'ratio',
                                               },
                                        'backgroundColor': 'rgb(240,240,240)',
                                        'fontSize': '12px',
                                    },
                                    {
                                        'if': {'row_index': 'even'},
                                        'backgroundColor': 'rgb(255, 255, 255)',
                                        'fontSize': '12px',
                                    }
                                ],
                                fixed_rows={'headers': False},
                                virtualization= True,
                                style_cell={
                                    'textAlign': 'center',
                                    'fontFamily': 'Times New Roman',
                                    'border': '4px solid white',
                                    'width': '100',
                                    'minWidth':'100',
                                    'textOverflow': 'ellipsis',
                                }
                            ),
                        ]),
                    ]),
                    html.Br(),
                    html.H3('Capital Vencido vs Dias vencidos',
                            style={'textAlign': 'center'}),
                    dcc.Graph(
                        figure=fig
                    )
                    ]),

            dcc.Tab(label='Predictor', value='Clients_predictor', className="custom_tab", selected_className="custom_tab_selected", children=[
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
                    ]),

            dcc.Tab(label='mapa', className='custom_tab', selected_className='custom_tab_selected',children=[
                html.H3('capital vencido ${:,.2f}'.format(gr.cap_vencido()), style={'textAlign':'center'}),
                html.Br(),
                html.H3('capital pendiente ${:,.2f}'.format(gr.cap_pendiente()), style={'textAlign':'center'}),
                html.Br(),
                html.H3('porcentaje de clientes pendientes: %{}'.format(gr.deudores_pen()), style={'textAlign':'center'})
            ]),
        ]),
    )
# close layout div and container
]),
)


if __name__ == '__main__': 
    app.run_server(debug=True)