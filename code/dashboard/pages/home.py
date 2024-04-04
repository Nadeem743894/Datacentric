#########################################################################
### Imports 
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
from app import app, colors
from navbar import generate_navbar
import plotly.express as px
import pandas as pd
import numpy as np
import os 

navbar = generate_navbar(brand="Project Code - Project Title")


markdown_text = """
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

#### Use this space to provide a brief overview of the project, the dashboard, demonstrator or whatever details you want to convey to the customer.
"""

for item in os.listdir(f"assets/home_page"):
    home_page_img = item

layout = html.Div(
    [
        navbar,
        html.Br(),
        dcc.Markdown(children=markdown_text),
        dbc.Row(
            [
                html.Img(
                    src=app.get_asset_url(f"front_page/{home_page_img}"),
                    style={
                        "height": "60vh", 
                        "object-fit": "cover"
                        },
                ),
            ],
            align="center",
            justify="center",
        ),
    ]
)