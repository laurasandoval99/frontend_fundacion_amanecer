from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path="/nosotros")

# specific layout for this page
layout = dbc.Container(children = [
    dbc.Row(children=[

        dbc.Col([
            html.H2(children='Equipo que trabajó en este proyecto',
            style={'text-align': 'left', 'fontFamily': 'Times New Roman'}),
        ], lg=12),

        dbc.Col([
            dcc.Link(html.A('Gamboa Villamizar, Jorge Hernán'), target='_blank', href="https://www.linkedin.com/in/jhgamboa97", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Bejarano Pinto, Laura Camila'), target='_blank', href="https://www.linkedin.com/in/laura-camila-bejarano-pinto-893776139/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Montaño Díaz, Andrés Felipe'), target='_blank', href="https://www.linkedin.com/in/andres-felipe-montano-diaz/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Romero Fierro, Juan Felipe'), target='_blank', href="https://www.linkedin.com/in/juan-felipe-romero-fierro-29b15598/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Sandoval Acosta, Laura Carolina'), target='_blank', href="https://www.linkedin.com/in/laura-carolina-sandoval-acosta-319979206/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Ariza Arenas, Diego Alexander'), target='_blank', href="https://www.linkedin.com/in/d-triplea/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(),
            dcc.Link(html.A('Arias Varón, Andres Elias'), target='_blank', href="https://www.linkedin.com/in/andres-elias-arias-varon-9a2209196/", 
            style={'color': 'blue', 'text-decoration': 'none'}),
            html.Br(), 
        ])
    ]),
    html.Br(),  
],fluid=True)