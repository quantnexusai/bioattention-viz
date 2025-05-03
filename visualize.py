import plotly.graph_objects as go
import numpy as np

def plot_attention_heatmap(tokens, attention_weights, title="Attention Heatmap"):
    fig = go.Figure(data=go.Heatmap(
        z=attention_weights,
        x=tokens,
        y=tokens,
        colorscale="Viridis"
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Tokens",
        yaxis_title="Tokens",
        xaxis=dict(tickangle=45),
        width=800,
        height=800
    )

    return fig