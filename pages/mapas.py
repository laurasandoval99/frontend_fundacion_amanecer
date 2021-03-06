from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

from components.maps.mapcol_departamentos import mapcol_departamentos
from components.sampledf.model import df_maptest
from components.table.table import table
from components.sampledf.model import mpio_en_mora


mapa_colombia_departamentos = mapcol_departamentos('Mapa Departamentos Colombia', 'div_municipios_fig2',df_maptest, False)
mapa_colombia_municipios= mapcol_departamentos('Mapa Municipios Colombia', 'div_municipios_fig1',mpio_en_mora, True)

params1 = {
            'title': 'Departamentos', 
            'description': 'Tabla de lista de departamentos',
            'columns': [ 'DEPARTAMENTO', 'CLIENTES_EN_MORA', 'PORCENTAJE']
}
tabla_datos_departamentos = table(df_maptest,params1)

params2 = {
            'title': 'municipios', 
            'description': 'Tabla de lista de municipios',
            'columns': ['MUNICIPIO_CLIENTE','DEPARTAMENTO','CLIENTES_MORA','PORCENTAJE']
}
tabla_datos_municipios = table(mpio_en_mora,params2)


register_page(__name__, path="/mapa2")

layout= html.Div(
    [   
        dbc.Row([
            dbc.Col([
                html.Br(),
                html.Br(),
                html.H1("Mapas de clientes en mora por departamento", className='title ml-2'),
                html.Br(),
            ])
           
        ]),

        html.Div([
            dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div(['Seleccione los departamentos'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_municipio",
                    options=[
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
                        {"label": "CASANARE", "value": "CASANARE"},
                        {"label": "ARAUCA", "value": "ARAUCA"},
                        {"label": "META", "value": "META"},
                    ],
                    value=['BOYACA','CUNDINAMARCA','CASANARE', 'ARAUCA','META'],
                    multi = True
                )
                ])
                
            ]),
            
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Button([
                    'Filtrar'
                ],id="id_filtrar")
                
            ],class_name="d-flex justify-content-end mt-2"),
        ]),

        ],className="card"),
        

        dbc.Row([
            dbc.Col([
                html.Div([
                    mapa_colombia_departamentos.display()  
                ],id="row_map")   
            ])
        ], className= "card"),

         dbc.Row([
            dbc.Col([
                html.Div([
                    tabla_datos_departamentos.display()
                ],id="row_tabla")   
            ])
        ], className= "card"),

        html.Br(),
        html.Br(),
        html.Br(),
        
        dbc.Row([
            dbc.Col([
                 html.H1("Mapas de clientes en mora por municipio", className='title ml-2'),
            ])
           
        ]),

        html.Div([
            dbc.Row([
            dbc.Col([
                html.Div([
                    html.Div(['Seleccione los departamentos'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_municipio2",
                    options=[
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
                        {"label": "CASANARE", "value": "CASANARE"},
                        {"label": "ARAUCA", "value": "ARAUCA"},
                        {"label": "META", "value": "META"},
                    ],
                    value=['BOYACA','CUNDINAMARCA','CASANARE', 'ARAUCA','META'],
                    multi = True
                )
                ])
                
            ]),
            
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Button([
                    'Filtrar'
                ],id="id_filtrar2")
                
            ],class_name="d-flex justify-content-end mt-2"),
        ]),

        ],className="card"),
        

        dbc.Row([
            dbc.Col([
                html.Div([
                    mapa_colombia_municipios.display()  
                ],id="row_map2")   
            ])
        ], className= "card"),

         dbc.Row([
            dbc.Col([
                html.Div([
                    tabla_datos_municipios.display()
                ],id="row_tabla")   
            ])
        ], className= "card"),

    


    ], className='container-fluid', style={'margin': 'auto', 'width':'100%'}
    
)  


@callback(
        [Output("row_map", 'children')], 
        [State("id_selector_municipio", "value"), 
         Input("id_filtrar", "n_clicks"),
                
        ],prevent_initial_call=True
    )
def update_map(selector_municipio,selector_year):
        df_filtrado = mapa_colombia_departamentos.df[mapa_colombia_departamentos.df['DEPARTAMENTO'].isin(selector_municipio)]
        #df_filtrado = df_filtrado[df_filtrado['COUNT']<(10**selector_year)]
        #mapa_colombia_departamentos.df = df_filtrado
        #nuevo_mapa = mapa_colombia_departamentos.display()
        mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado,False )
        nuevo_mapa = mapa_filtrado.display()
        return [nuevo_mapa]

@callback(
        [Output("row_map2", 'children')], 
        [State("id_selector_municipio2", "value"), 
         Input("id_filtrar2", "n_clicks"),
                
        ],prevent_initial_call=True
    )
def update_map_mun(selector_municipio,selector_year):
        df_filtrado = mapa_colombia_municipios.df[mapa_colombia_municipios.df['DEPARTAMENTO'].isin(selector_municipio)]
        #df_filtrado = df_filtrado[df_filtrado['COUNT']<(10**selector_year)]
        #mapa_colombia_departamentos.df = df_filtrado
        #nuevo_mapa = mapa_colombia_departamentos.display()
        mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado,True )
        nuevo_mapa = mapa_filtrado.display()
        return [nuevo_mapa]