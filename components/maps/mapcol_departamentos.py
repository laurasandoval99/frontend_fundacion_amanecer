from dash import html , dcc
import plotly.graph_objects as go

import json
          
class mapcol_departamentos:
    """A Class to represent a map of Colombia with two Layers, one for Municipios and 
    the second one for markers as overlay
    
    based in json file of 
    https://www.kaggle.com/code/alfredomaussa/colombia-municipios/notebook?scriptVersionId=39794627
    
    Towns codes available in
    https://www.dane.gov.co/files/censo2005/provincias/subregiones.pdf

    """
    def __init__(self,map_title:str, ID:str,df, mun:bool):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df = df 
        self.mun= mun

 
    @staticmethod
    def figura(self):
        if(self.mun == False):
            with open('data/jsonmaps/colombia.geo.json', encoding='utf-8') as json_file:
                departamentos = json.load(json_file)
            for i, each in enumerate(departamentos["features"]):
                departamentos["features"][i]['id']=departamentos["features"][i]['properties']['DPTO']

            mapa = go.Choroplethmapbox(
                geojson=departamentos, 
                locations=self.df.CODIGO_DEPARTAMENTO, 
                z=self.df['CLIENTES_EN_MORA'],
                colorscale="reds",
                text=self.df.DEPARTAMENTO,
                marker_opacity=0.9, 
                marker_line_width=0.5,
                colorbar_title = "COUNT",
                )
            annotations = [
                dict(
                    showarrow=False,
                    align="right",
                    text="",
                    font=dict(color="#000000"),
                    bgcolor="#f9f9f9",
                    x=0.95,
                    y=0.95,
                )
            ]

            fig = go.Figure(data=mapa)

            

            fig.update_layout(
                geo_scope='south america',
                mapbox_style="carto-positron",
                mapbox_zoom=5.8, 
                mapbox_center = {"lat": 6.88970868, "lon": -74.2973328},
                annotations=annotations,
                height=400),

            
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            
            return fig
        else: 

            with open ('./data/jsonmaps/MunicipiosColombia.json', encoding='utf-8') as json_file:
                municipios = json.load(json_file)

            mapa = go.Choroplethmapbox(
                geojson=municipios, 
                locations=self.df.COD_MUN, 
                z=self.df['CLIENTES_MORA'],
                colorscale="reds",
                text=self.df.MUNICIPIO_CLIENTE,
                marker_opacity=0.9, 
                marker_line_width=0.5,
                colorbar_title = "COP",
                )
            annotations = [
                dict(
                    showarrow=False,
                    align="right",
                    text="",
                    font=dict(color="#000000"),
                    bgcolor="#f9f9f9",
                    x=0.95,
                    y=0.95,
                )
            ]

            fig = go.Figure(data=mapa)


            fig.update_layout(
                mapbox_style="carto-positron",
                mapbox_zoom=6.5, 
                mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
                annotations=annotations,
                height=1000),


            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            fig.update_geos(fitbounds="locations")
            return fig

    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapcol_departamentos.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout
            
        
    