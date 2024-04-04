### Import Packages ###
import dash
from dash import html, dcc, Input, Output, ctx

# from dash.dependencies import Input, Output#, ctx
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import os

### AMRC branding overrides ###
colors = {
    "amrc-blue-light": "#6BBEFF",
    "amrc-blue": "#0053A1",
    "amrc-blue-hover": "#004A8F",
    "amrc-blue-dark": "#00203D",
}


def generate_navbar(brand):

    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Example", href="/example")),
            dbc.NavItem(
                html.Img(src="assets/thumbnails/amrc-logo-white.png", height="50px")
            ),
        ],
        brand=brand,
        brand_href="/",
        color=colors["amrc-blue"],
        dark=True,
        fluid=True,
    )

    return navbar
