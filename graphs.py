import plotly.graph_objects as go

def generate_line_chart_year_genres(df):
    
    line_plots = []
    for feature in df.columns[1:]:
        line_plot = go.Scatter(
            x=df['index'],
            y=df[feature],
            mode='lines+markers',
            name=feature
        )
        line_plots.append(line_plot)

    layout = go.Layout(
        xaxis=dict(title='Year'),
        yaxis=dict(title='Count'),
        title='Genre Count by Year - Line Chart',
        showlegend=True
    )

    fig_line = go.Figure(data=line_plots, layout=layout)

    return fig_line

def generate_heatmap_year_genres(df):
    df = df.set_index("index")
    heatmap = go.Heatmap(
        x=df.columns,
        y=df.index,
        z=df.values,
        colorscale='Blues'
    )

    layout_heatmap = go.Layout(
        xaxis=dict(title='Genres'),
        yaxis=dict(title='Year'),
        title='Genre Count by Year - Heatmap'
    )

    fig_heatmap = go.Figure(data=[heatmap], layout=layout_heatmap)

    return fig_heatmap


def generate_line_chart_score_group_genres(df):
    #df_plotly1 = df.reset_index()
    df_plotly1 = df
    line_plots = []
    for feature in df_plotly1.columns[1:]:
        line_plot = go.Scatter(
            x=df_plotly1['score-group'],
            y=df_plotly1[feature],
            mode='lines+markers',
            name=feature
        )
        line_plots.append(line_plot)

    layout = go.Layout(
        xaxis=dict(title='count'),
        yaxis=dict(title='score-group'),
        title='Genre Count by score-group - Line Chart',
        showlegend=True
    )

    fig = go.Figure(data=line_plots, layout=layout)

    return fig


def generate_table_score_group_genres(df):
    #df_plotly1 = df.reset_index()
    df_plotly1 = df
    bar_plots = []
    for feature in df_plotly1.columns[1:]:
        bar_plot = go.Bar(
            x=df_plotly1['score-group'],
            y=df_plotly1[feature],
            name=feature
        )
        bar_plots.append(bar_plot)

    layout = go.Layout(
        xaxis=dict(title='score-group'),
        yaxis=dict(title='count'),
        title='Genre Count by score-group - Bar Chart',
        barmode='group'
    )

    fig = go.Figure(data=bar_plots, layout=layout)

    return fig





def generate_heatmap_score_genres(df):
    df = df.set_index('score')
    heatmap = go.Heatmap(
        x=df.columns,
        y=df.index,
        z=df.values,
        colorscale='Blues'
    )

    layout = go.Layout(
        xaxis=dict(title='Genres'),
        yaxis=dict(title='score'),
        title='Genre Count by Score - Heatmap'
    )

    fig = go.Figure(data=[heatmap], layout=layout)

    return fig


def generate_heatmap_score_group_genres(df):
    df = df.set_index('score-group')
    heatmap = go.Heatmap(
        x=df.columns,
        y=df.index,
        z=df.values,
        colorscale='Blues'
    )

    layout = go.Layout(
        xaxis=dict(title='Genres'),
        yaxis=dict(title='score'),
        title='Genre Count by SCORE-GROUPS - Heatmap'
    )

    fig = go.Figure(data=[heatmap], layout=layout)
    return fig
   