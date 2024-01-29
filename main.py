# Import necessary libraries
import streamlit as st
import bomber
import asyncio
import pandas as pd

st.set_page_config(page_title='Keyword Generator', page_icon=':smiley:')
# Function to run asyncio code
def run_asyncio_code(keyword, country, api_key):
    return asyncio.run(bomber.get_keyword_data(keyword, country, api_key))


# Function to display Keyword Data
def display_keyword_data(keyword_data):
    st.markdown("## Keyword Data")
    for category, keywords in keyword_data.items():
        st.markdown(f"### {category}")
        df = pd.DataFrame.from_dict(keywords, orient='index').transpose()
        st.dataframe(df)

# Function to display AI Report
def display_ai_report(ai_report):
    st.markdown("## AI Analysis Report")
    st.markdown(ai_report)

# Streamlit UI layout
st.title("Keyword Generator")

st.write("Enter the details below to fetch keyword data. generate 100's of keyword with just a single keyword....")

input_keyword = st.text_input("Enter the keyword", "")
input_country = st.text_input("Enter your country", "")
API_KEY = "null"

if st.button("Fetch Data"):
    with st.spinner("Fetching data..."):
        result = run_asyncio_code(input_keyword, input_country, API_KEY)
        if result.get('success'):
            display_keyword_data(result['result']['keyword_data'])
            display_ai_report(result['result']['ai_report'])
        else:
            st.error("Failed to fetch data")
