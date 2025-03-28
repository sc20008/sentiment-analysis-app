import streamlit as st
from textblob import TextBlob

# Title
st.title("AI-Powered Sentiment Analysis")

# User input
user_input = st.text_area("Enter a sentence:")

if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        blob = TextBlob(user_input)
        sentiment_score = blob.sentiment.polarity

        # Display results
        if sentiment_score > 0:
            st.success(f"Positive 😊 (Score: {sentiment_score:.2f})")
        elif sentiment_score < 0:
            st.error(f"Negative 😞 (Score: {sentiment_score:.2f})")
        else:
            st.info(f"Neutral 😐 (Score: {sentiment_score:.2f})")
    else:
        st.warning("Please enter some text for analysis.")
