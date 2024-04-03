### Import Packages ###
from dash import html, dcc, Input, Output, ctx
import dash_bootstrap_components as dbc
from app import colors

def generate_navbar(brand):
    """
    Function to update the navbar at the top of each page.

    Args: 
        brand (str) - the title for the page 
    Returns:
        navbar (dbc) - dash bootstrap component defining the navbar
    """

    children = [dbc.NavItem(dbc.NavLink("Home", href="/"))]

    ### add new pages manually here with this syntax
    children.append(dbc.NavItem(dbc.NavLink("Example", href="/example")))
    # children.append(dbc.NavItem(dbc.NavLink("Example 2", href="/example_2"))) # uncomment this line to add the example_2 page to the navbar

    children.append(dbc.NavItem(
                html.Img(src="assets/thumbnails/amrc-logo-white.png", height="50px")
            ))
    
    navbar = dbc.NavbarSimple(
        children=children,
        brand=brand,
        brand_href="/",
        color=colors["amrc-teal"],
        dark=True,
        fluid=True,
    )

    return navbar
