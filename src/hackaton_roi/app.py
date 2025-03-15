import streamlit as st
import pandas as pd
from utils.logger import log_action
from utils.file_handler import handle_file_upload
from utils.manual_input import handle_manual_input

# Streamlit UI
st.title("Streamlit Data Input App")

# Radio buttons in a horizontal layout
selection = st.radio("Choose Data Input Method", ("Document", "Manual"), horizontal=True)

# Log user's choice
log_action("User Selection", f"Selected: {selection}")

df = None  # Initialize an empty DataFrame

if selection == "Document":
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xls', 'xlsx'])
    if uploaded_file:
        df = handle_file_upload(uploaded_file)

elif selection == "Manual":
    df = handle_manual_input()

# Display DataFrame if available
if df is not None:
    st.write("Data Preview:")
    st.dataframe(df, use_container_width=True)