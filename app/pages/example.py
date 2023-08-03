### Import Packages ###
from re import M
from venv import create
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import logging

### Import Dash Instance and Pages ###
from app import app, colors
from navbar import generate_navbar
import plotly.graph_objects as go
import os
import configparser
import math

config = configparser.ConfigParser()

index_style = {
    "height": "40%",
    "width": "100%",
    "display": "inline-block",
    "vertical-align": "top",
}

navbar = generate_navbar(brand="IMG Data Science - Example")

layout = html.Div(
    children=[
        navbar,
        html.Br(),
        # insert content row,
        html.Br(),
    ]
)
