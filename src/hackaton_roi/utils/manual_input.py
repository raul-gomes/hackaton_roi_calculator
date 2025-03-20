import streamlit as st
from utils.logger import log_action


def collect_manual_input() -> dict:
    """
    Collects manual data input from the user and processes it with a single button.

    Returns:
        dict: Dictionary containing manually entered data or None if validation fails.
    """
    with st.form("business_info_form"):
        business_type = st.text_input(
            "What is your type of business?",
            help="Example: 'I want to open a unisex clothing store in my neighborhood.'",
        )
        investment_amount = st.text_input(
            "Do you already have a defined amount to invest?",
            help="Example: 'No, I don't know yet.'",
        )
        store_type = st.radio(
            "Will the store be physical or online?",
            ["Physical", "Online"],
            horizontal=True,
        )
        rental_status = st.radio(
            "Do you want to rent a commercial space or do you already have a location?",
            ["I will need to rent.", "I already have a location."],
            horizontal=True,
        )
        exact_location = st.text_input(
            "What is the exact location?",
            help="Example: 'Goiânia neighborhood, Belo Horizonte.'",
        )

        # Single button for submitting and processing
        submitted = st.form_submit_button("Submit and Generate Analysis")

    # Validate inputs
    if submitted:
        if not all(
            [
                business_type,
                investment_amount,
                store_type,
                rental_status,
                exact_location,
            ]
        ):
            log_action("Manual input failed", "All fields are required")
            st.error("All fields are required. Please fill them in.")
            return None  # Return None if any field is empty
        else:
            business_data = {
                "What is your type of business?": [business_type],
                "Do you already have a defined amount to invest?": [investment_amount],
                "Will the store be physical or online?": [store_type],
                "Do you want to rent a commercial space or do you already have a location?": [
                    rental_status
                ],
                "What is the exact location?": [exact_location],
            }
            log_action("Manual input collected", f"Data: {business_data}")
            return business_data  # Return collected data

    return None  # Default return if no submission occurs
