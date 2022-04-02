import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from app import app
import pandas as pd
import os
import plotly.express as px
from pages.home import home_callbacks
from pages.home import home_data

fig = None

layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(html.Div(children=[
                dcc.Input(id="contractor-search", type="search", placeholder="Search Contractors"), 
            ]), 
            width=4),
            dbc.Col(html.Div(children=[
                html.Button('Show', id='contractor-show', n_clicks=0),
            ]), 
            width=4),
        ],
        justify="between",
    ),
    dbc.Row(
        [
            dbc.Col(html.Div(id='contractor-name'), width=12),
        ]
    ),
    html.Hr(),
    dbc.Row(
        [
            dbc.Col(html.Div([dcc.Graph(id='overview-map', figure=fig)]), width=12),
        ],
        align="left",
    ),
    html.Hr(),
    html.Div(id='contractor-display', children = [])
])
