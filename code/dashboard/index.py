### Import Packages ###
from re import M
from venv import create
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import logging
from dash import Dash, dcc, html, Input, Output, callback

### Import Dash Instance and Pages ###
from app import app, colors
from navbar import generate_navbar
from pages import example
import plotly.graph_objects as go
import os
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
# config = configparser.ConfigParser()



markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

#### Use this space to provide a brief overview of the project, the dashboard, demonstrator or whatever details you want to convey to the customer.
'''

### Page container ###
page_container = html.Div(
    children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(
            id="url",
            refresh=False,
        ),
        # content will be rendered in this element
        html.Div(id="page-content"),
    ]
)

index_style = {
    "height": "40%",
    "width": "100%",
    "display": "inline-block",
    "vertical-align": "top",
}

navbar = generate_navbar(brand="Project Code - Project Title")

for item in os.listdir(f"assets/front_page"):
    front_page_img = item

index_layout = html.Div(
    [
        navbar,
        html.Br(),
        dcc.Markdown(children=markdown_text),     
        dbc.Row(
            [
                html.Img(
                    src=app.get_asset_url(f"front_page/{front_page_img}"),
                    style={"height": "60vh", "object-fit": "cover"},
                ),
            ],
            align="center",
            justify="center",
        ),
    ]
)

### Set app layout to page container ###
app.layout = page_container

### Assemble all layouts ###
pages = []
pages.append(example.layout)
pages.append(page_container)

app.validation_layout = html.Div(children=pages)
### Update Page Container ###
@app.callback(
    Output(
        component_id="page-content",
        component_property="children",
    ),
    [
        Input(
            component_id="url",
            component_property="pathname",
        )
    ],
)
def display_page(pathname):
    if pathname == "/":
        return index_layout
    elif pathname == "/example":
        return example.layout
    else:
        return "404"