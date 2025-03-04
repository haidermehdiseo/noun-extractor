import streamlit as st
import spacy

# Define the NLP model name
MODEL_NAME = "en_core_web_lg"  # High-accuracy NLP model

# Try loading the model
try:
    nlp = spacy.load(MODEL_NAME)
except OSError:
    st.error(f"Failed to load the model '{MODEL_NAME}'. Ensure it is installed correctly.")

def extract_nouns(text):
    doc = nlp(text)
    return set([token.text for token in doc if token.pos_ == "NOUN"])

# Streamlit UI
st.title("High-Accuracy Noun Extractor Tool")
st.write(f"Using NLP Model: **{MODEL_NAME}**")
st.write("Paste your article below, and click 'Extract Nouns' to get precise results.")

text_input = st.text_area("Enter your article:")

if st.button("Extract Nouns"):
    if text_input.strip():
        nouns = extract_nouns(text_input)
        st.subheader("Extracted Nouns:")
        st.write(", ".join(nouns))
    else:
        st.warning("Please enter some text first.")
