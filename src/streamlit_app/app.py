import streamlit as st
import numpy as np
import plotly.express as px
from src.core.embeddings.storage import EmbeddingStorage
from src.core.dimensionality.pca import compute_pca

st.set_page_config(page_title="Multimodal Embedding Explorer", layout="wide")
st.title("🔍 Multimodal Embedding Explorer")

# Load HDF5 embeddings
storage = EmbeddingStorage("embeddings.h5")

emb_type = st.selectbox("Select Embedding Type", ["image", "text"])

try:
    ids = storage.list_ids(emb_type)
    embeddings = np.array([storage.load_embedding(emb_type, id_) for id_ in ids])

    # PCA projection
    coords = compute_pca(embeddings)

    df = {
        "x": coords[:, 0],
        "y": coords[:, 1],
        "label": ids,
    }

    st.subheader("2D PCA Projection")
    fig = px.scatter(df, x="x", y="y", text="label", hover_name="label", height=700)
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.warning(f"Could not load embeddings: {e}")
