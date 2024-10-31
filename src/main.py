# Plotly
import plotly
import plotly.express as px

from dash import Dash, html, dcc, Input, Output, State, callback, Patch
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import plotly.graph_objects as go

# Pandas
import pandas as pd

nac2018 = pd.read_csv('./src/data/NACIMIENTOS/nac2018.csv')

