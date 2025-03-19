import streamlit as st
import pandas as pd
from utils.logger import log_action

def collect_manual_input() -> pd.DataFrame:
    """
    Collects manual data input from the user.

    Returns:
        pd.DataFrame: DataFrame containing manually entered data.
    """
    st.subheader("Manual Data Entry")
    
    fields = ["Business Type", "Investment Amount", "Store Type", "Rental Status", "Exact Location"]
    field_inputs = {}
    
    for field in fields:
        field_inputs[field] = st.text_input(f"{field}:", help=f"Example input for {field}")
    
    if st.button("Submit Manual Data"):
        if all(field_inputs.values()):
            log_action("Manual data submission", str(field_inputs))
            df = pd.DataFrame([field_inputs])
            return df
        else:
            log_action("Manual data submission failed", "Some fields were left empty")
            st.error("All fields must be filled.")
            return pd.DataFrame()
