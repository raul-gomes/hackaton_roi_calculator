import streamlit as st
import pandas as pd
from utils.logger import log_action
from typing import Optional

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
