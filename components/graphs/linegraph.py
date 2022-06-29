import dash
from dash import dcc, html, dash_table
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


class linegraph:
    def __init__(self,title,xaxis,yaxis,df,x,y,color):
        self.title = title
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.x = x
        self.y = y
        self.df = df
        self.color = color
        
        
    
    @staticmethod
    def figura(self):
        fig = px.line(self.df, x=self.x, y=self.y, color=self.color)
                 
        fig.update_layout(title=self.title,
                  xaxis_title=self.xaxis,
                  yaxis_title=self.yaxis,
                  )
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
            buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
           dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=5, label="5y", step="year", stepmode="backward"),
            dict(step="all")
            ])
            )
            )
        return fig

    def display(self):
        layout = dbc.Card(children=[
            dbc.Row(children=[
                dbc.Col(children=[
                    dcc.Graph(figure=linegraph.figura(self))
                ], className='col align-self-center')
            ])
        ], className='m-1 border-success')

        return layout
