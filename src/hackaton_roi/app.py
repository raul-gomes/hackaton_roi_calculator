import streamlit as st
import pandas as pd
import logging
import uuid
from datetime import datetime
from typing import Optional

# Configure Logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_action(action: str, details: str = "") -> None:
    """
    Logs user actions with a unique identifier.

    Parameters:
    action (str): Description of the action performed.
    details (str): Additional details related to the action.

    Returns:
    None
    """
    action_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"Action ID: {action_id} | Action: {action} | Timestamp: {timestamp} | Details: {details}"
    logging.info(log_entry)

def handle_file_upload(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> Optional[pd.DataFrame]:
    """
    Handles file upload and reads the content as a DataFrame.

    Parameters:
    uploaded_file (st.runtime.uploaded_file_manager.UploadedFile): The uploaded CSV, XLS, or XLSX file.

    Returns:
    Optional[pd.DataFrame]: A DataFrame containing the file data, or None if an error occurs.
    """
    try:
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a CSV, XLS, or XLSX file.")
                log_action("File Upload Error", f"Unsupported format: {uploaded_file.name}")
                return None

            df.reset_index(drop=True, inplace=True)  # Ensure the index is not treated as a separate column

            log_action("File Uploaded", f"File: {uploaded_file.name} | Rows: {len(df)}")
            return df

    except Exception as e:
        st.error(f"Error reading file: {e}")
        log_action("File Upload Error", str(e))
        return None

def handle_manual_input() -> Optional[pd.DataFrame]:
    """
    Handles manual data entry from the user.

    The user inputs values for three predefined fields: "Field 1", "Field 2", and "Field 3".
    
    Returns:
    Optional[pd.DataFrame]: A DataFrame containing the user-entered data, or None if an error occurs.
    """
    try:
        value1: str = st.text_input("Enter value for Field 1")
        value2: str = st.text_input("Enter value for Field 2")
        value3: str = st.text_input("Enter value for Field 3")

        if st.button("Submit Data"):
            if not value1 or not value2 or not value3:
                st.error("Please enter values for all fields.")
                log_action("Manual Input Error", "Missing values")
                return None
            
            df = pd.DataFrame({
                "Field 1": [value1],
                "Field 2": [value2],
                "Field 3": [value3]
            })

            log_action("Manual Data Entered", f"Values: {value1}, {value2}, {value3}")
            return df

    except Exception as e:
        st.error(f"Error in manual entry: {e}")
        log_action("Manual Input Error", str(e))
        return None

# Streamlit UI
st.title("Streamlit Data Input App")

# Radio buttons in a horizontal layout
selection: str = st.radio("Choose Data Input Method", ("Document", "Manual"), horizontal=True)

# Log user's choice
log_action("User Selection", f"Selected: {selection}")

# Handle file upload option
if selection == "Document":
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=['csv', 'xls', 'xlsx'])
    
    if uploaded_file is not None:
        df = handle_file_upload(uploaded_file)
        if df is not None:
            st.write("Uploaded Data:")
            st.dataframe(df, use_container_width=True)

# Handle manual input option
elif selection == "Manual":
    df = handle_manual_input()
    if df is not None:
        st.write("Entered Data:")
        st.dataframe(df, use_container_width=True)

# Error handling for unexpected cases
else:
    st.error("Please select a valid option.")
    log_action("Error", "Invalid selection")
