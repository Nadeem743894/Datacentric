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

navbar = generate_navbar(brand="")

for item in os.listdir(f"assets/front_page"):
    front_page_img = item

index_layout = html.Div(
    [
        navbar,
        html.Br(),
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
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="line-1",
                            figure=px.line(
                                pd.Series(),
                                title="Line 1",
                            ),
                        )
                    )
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="line-2",
                            figure=px.line(
                                pd.Series(),
                                title="Line 2",
                            ),
                        )
                    )
                ),
            ],
            align="center",
            justify="center",
        ),
        html.Div([
        html.H4('GPS location'),
        dcc.Graph(
            id='live-update-graph',
            figure=px.scatter_geo(
                pd.DataFrame(),
                title="GPS location"
                )
            ),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
    ]
)

### Set app layout to page container ###
app.layout = page_container

### Assemble all layouts ###
pages = []
pages.append(example.layout)
# pages.append(page_container)

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):

    fig = px.scatter_geo(
        ) 

    return fig

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