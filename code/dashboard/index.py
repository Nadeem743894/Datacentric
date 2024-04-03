### Import Packages ###
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
import logging
from dash import Dash, dcc, html, Input, Output, callback

### Import Dash Instance and Pages ###
from app import app, colors
from navbar import generate_navbar
import os

import pages as pg
import inspect 

### organise imported into a dict to iterate
pages = {}
for name, module in inspect.getmembers(pg, predicate=inspect.ismodule):
    if name in pg.__all__:
        pages[name] = module

markdown_text = """
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!

#### Use this space to provide a brief overview of the project, the dashboard, demonstrator or whatever details you want to convey to the customer.
"""

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
                    style={
                        "height": "30vh", 
                        "object-fit": "cover"
                        },
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

    for name in pages.keys():
        if pathname == f'/{name}':
            return pages[name].layout
    if pathname == "/":
        return index_layout
    else:
        return '404'
