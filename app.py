from flask import Flask, render_template
import plotly.graph_objects as go
from graphs import generate_line_chart_year_genres, generate_heatmap_year_genres, generate_line_chart_score_group_genres, generate_table_score_group_genres, generate_heatmap_score_genres, generate_heatmap_score_group_genres
import pandas as pd

app = Flask(__name__)


# Read file for calling it
df_ex_combined = pd.read_csv('/Users/thienhtt20/Documents/nam3-sem2/DSDV_lab/project-dsdv/data-cleaned/df_ex_combined-manga.csv')
df_gen_sco = pd.read_csv('/Users/thienhtt20/Documents/nam3-sem2/DSDV_lab/project-dsdv/data-cleaned/df_gen_sco_manga.csv')
df_gen_sco_final = pd.read_csv('/Users/thienhtt20/Documents/nam3-sem2/DSDV_lab/project-dsdv/data-cleaned/df_gen_sco_final-manga.csv')


@app.route('/')
def index():
    
    line_graph_year_genres = generate_line_chart_year_genres(df_ex_combined)
    line_html_year = line_graph_year_genres.to_html(full_html=False, default_width="100%", default_height='500px')
    
    heat_map_year_genres = generate_heatmap_year_genres(df_ex_combined)
    heatmap_html_year = heat_map_year_genres.to_html(full_html=False, default_width="100%", default_height='500px')

    heat_map_score_genres = generate_heatmap_score_genres(df_gen_sco)
    heatmap_html_score = heat_map_score_genres.to_html(full_html=False, default_width="100%", default_height='500px')

    heat_map_score_group_genres = generate_heatmap_score_group_genres(df_gen_sco_final)
    heatmap_html_scoregroup = heat_map_score_group_genres.to_html(full_html=False, default_width="100%", default_height='500px')

    line_graph_score_group_genres = generate_line_chart_score_group_genres(df_gen_sco_final)
    line_html_score = line_graph_score_group_genres.to_html(full_html=False, default_width="100%", default_height='500px')

    table_score_group_genres = generate_table_score_group_genres(df_gen_sco_final)
    table_html_score = table_score_group_genres.to_html(full_html=False, default_width="100%", default_height='500px')

    # Render the HTML template with the graph
    return render_template('index.html', linegraph_html=line_html_year, heatmap_html_year=heatmap_html_year,
                           heatmap_html_score=heatmap_html_score, heatmap_html_scoregroup=heatmap_html_scoregroup,
                           line_html_score=line_html_score, table_html_score=table_html_score)

if __name__ == '__main__':
    app.run(debug=True)
