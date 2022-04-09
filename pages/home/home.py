import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import assets
from app import app
import pandas as pd
import os
import plotly.express as px
from pages.home import home_callbacks
from pages.home import home_data
from utils.constants import titles, git_links, medium_links, images
import base64

def get_card_content(image = None, header = "Project X", git_link = "link to git", medium_link = "Link to medium"):
    width = 280
    card_content = [
        dbc.CardImg(src=image, top=True),
        dbc.CardBody(
            [
                html.H4(header, className="card-title"),
                dbc.Col([
                    html.A(dbc.Button("The Code", color="dark", style={"width":width}), href=git_link, style={"padding-bottom":10}), 
                    html.A(dbc.Button("An Article", color="dark", style={"width":width}), href=medium_link, style={"padding-bottom":10}), 
                    ], 
                    align="center"),
            ])
    ]
    return card_content
    

def get_cards():
    width = 300
    cards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(get_card_content(image = images[0], header = titles[0], git_link = git_links[0], medium_link = medium_links[0]), style={"width": width}, color="dark", outline=True)),
                    dbc.Col(dbc.Card(get_card_content(image = images[1], header = titles[1], git_link = git_links[1], medium_link = medium_links[1]), style={"width": width}, color="dark", outline=True)),
                    dbc.Col(dbc.Card(get_card_content(image = images[2], header = titles[2], git_link = git_links[2], medium_link = medium_links[2]), style={"width": width}, color="dark", outline=True)),
                ],
                justify="evenly",
                className="mb-4",
            ),
            dbc.Row(
                [
                    dbc.Col(dbc.Card(get_card_content(image = images[3], header = titles[3], git_link = git_links[3], medium_link = medium_links[3]), style={"width": width}, color="dark", outline=True)),
                    dbc.Col(dbc.Card(get_card_content(image = images[4], header = titles[4], git_link = git_links[4], medium_link = medium_links[4]), style={"width": width}, color="dark", outline=True)),
                    dbc.Col(dbc.Card(get_card_content(image = images[5], header = titles[5], git_link = git_links[5], medium_link = medium_links[5]), style={"width": width}, color="dark", outline=True)),
                ],
                justify="evenly",
                className="mb-4",
            ),
        ]
    )
    return cards

layout = dbc.Container([
    dbc.Row(
        [
            get_cards()
        ],
        justify="between",
    ),
    html.Div(id='dummy-display', children = [])
])
