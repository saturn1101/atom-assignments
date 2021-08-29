import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Handpick Files")
input = st.file_uploader("Upload An Excel File")

if input is not None:
    try:
        df = pd.read_excel(input)
    except (ValueError, AssertionError):
        st.warning("Please upload an Excel file")
