import streamlit as st
from document_loader import load_pdf
from rag_pipeline import build_vector_store, get_relevant_chunks, generate_answer

st.set_page_config(page_title="Chat avec votre PDF", layout="centered")
st.title("Chatbot RAG avec votre document PDF")

# Upload du document
uploaded_file = st.file_uploader("Uploadez un document PDF", type=["pdf"])

if uploaded_file and "vectorstore" not in st.session_state:
    with st.spinner("Chargement et indexation du document..."):
        text = load_pdf(uploaded_file)
        st.session_state.vectorstore = build_vector_store(text)
    st.success("Document indexé avec succès")

# Champ de question
if "vectorstore" in st.session_state:
    question = st.text_input("Posez une question sur le document")
    if question:
        with st.spinner("Recherche en cours..."):
            docs = get_relevant_chunks(question, st.session_state.vectorstore)
            context = "\n\n".join([doc.page_content for doc in docs])
            answer = generate_answer(question, context)
        st.markdown(f"**Réponse :** {answer}")
