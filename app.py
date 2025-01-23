import streamlit as st
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader
from transformers import pipeline

# Initialize models
retrieval_model = SentenceTransformer('all-MiniLM-L6-v2')  # Embedding model
generation_model = pipeline("text-generation", model="distilgpt2")  # Generative model
dimension = 384
index = faiss.IndexFlatL2(dimension)  # FAISS index

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ''.join([page.extract_text() for page in reader.pages])
    return text

def parse_pnl_table(text):
    lines = text.split("\n")
    pnl_data = [
        line.split()[:6] for line in lines if any(keyword in line.lower() for keyword in ["revenue", "expenses", "profit"])
    ]
    return pd.DataFrame(pnl_data, columns=["Metric", "Q1", "Q2", "Q3", "Q4", "Year"])

def store_embeddings_in_faiss(df):
    texts = [
        f"{row['Metric']} Q1: {row['Q1']}, Q2: {row['Q2']}, Q3: {row['Q3']}, Q4: {row['Q4']}, Year: {row['Year']}"
        for _, row in df.iterrows()
    ]
    vectors = np.array([retrieval_model.encode(text) for text in texts]).astype("float32")
    index.add(vectors)
    return texts

def query_rag(query, texts):
    query_vector = np.array(retrieval_model.encode(query)).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_vector, k=1)
    retrieved_text = texts[indices[0][0]]
    input_prompt = f"Query: {query}\nRetrieved Information: {retrieved_text}\nResponse:"
    response = generation_model(input_prompt, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"], retrieved_text

st.title("Financial QA Bot")

uploaded_file = st.file_uploader("Upload P&L PDF", type="pdf")
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    pnl_table = parse_pnl_table(text)
    st.write("Parsed P&L Data:")
    st.dataframe(pnl_table)

    texts = store_embeddings_in_faiss(pnl_table)
    st.success("Embeddings stored successfully!")

    query = st.text_input("Ask a financial question:")
    if query:
        response, retrieved_text = query_rag(query, texts)
        st.write("Retrieved Information:", retrieved_text)
        st.write("Generated Response:", response)
