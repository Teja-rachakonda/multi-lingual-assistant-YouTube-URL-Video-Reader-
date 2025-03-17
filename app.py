import streamlit as st
from models.sentiment_model import analyze_sentiment
from data.database import save_to_db
from utils.visualizations import show_sentiment_chart

# Set the title of the app
st.title("Sentiment Analysis App")

# Create a text area for user input
user_input = st.text_area("Enter text to analyze")

# Analyze button and logic
if st.button("Analyze"):
        result = analyze_sentiment(user_input)
        save_to_db(user_input, result)
        st.write(f"Sentiment: {result['label']}")
        st.write(f"Confidence: {result['score']:.2f}")

# Display sentiment chart
st.bar_chart(show_sentiment_chart())