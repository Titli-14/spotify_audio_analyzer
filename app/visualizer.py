import plotly.graph_objects as go

def plot_features(features):
    if "error" in features:
        return None

    labels = list(features.keys())
    values = list(features.values())

    fig = go.Figure(data=[
        go.Bar(name='Audio Features', x=labels, y=values, marker_color='indigo')
    ])

    fig.update_layout(
        title="Spotify Audio Feature Analysis",
        xaxis_title="Feature",
        yaxis_title="Value",
        template="plotly_dark"
    )

    return fig
