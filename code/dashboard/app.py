### Import Packages ###
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

### AMRC branding overrides ###
colors = {
    # primary colour palette, use these for the most part
    "amrc-sky-blue": "#64CBE8",
    "amrc-teal": "#005A8F",
    "amrc-midnight-black": "#131E29",
    "amrc-midnight-black-5": "#EDEDF1",
    
    # secondary colour palette, can be use sparingly for additional impact + versatility
    "amrc-deep-violet": "#440099",
    "amrc-mint-green": "#00CE7C",
    "amrc-mauve": "#663DB3",
    "amrc-coral": "#E7004C",
    "amrc-aqua": "#00BBCC",
    "amrc-spearmint": "#3BD4AE",
    "amrc-purple": "#981F92",
    "amrc-flamingo": "#FF6371",
    "amrc-powder-blue": "#9ADBE8",
    "amrc-pastel-green": "#A1DED2",
    "amrc-lavender": "#DAA8E2",
    "amrc-peach": "#FF9664",
}

#### Dash instance ###
external_stylesheets = [dbc.themes.DARKLY]
load_figure_template("darkly")
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)