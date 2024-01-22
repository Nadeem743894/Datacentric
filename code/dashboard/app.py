### Import Packages ###
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


### AMRC branding overrides ###
colors = {
    "amrc-blue-light": "#6BBEFF",
    "amrc-blue": "#0053A1",
    "amrc-blue-hover": "#004A8F",
    "amrc-blue-dark": "#00203D",
}

#### Dash instance ###
external_stylesheets = [dbc.themes.DARKLY]
load_figure_template("darkly")
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)