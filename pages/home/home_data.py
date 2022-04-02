import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from app import app

import pandas as pd
import os

import plotly.express as px

from pages.home import home_callbacks
from pages.home import home



def get_fig():

    fig = px.scatter_mapbox(zoom=2, height=800) #None, lat=None, lon=None, hover_name=None, hover_data=None, color=None,size=None,
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(showlegend=False)
    
    return fig