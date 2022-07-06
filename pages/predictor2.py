from dash import dcc, html, dash_table, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash_labs.plugins.pages import register_page
import plotly.graph_objects as go

# dash-labs plugin call, menu name and route
register_page(__name__, path="/predictor2")

# creating a figure to show the image

# Create figure
fig = go.Figure()

# Constants
img_width = 2000
img_height = 1200
scale_factor = 0.5

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

# Configure axes
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source="/assets/arbol_output.png")
)

# Configure other layout
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
)

# Disable the autosize on double click because it adds unwanted margins around the image
# More detail: https://plotly.com/python/configuration-options/
fig.show(config={'doubleClick': 'reset'})


# specific layout for this page
layout = dbc.Container(children=[
    dbc.Row(children=[
        dbc.Col([
            html.H2(children='Prediccion usando modelo de arboles de decisión',
                    style={'text-align': 'left', 'fontFamily': 'Times New Roman'}),
        ], lg=12),
    ]),
    html.Br(),
    dbc.Row(children=[
        dbc.Col([
            dcc.Graph(figure=fig)
        ],lg=12, style={'offset':2})
    ]),
    html.Br()
], fluid=True)
