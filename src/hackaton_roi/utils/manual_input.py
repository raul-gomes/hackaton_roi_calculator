import streamlit as st
from utils.logger import log_action


def collect_manual_input() -> dict:
    """
    Collects manual data input from the user and processes it with a single button.

    Returns:
        dict: Dictionary containing manually entered data or None if validation fails.
    """

    business_type = st.text_input(
        "What is your type of business?",
        help="Example: 'I want to open a unisex clothing store in my neighborhood.'",
        key="business_type_input",
    )
    investment_amount = st.text_input(
        "Do you already have a defined amount to invest?",
        help="Example: 'No, I don't know yet.'",
        key="investment_amount_input",
    )
    store_type = st.radio(
        "Will the store be physical or online?",
        ["Physical", "Online"],
        horizontal=True,
        key="store_type_radio",
    )
    rental_status = st.radio(
        "Do you want to rent a commercial space or do you already have a location?",
        ["I will need to rent.", "I already have a location."],
        horizontal=True,
        key="rental_status_radio",
    )
    exact_location = st.text_input(
        "What is the exact location?",
        help="Example: 'Goiânia neighborhood, Belo Horizonte.'",
        key="exact_location_input",
    )

    # Validate inputs
    if any(
        [business_type, investment_amount, store_type, rental_status, exact_location]
    ):
        business_data = {
            "What is your type of business?": (
                business_type if business_type else "Not provided"
            ),
            "Do you already have a defined amount to invest?": (
                investment_amount if investment_amount else "Not provided"
            ),
            "Will the store be physical or online?": (
                store_type if store_type else "Not provided"
            ),
            "Do you want to rent a commercial space or do you already have a location?": (
                rental_status if rental_status else "Not provided"
            ),
            "What is the exact location?": (
                exact_location if exact_location else "Not provided"
            ),
        }
        log_action("Manual input collected", f"Data: {business_data}")
        return business_data
    else:
        log_action("Manual input failed", "At least one field is required")
        st.error("At least one field is required. Please fill them in.")
        return None
