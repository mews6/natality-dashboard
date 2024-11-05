import hvplot.pandas
import numpy as np
import pandas as pd
import panel as pn
from plotly import subplots

PRIMARY_COLOR = "#0072B5"
SECONDARY_COLOR = "#B54300"
CSV_FILE = (
    "https://raw.githubusercontent.com/holoviz/panel/main/examples/assets/occupancy.csv"
)

pn.extension("plotly")
pn.extension(design="material", sizing_mode="stretch_width")

