import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging

# -------------------------------
# Streamlit Config
# -------------------------------
st.set_page_config(
    page_title="AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

logging.basicConfig(level=logging.ERROR)

# -------------------------------
# Configure Gemini API
# -------------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# -------------------------------
# Force Model: Gemini 2.5 Flash
# -------------------------------
MODEL_NAME = "gemini-2.5-flash"

# -------------------------------
# UI
# -------------------------------
st.title("🤖 Gemini AI ChatBot")
st.caption("Powered by Gemini 2.5 Flash")

st.subheader("💬 Ask a Question")

question = st.text_input("", placeholder="Ask anything about tech, coding, or AI...")

# -------------------------------
# Safe Generate Function
# -------------------------------
def safe_generate(prompt: str) -> str:
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(
            f"You are an AI updated till 2026. Answer accurately.\n\nUser: {prompt}"
        )
        return response.text
    except Exception as e:
        logging.error(f"Generation error: {e}")
        return "⚠️ AI is temporarily unavailable. Please try again later."

# -------------------------------
# Buttons
# -------------------------------
if st.button("Get Response"):
    if question.strip():
        with st.spinner("Thinking..."):
            output = safe_generate(question)
            st.success(output)
    else:
        st.warning("Please enter a question.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Google Gemini API")