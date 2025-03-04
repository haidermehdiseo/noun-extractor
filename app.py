import streamlit as st
import spacy

# Define the NLP model name
MODEL_NAME = "en_core_web_lg"  # High-accuracy NLP model

# Try loading the model
try:
    nlp = spacy.load(MODEL_NAME)
except OSError:
    st.error(f"Failed to load the model '{MODEL_NAME}'. Ensure it is installed correctly.")

def extract_entities(text):
    """Extracts named entities from the given text using spaCy."""
    doc = nlp(text)
    entities = [(ent.text.strip(), ent.label_) for ent in doc.ents if ent.label_ != "NORP"]  # Avoid non-useful entities
    return entities

# Streamlit UI
st.title("High-Accuracy Entity Extractor Tool")
st.write(f"Using NLP Model: **{MODEL_NAME}**")
st.write("Paste your article below, and click 'Extract Entities' to get precise results.")

text_input = st.text_area("Enter your article:")

if st.button("Extract Entities"):
    if text_input.strip():
        entities = extract_entities(text_input)
        if entities:
            st.subheader("Extracted Entities:")
            for entity, label in entities:
                st.write(f"**{entity}** ({label})")
        else:
            st.warning("No named entities found. Try another text.")
    else:
        st.warning("Please enter some text first.")
