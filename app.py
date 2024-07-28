import random
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("The GEMINI_API_KEY environment variable is not set.")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get financial advice from Gemini
def get_gemini_advice(prompt):
    response = model.generate_content(prompt)
    advice = response.text.strip()
    return advice

# Streamlit app
import streamlit as st
import streamlit_analytics

streamlit_analytics.start_tracking()

st.set_page_config(page_title="FinSafe - Your Personal Financial Advisor", page_icon="💰")

# Header
st.title("Welcome to FinSafe")
st.write("Your Personal Financial Advisor for Smart Saving, Investing, and Debt Management")

# Input fields
age = st.number_input("Age:", min_value=0, max_value=100)
income = st.number_input("Monthly Income ($):", min_value=0, max_value=99999999)
debt = st.number_input("Debt ($):", min_value=0, max_value=99999999)

if "advice_counter" not in st.session_state:
    st.session_state.advice_counter = 0

if "advice_generated" not in st.session_state:
    st.session_state.advice_generated = False

if "first_load" not in st.session_state:
    st.session_state.first_load = True

generate_advice = st.button("Generate Advice")
# Display financial advice
if generate_advice:
    st.session_state.advice_counter += 1  # Increment the advice counter
    st.session_state.advice_generated = True

    with st.spinner("Generating advice for you..."):
        sleep_time = random.uniform(4, 8)  # Generate random sleep time between 4 to 8 seconds
        time.sleep(sleep_time)  # Simulate loading

    # Generate advice using Gemini
    prompt = f"You are a kind and expert financial advisor. Provide financial advice for someone who is ${age} years old, has a monthly income of ${income}, and has ${debt} in debt. DO NOT ask for further input from the user."
    gemini_advice = get_gemini_advice(prompt)

    # Display advice
    if st.session_state.advice_generated:
        if st.session_state.first_load:
            st.session_state.first_load = False  # Set the flag to False

        if not st.session_state.first_load:
            st.subheader("Financial Advice:")

            if debt > 0:
                st.write("Priority: Pay off your debt as soon as possible to reduce financial stress.")

            st.write(gemini_advice)

# Footer
st.markdown("---")
st.write("© 2024 FinSafe. All rights reserved.")
st.write("Disclaimer: The financial advice provided here is for educational purposes only and should not be considered as personalized financial advice. It is recommended to consult with a qualified financial advisor before making any investment decisions")

streamlit_analytics.stop_tracking()