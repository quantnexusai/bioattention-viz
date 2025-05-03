import sys
print("Python version:", sys.version)
print("Current file:", __file__)
import streamlit as st
from visualize import plot_attention

st.title("BioBERT Attention Visualization Tool")
st.write("Visualize attention patterns in BioBERT.")

input_type = st.radio("Choose Input Type", ["Manual Text", "PubMed Abstract"])
text = st.text_area("Input Biomedical Text", "TP53 mutations are associated with breast cancer.")

if input_type == "PubMed Abstract":
    from fetch_data import fetch_pubmed_abstract
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
    except Exception as e:
        st.error(f"Error: {e}")