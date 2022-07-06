# import os 
import dash
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_labs as dl
import dash_auth
from callbacks import register_callbacks

#os.chdir("C://Users//MIPC//Desktop//DS4A//FUNDACIÓN AMANECER//Visualización//FrontEnd")

# inicializing the app
app= dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY], update_title='Cargando...')

auth = dash_auth.BasicAuth(
    app,
    {'born.to.lose': 'live.to.win',
     'admin': 'unsecreto'}
)

app.config.suppress_callback_exceptions=True

encabezado = dbc.Container(children=[
    dbc.Row([
        html.Div([
            html.Div([html.H1("Fundación Amanecer")
                      ]),
            html.Div([(html.Img(src=app.get_asset_url('amanecer.jpg')))
                      ])
        ])

    ], id="header1"),

    dbc.Row(children=[
        dbc.NavbarSimple( children = [
            dbc.NavItem(dbc.NavLink("Inicio", href="/")),
            dbc.DropdownMenu(
                [ 
                    dbc.DropdownMenuItem(page["name"], href=page["path"])
                    for page in dash.page_registry.values()
                    if page["module"] != "pages.not_found_404" 
                ],
                nav=True,
                label="Opciones",
            ),
            dbc.NavItem(dbc.NavLink("Nosotros", href="https://www.amanecer.org.co/")),
        ],
            brand="DS4A Project - Team 164",
            color="success",
            dark=True,
            className="mb-2",
            style ={'font-style': 'italic', 'fontSize':'20px'}
        )

    ])
])

# inicialize the app layout
app.layout = dbc.Container(children=[
    encabezado,
    dl.plugins.page_container

], className="dbc", fluid=True
)

# Call to external function to register all callbacks
register_callbacks(app)

# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run(debug=True)