import streamlit as st
import spacy
import subprocess

# Check if the language model is installed, if not, install it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.warning("Downloading 'en_core_web_sm' model...")
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
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
