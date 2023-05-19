import plotly.graph_objects as go

def generate_line_chart(df):
    # Convert the dataframe to a Plotly-compatible format
    df_plotly = df
    

    # Create line plots for each feature
    line_plots = []
    for feature in df_plotly.columns[1:]:
        line_plot = go.Scatter(
            x=df_plotly['index'],
            y=df_plotly[feature],
            mode='lines+markers',
            name=feature
        )
        line_plots.append(line_plot)

    # Create the layout for line chart
    layout_line = go.Layout(
        xaxis=dict(title='Year'),
        yaxis=dict(title='Count'),
        title='Genre Count by Year - Line Chart',
        showlegend=True
    )

    # Create the figure for line chart
    fig_line = go.Figure(data=line_plots, layout=layout_line)

    return fig_line

def generate_heatmap(df):
    # Create the heatmap
    df = df.set_index("index")
    heatmap = go.Heatmap(
        x=df.columns,
        y=df.index,
        z=df.values,
        colorscale='Blues'
    )

    # Create the layout for heatmap
    layout_heatmap = go.Layout(
        xaxis=dict(title='Genres'),
        yaxis=dict(title='Year'),
        title='Genre Count by Year - Heatmap'
    )

    # Create the figure for heatmap
    fig_heatmap = go.Figure(data=[heatmap], layout=layout_heatmap)

    return fig_heatmap
