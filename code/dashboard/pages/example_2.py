#########################################################################
### Imports 
from re import M
from venv import create
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output
from app import app, colors
from navbar import generate_navbar
import plotly.graph_objects as go
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
            id="interval-component-2", interval=1 * 1000, n_intervals=1  # in milliseconds
        ),
        html.Br(),
        ###############
        ### Components organised in columns and rows
        # html.H4("Scatter plots"),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 dcc.Graph(
        #                     id="scatter-3",
        #                     figure=px.line(
        #                         pd.Series(),
        #                         title="Scatter 1 - Increasing Signal",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
        #                     ),
        #                 )
        #             ),
        #             width=6,
        #         ),
        #         dbc.Col(
        #             html.Div(
        #                 dcc.Graph(
        #                     id="scatter-4",
        #                     figure=px.line(
        #                         pd.Series(),
        #                         title="Scatter 2 - Random Signal",  # Scatter plot docs: https://plotly.com/python/line-and-scatter/
        #                     ),
        #                 )
        #             ),
        #             width=6,
        #         ),
        #     ],
        #     align="center",
        #     justify="center",
        # ),
        html.Br(),
        ###############
        ### Components added straight to the layout
        html.Br(),  # line break between components
        # insert more content rows,
        html.Br(),
    ]
)
# #########################################################################
# ### Callbacks
# ### https://dash.plotly.com/basic-callbacks
# ### https://dash.plotly.com/advanced-callbacks
# ### Callbacks are functions you can define to update the graphs interactively
# ### They take Inputs
# ### Multiple components can update everytime interval gets fired.

# # Callback example 2
# # This callback takes 1 input (regular increasing button component) and returns 2 outputs (Figures to scatter-1 and scatter-2)
# @app.callback(
#     Output("scatter-3", "figure"),
#     Output("scatter-4", "figure"),
#     Input("interval-component-2", "n_intervals"),
# )
# def update_graph_live(n_intervals):
#     """
#     Function to update the scatter graphs in components scatter-3 and scatter-4.

#     Args: 
#         n_intervals (int) - the number of of seconds counted by the 'interval-component' since the app started 
#     Returns:
#         fig['scatter-3'] (obj) - the updated figure for component 'scatter-3'
#         fig['scatter-4'] (obj) - the updated figure for component 'scatter-4'
#     """

#     fig = {}
#     df = pd.DataFrame()
#     df["Random Signal"] = np.random.randint(0, n_intervals, n_intervals - 1)
#     df["Increasing Signal"] = np.linspace(0, n_intervals, n_intervals - 1)

#     fig["scatter-3"] = px.scatter(
#         df,
#         y="Random Signal",
#         color="Increasing Signal",
#         title="Scatter 1 - Random Signal",
#     )

#     fig["scatter-4"] = px.scatter(
#         df,
#         y="Increasing Signal",
#         color="Increasing Signal",
#         title="Scatter 2 - Increasing Signal",
#     )

#     return fig["scatter-3"], fig["scatter-4"]
