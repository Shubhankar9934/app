import streamlit as st
import torch
from transformers import pipeline

# Initialize the translation pipeline
translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")

# Define the translation function
def translate_transformers(input_text):
    results = translation_pipeline(input_text)
    return results[0]['translation_text']

# Streamlit app
st.title("Spanish to English Translator")
st.write("Enter Spanish text to get the English translation.")

# Input text box
input_text = st.text_area("Spanish Text", "")

# When the button is pressed
if st.button("Translate"):
    if input_text:
        translation = translate_transformers(input_text)
        st.write("### English Translation")
        st.write(translation)
    else:
        st.write("Please enter text to translate.")

# To run the app, save this script and run `streamlit run script_name.py` in the terminal.
