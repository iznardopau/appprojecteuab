import streamlit as st
import pandas as pd

# Set the title of the app
st.markdown("<h1 style='color: #4CAF50; text-align: center;'>GuardIan</h1>", unsafe_allow_html=True)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f0f0;
        padding: 2rem;
    }
    .stTextInput, .stNumberInput {
        margin-bottom: 1rem;
    }
    .css-18e3th9 {
        color: #333333;
    }
    .css-1d391kg input {
        color: #333333 !important;
        border: 1px solid #4CAF50 !important;
        border-radius: 5px;
    }
    .css-1d391kg label {
        color: #4CAF50 !important;
        font-weight: bold;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input box for log
log = st.text_input("Log")

# Use columns to make input boxes smaller and more organized
cols = st.columns(5)
web = cols[0].number_input("Web", min_value=0, value=0)
ip = cols[1].number_input("IP", min_value=0, value=0)
date = cols[2].number_input("Date", min_value=0, value=0)
method = cols[3].number_input("Method", min_value=0, value=0)
link = cols[4].number_input("Link", min_value=0, value=0)

cols = st.columns(5)
http_version = cols[0].number_input("HTTP Version", min_value=0, value=0)
status_code = cols[1].number_input("Status Code", min_value=0, value=0)
bytes_sent = cols[2].number_input("Bytes Sent", min_value=0, value=0)
referrer = cols[3].number_input("Referrer", min_value=0, value=0)
user_agent = cols[4].number_input("User Agent", min_value=0, value=0)

# Placeholder for prediction (for demonstration purposes, it's a static value)
prediction = "Mikel virgen"

# Button to show the output
if st.button("Show Output"):
    # Create a DataFrame with the input values
    data = {
        "Log": [log],
        "Prediction": [prediction]
    }
    df = pd.DataFrame(data)
    
    # Display the DataFrame
    st.write("Output Data:")
    st.dataframe(df)
