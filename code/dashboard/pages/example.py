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

#########################################################################
### Initialisation

# index_style = {
#     "height": "40%",
#     "width": "100%",
#     "display": "inline-block",
#     "vertical-align": "top",
# }

# load a static signal from the /data/external folder in the template, which executes once when the page is opened
df_static = pd.read_csv('../data/external/example_data.csv')

navbar = generate_navbar(brand="Project - Example")

#########################################################################
### Layout
### docs: https://dash.plotly.com/layout
### This section controls the layout of the page

layout = html.Div(
    children=[
        ###############
        ### The navigation bar
        navbar,
        html.Br(),
        ###############
        ### Intervals and interactions
        dcc.Interval(
            id="interval-component", interval=1 * 1000, n_intervals=1  # in milliseconds
        ),
        dbc.Row(
            dbc.Col(
                html.Button(
                    "Button - change length of Line 2",
                    id="button-click",
                    n_clicks=5,
                    style={
                        "font-size": "24px",
                        "backgroundColor": colors['amrc-deep-violet'],
                        "color": "white",
                    },
                ),
                width={"size": 3, "offset": 5},
            ),
        ),
        html.Br(),
        ###############
        ### Components organised in columns and rows
        html.H4("Line plots"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="line-1",
                            figure=px.line(
                                df_static,
                                y="Static Signal",
                                color_discrete_sequence=[colors['amrc-powder-blue']],
                                title="Line 1 - Static Signal, loaded from /data/external/example_data.csv",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
                            ),
                        )
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="line-2",
                            figure=px.line(
                                pd.Series(),
                                title="Line 2 - Random Signal",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
                            ),
                        )
                    ),
                    width=6,
                ),
            ],
            align="center",
            justify="center",
        ),
        html.H4("Scatter plots"),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="scatter-1",
                            figure=px.line(
                                pd.Series(),
                                title="Scatter 1 - Increasing Signal",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
                            ),
                        )
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.Div(
                        dcc.Graph(
                            id="scatter-2",
                            figure=px.line(
                                pd.Series(),
                                title="Scatter 2 - Random Signal",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
                            ),
                        )
                    ),
                    width=6,
                ),
            ],
            align="center",
            justify="center",
        ),
        html.Br(),
        ###############
        ### Components added straight to the layout
        html.Br(),  # line break between components
        # insert more content rows,
        html.Br(),
    ]
)
#########################################################################
### Callbacks
### https://dash.plotly.com/basic-callbacks
### https://dash.plotly.com/advanced-callbacks
### Callbacks are functions you can define to update the graphs interactively
### They take Inputs
### Multiple components can update everytime interval gets fired.

# Callback example 1
# This callback takes 2 inputs (number of button clicks, regular increasing button component) and returns one output (Figure to line-2)
@app.callback(
    Output("line-2", "figure"),
    Input("button-click", "n_clicks"),
    Input("interval-component", "n_intervals"),
)
def update_graph_live(n_clicks, n_intervals):
    """
    Function to update the line graph in component line-2.

    Args: 
        n_clicks (int) - the number of times the button 'button-click' has been clicked
        n_intervals (int) - the number of of seconds counted by the 'interval-component' since the app started 
    Returns:
        fig (obj) - the updated figure object, to 'line-2'
    """

    df = pd.DataFrame()
    df["Random Signal"] = pd.DataFrame(
        np.random.randint(0, n_intervals, size=(n_clicks * 20, 1))
    )
    fig = px.line(
        df, 
        y="Random Signal", 
        title="Line 2 - Random signal",
        color_discrete_sequence=[colors['amrc-powder-blue']]
        )

    return fig


# Callback example 2
# This callback takes 1 input (regular increasing button component) and returns 2 outputs (Figures to scatter-1 and scatter-2)
@app.callback(
    Output("scatter-1", "figure"),
    Output("scatter-2", "figure"),
    Input("interval-component", "n_intervals"),
)
def update_graph_live(n_intervals):
    """
    Function to update the scatter graphs in components scatter-1 and scatter-2.

    Args: 
        n_intervals (int) - the number of of seconds counted by the 'interval-component' since the app started 
    Returns:
        fig['scatter-1'] (obj) - the updated figure for component 'scatter-1'
        fig['scatter-2'] (obj) - the updated figure for component 'scatter-2'
    """

    fig = {}
    df = pd.DataFrame()
    df["Random Signal"] = np.random.randint(0, n_intervals, n_intervals - 1)
    df["Increasing Signal"] = np.linspace(0, n_intervals, n_intervals - 1)

    fig["scatter-1"] = px.scatter(
        df,
        y="Random Signal",
        color="Increasing Signal",
        color_continuous_scale=[colors['amrc-deep-violet'], colors['amrc-peach']],
        title="Scatter 1 - Random Signal",
    )

    fig["scatter-2"] = px.scatter(
        df,
        y="Increasing Signal",
        color="Increasing Signal",
        color_continuous_scale=[colors['amrc-deep-violet'], colors['amrc-peach']],
        title="Scatter 2 - Increasing Signal",
    )

    return fig["scatter-1"], fig["scatter-2"]
