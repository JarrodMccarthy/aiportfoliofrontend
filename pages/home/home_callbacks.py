import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
from app import app
import os
import pandas as pd
import csv

from components.table import make_dash_table
from components.indicator import make_indicator




@app.callback(
    Output('contractor-name', 'children'),
    Input('contractor-search', 'value')
)
def update_output(value):
    if value:
        matches = checkformatches(value)
        if len(matches) < 1:
            return "Not Found"
        else:
            return "Matches: {}".format(matches)
    

@app.callback(
    Output('contractor-display', 'children'),
    Input('contractor-show', 'n_clicks'),
    State('contractor-search', 'value')
)
def update_output(n_clicks, value):
    if value and n_clicks > 0:
        matches = checkformatches(value)
        if len(matches) > 1:
            return "Too Many matches to Show, Narrow your search to One contractor"
        elif len(matches) < 1:
            return "No Matches"
        else:
            return str(matches)
        