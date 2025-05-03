import streamlit as st
from model import BioBERTAttention
from visualize import plot_attention_heatmap
from fetch_data import fetch_pubmed_abstract
from entities import detect_entities

# Initialize session state for user_input
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

st.title("BioBERT Attention Visualization Tool")
st.write("Visualize attention patterns in BioBERT & highlight biomedical entities.")

# Initialize model
@st.cache_resource
def load_model():
    return BioBERTAttention()

bio_model = load_model()

# Input options
input_option = st.radio("Choose Input Type", ("Manual Text", "PubMed Abstract"))

if input_option == "Manual Text":
    st.session_state.user_input = st.text_area("Input Biomedical Text", "TP53 mutations are associated with breast cancer.")
else:
    query = st.text_input("PubMed Search Query", "TP53 breast cancer")
    if st.button("Fetch Abstract"):
        abstracts = fetch_pubmed_abstract(query, max_results=1)
        if abstracts:
            st.session_state.user_input = abstracts[0]
            st.text_area("Fetched Abstract", st.session_state.user_input, height=200)
        else:
            st.error("No abstracts found for the query. Please try a different search term.")
            st.session_state.user_input = ""

# Visualization settings
layer = st.slider("Select Layer", 0, 11, 0)
head = st.slider("Select Head", 0, 11, 0)
avg_attention = st.checkbox("Show Average Attention Across Layers and Heads")

if st.button("Visualize Attention"):
    if st.session_state.user_input.strip():
        # Get attention weights
        if avg_attention:
            tokens, attentions = bio_model.get_average_attention(st.session_state.user_input)
            title = "Average Attention Across Layers and Heads"
        else:
            tokens, attentions = bio_model.get_attention_weights(st.session_state.user_input, layer=layer, head=head)
            title = f"Attention (Layer {layer}, Head {head})"
        
        # Plot heatmap
        fig = plot_attention_heatmap(tokens, attentions, title=title)
        st.plotly_chart(fig)

        # Detect and display entities
        entities = detect_entities(st.session_state.user_input)
        if entities:
            st.subheader("Detected Biomedical Entities")
            for entity, label in entities:
                st.write(f"- {entity} ({label})")
        else:
            st.write("No biomedical entities detected.")
    else:
        st.error("Please enter or fetch some text before visualizing.")