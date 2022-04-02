
import dash_html_components as html
import dash_table
from datetime import date, timedelta
import pandas as pd


def make_dash_table(df):

    df['id'] = df.index
    table = dash_table.DataTable(
        id='table', 
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns if i != 'id'],#columns=[{"name": i, "id": i} for i in df.columns],
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white'
        },
        style_data_conditional = df,
        editable=True,
        export_format="xlsx",
        export_headers="display"
    )
    return table