import streamlit as st
import pandas as pd
from utils.logger import log_action
from typing import Optional

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
