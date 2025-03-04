import streamlit as st
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_nouns(text):
    doc = nlp(text)
    return set([token.text for token in doc if token.pos_ == "NOUN"])

# Streamlit UI
st.title("Noun Extractor Tool")
st.write("Paste your article below, and click 'Extract Nouns'.")

text_input = st.text_area("Enter your article:")

if st.button("Extract Nouns"):
    if text_input.strip():
        nouns = extract_nouns(text_input)
        st.subheader("Extracted Nouns:")
        st.write(", ".join(nouns))
    else:
        st.warning("Please enter some text first.")
