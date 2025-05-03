import streamlit as st
from visualize import plot_attention
from fetch_data import fetch_pubmed_abstract
from entities import get_entities
import init_model

init_model.install_scispacy_model()

st.title("BioBERT Attention Visualization Tool")
st.write("Visualize attention patterns in BioBERT and highlight biomedical entities.")

input_type = st.radio("Choose Input Type", ["Manual Text", "PubMed Abstract"])
text = st.text_area("Input Biomedical Text", "TP53 mutations are associated with breast cancer.")

if input_type == "PubMed Abstract":
    query = st.text_input("Enter PubMed Query", "TP53 breast cancer")
    if st.button("Fetch Abstract"):
        text = fetch_pubmed_abstract(query)
        st.write(text)

layer = st.slider("Select Layer", 0, 11, 8)
head = st.slider("Select Head", 0, 11, 4)
avg_attention = st.checkbox("Show Average Attention Across Layers and Heads")

if st.button("Visualize Attention"):
    try:
        fig = plot_attention(text, layer, head, avg_attention)
        st.plotly_chart(fig)
        entities = get_entities(text)
        st.write("Detected Entities:", entities)
    except Exception as e:
        st.error(f"Error: {e}. Visualization may be limited without scispacy.")