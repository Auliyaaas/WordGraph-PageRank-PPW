import streamlit as st
import pandas as pd
import streamlit as st
import nltk

from utils.pdf_reader import extract_text_from_pdf
from utils.preprocessing import sentences_from_text, build_terms
from utils.cooccurrence import build_cooccurrence_matrix
from utils.graph_analysis import build_filtered_graph, compute_all_centrality
from utils.visualization import draw_graph

@st.cache_resource
def download_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')

download_nltk()

st.set_page_config(page_title="Word Graph Centrality PDF", layout="wide")


st.title("📄 Analisis Word Graph & Centrality dari PDF")
st.write("Upload **1 file PDF**, sistem akan memproses seluruh tahapan seperti pada IPYNB.")


min_weight = st.sidebar.slider("Minimal Bobot Ko-okurensi", 1, 10, 5)
window_size = st.sidebar.slider("Ukuran Window", 1, 5, 2)


uploaded_pdf = st.file_uploader("Upload PDF", type=['pdf'])

if uploaded_pdf:
    with st.spinner("Mengekstrak teks PDF..."):
        text = extract_text_from_pdf(uploaded_pdf)

    sentences = sentences_from_text(text)
    terms = build_terms(sentences)

    st.success(f"Total kalimat: {len(sentences)} | Total term: {len(terms)}")

    co_df = build_cooccurrence_matrix(terms, window_size)
    Gf = build_filtered_graph(co_df, min_weight)

    pr_df, summary_df, subgraph = compute_all_centrality(Gf)

    st.subheader("🏆 Top 20 Kata (PageRank)")
    st.dataframe(pr_df, use_container_width=True)

    st.subheader("📊 Ringkasan Semua Centrality")
    st.dataframe(summary_df, use_container_width=True)

    st.subheader("🕸️ Visualisasi Subgraph Top-20")
    fig = draw_graph(subgraph, "Word Graph Top-20")
    st.pyplot(fig)

    st.download_button(
    "⬇️ Download CSV Hasil",
    summary_df.to_csv(index=False).encode('utf-8'),
    "hasil_ekstraksi_kata_kunci.csv",
    "text/csv"
    )


else:

    st.info("Silakan upload satu file PDF untuk memulai.")
