import base64
import datetime
import io

from turtle import width
import dash
from dash import dcc
from dash import html
import os 
import dash_bootstrap_components as dbc
from dash import dash_table
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output,State
import graficos as gr

#os.chdir("C://Users//MIPC//Desktop//DS4A//FUNDACIÓN AMANECER//Visualización//FrontEnd")

# inicializing the app
app= dash.Dash(external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True)

#Load the data 
# df1 is for cards because Jorge made some new colums
df = gr.load_data()
fig= px.scatter(df, x='DIAS VENCIDO', y= 'CP')
# df2 is for showing the table
df2 = gr.show_data()

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
                    ##
                    html.Div(
                        dbc.Row([dbc.Col([dcc.Upload(
                        id = "upload-data",
                        children = html.Div([
                            'Arrastre o ',
                            html.A('seleccione el archivo ')
                        ]),
                        style = {
                            'width': '98%',
                            'height': '60px',
                            'lineHeight': '60px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px'
                        },
                        # Allow multiple files to be uploaded
                        multiple=True
                    ),
                    html.Div(id='output-div'),
                    html.Div(id='output-datatable'),
                    ])
                    ])

                    , id = "upload-data1"),
                    

                    dbc.Row(children=[
                        dbc.Col(width={"size": 8, "offset": 2}, children=[
                            html.H2('Dataset Introduction', style={
                                    'textAlign': 'center'}),
                            dash_table.DataTable(
                                data=df2.to_dict('records'),
                                columns=[{'id': c, 'name': c}
                                         for c in df2.columns],
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

            dcc.Tab(label='Mapa', className='custom_tab', selected_className='custom_tab_selected',children=[
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


## Check the number of rows!!!
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df_table = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')),low_memory=False,nrows=1000)
            df_table = df_table[["OBLIGACION",'NRO SOLICITUD','MUNICIPIO CLIENTE', 'MONTO', 'VALOR CUOTA', 'CUOTAS PACTADAS','CUOTAS PENDIENTES', 'CALIFICACION CIERRE', 'VENCIDA', 'DIAS VENCIDO','CAPITAL VEN','MORA', 'FEC ULT.PAGO','FEC PROXIMO PAGO', 'VENCIMIENTO FINAL', 'Fecha']]
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df_table = pd.read_excel(io.BytesIO(decoded),low_memory=False,nrows=1000)
            df_table = df_table[["OBLIGACION",'NRO SOLICITUD','MUNICIPIO CLIENTE', 'MONTO', 'VALOR CUOTA', 'CUOTAS PACTADAS','CUOTAS PENDIENTES', 'CALIFICACION CIERRE', 'VENCIDA', 'DIAS VENCIDO','CAPITAL VEN','MORA', 'FEC ULT.PAGO','FEC PROXIMO PAGO', 'VENCIMIENTO FINAL', 'Fecha']]
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.P("Inset X axis data"),
        dcc.Dropdown(id='xaxis-data',
                     options=[{'label':x, 'value':x} for x in df_table.columns]),
        html.P("Inset Y axis data"),
        dcc.Dropdown(id='yaxis-data',
                     options=[{'label':x, 'value':x} for x in df_table.columns]),
        html.Button(id="submit-button", children="Create Graph"),
        html.Hr(),

        dash_table.DataTable(
            data=df_table.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df_table.columns],
            page_size=15
        ),
        dcc.Store(id='stored-data', data=df_table.to_dict('records')),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])


#Callback to output of the csv file
@app.callback(Output('output-datatable', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


@app.callback(Output('output-div', 'children'),
              Input('submit-button','n_clicks'),
              State('stored-data','data'),
              State('xaxis-data','value'),
              State('yaxis-data', 'value'))
def make_graphs(n, data, x_data, y_data):
    if n is None:
        return dash.no_update
    else:
        bar_fig = px.bar(data, x=x_data, y=y_data)
        # print(data)
        return dcc.Graph(figure=bar_fig)


if __name__ == '__main__': 
    app.run_server(debug=True)
