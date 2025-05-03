import plotly.graph_objects as go
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

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

def plot_attention(text, layer, head, avg_attention):
    # Load BioBERT
    tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
    model = AutoModel.from_pretrained("dmis-lab/biobert-v1.1", output_attentions=True)

    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    # Get attention weights
    with torch.no_grad():
        outputs = model(**inputs)
        attention = outputs.attentions[layer][0][head].numpy()

    # Average attention across layers and heads if specified
    if avg_attention:
        attention = torch.stack(outputs.attentions).mean(dim=0).mean(dim=1)[0].numpy()

    # Plot heatmap
    return plot_attention_heatmap(tokens, attention, title=f"Layer {layer} Head {head}")