from flask import Flask, render_template
import plotly.graph_objects as go
from graphs import generate_line_chart, generate_heatmap
import pandas as pd

app = Flask(__name__)
# Read file for calling it
df_ex_combined = pd.read_csv('/Users/thienhtt20/Documents/nam3-sem2/DSDV_lab/project-dsdv/data-cleaned/df_ex_combined-manga.csv')

@app.route('/')
def index():
    
    line_graph = generate_line_chart(df_ex_combined)
    line_html = line_graph.to_html(full_html=False, default_width="100%", default_height='500px')
    
    heat_map = generate_heatmap(df_ex_combined)
    heatmap_html = heat_map.to_html(full_html=False, default_width="100%", default_height='500px')

    # Render the HTML template with the graph
    return render_template('index.html', line_html=line_html, heatmap_html=heatmap_html)

if __name__ == '__main__':
    app.run(debug=True)
