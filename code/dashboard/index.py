### Import Packages ###
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import logging
from dash import Dash, dcc, html, Input, Output, callback

### Import Dash Instance and Pages ###
from app import app, colors

import pages as pg
import inspect 

### organise imported into a dict to iterate
pages = {}
for name, module in inspect.getmembers(pg, predicate=inspect.ismodule):
    if name in pg.__all__:
        pages[name] = module

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

### Set app layout to page container ###
app.layout = page_container

### Assemble all layouts ###
layouts = [pages[name].layout for name in pages.keys()]
layouts.append(page_container)

app.validation_layout = html.Div(children=layouts)

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
    """
    Function to display a page based on the corresponding URL entered (or clicked via navbar)
    Args: 
        pathname (str) - the URL of the page entered (after localhost:8050/)
    Returns:
        layout (obj) or '404' (str) - the Dash layout of the new page, or a 404 error message
    """

    if pathname == "/":
        return pages['home'].layout
    for name in pages.keys():
        if pathname == f'/{name}':
            return pages[name].layout
    else:
        return '404'
