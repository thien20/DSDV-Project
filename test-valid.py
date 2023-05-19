from flask import Flask, render_template
import plotly.graph_objects as go
from graphs import generate_line_chart, generate_heatmap
import pandas as pd


df = pd.read_csv('/Users/thienhtt20/Documents/nam3-sem2/DSDV_lab/project-dsdv/data-cleaned/df_ex_combined-manga.csv')
df.index