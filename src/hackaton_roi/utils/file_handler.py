import pandas as pd
import streamlit as st
from utils.logger import log_action


def process_uploaded_file(uploaded_file) -> pd.DataFrame:
    """
    Reads and processes an uploaded file.

    Args:
        uploaded_file: The uploaded file object.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    log_action("File upload started", f"Filename: {uploaded_file.name}")
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xls", ".xlsx")):
            df = pd.read_excel(uploaded_file)
        else:
            raise ValueError("Unsupported file format")

        log_action("File processed successfully", f"Filename: {df}")

        return df.to_dict(orient="records")

    except Exception as e:
        log_action("File processing failed", str(e))
        st.error(
            f"Error processing the file. Please check the format and try again. ({e})"
        )
        return dict({})
