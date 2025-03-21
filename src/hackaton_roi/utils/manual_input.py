import streamlit as st
from utils.logger import log_action


def collect_manual_input() -> dict:
    """
    Collects manual data input from the user and processes it with a single button.

    Returns:
        dict: Dictionary containing manually entered data or None if validation fails.
    """

    st.header("Business Questionnaire")

    # Question 1
    business_type = st.text_input(
        "What is your type of business? (Example: Restaurant, Online Store, Industry, SaaS)"
    )

    # Question 2
    has_investment = st.radio(
        "Do you already have a defined investment amount?", ["Yes", "No"]
    )
    investment_amount = None
    if has_investment == "Yes":
        investment_amount = st.text_input("How much is the investment amount?")

    # Question 3
    store_type = st.selectbox(
        "Will your company be physical, online, or hybrid?",
        ["", "Physical", "Online", "Hybrid"],
    )

    # Question 4
    rental_status = st.selectbox(
        "Do you already have a location or will you need to rent/buy a space?",
        [
            "",
            "I already have a location",
            "I'll need to rent",
            "I'll need to buy",
            "Not applicable",
        ],
    )

    # Question 5
    exact_location = st.text_input("What is the desired location of the business?")

    # Question 6
    sales_channel = st.multiselect(
        "How do you plan to sell?",
        ["Physical store", "Online", "Marketplace", "Franchise", "Other"],
    )

    # Question 7
    competitive_advantages = st.text_area("What are your main competitive advantages?")

    # Question 8
    has_marketing_strategy = st.radio(
        "Do you have an initial marketing strategy?", ["Yes", "No"]
    )
    marketing_strategy = None
    if has_marketing_strategy == "Yes":
        marketing_strategy = st.text_area("Describe your initial marketing strategy:")

    # Question 9
    has_experience = st.radio(
        "Do you have any experience selling this product/service?", ["Yes", "No"]
    )

    # Question 10
    work_structure = st.radio(
        "Will you work alone or hire employees?",
        ["Alone", "With employees", "Haven't decided yet"],
    )

    # Question 11
    has_emergency_fund = st.radio(
        "Do you have any money set aside for emergencies in case the business takes time to profit?",
        ["Yes", "No"],
    )

    # Question 12
    knows_breakeven = st.radio(
        "Do you know how to calculate how much you need to sell to cover your costs?",
        ["Yes", "No"],
    )

    # Question 13
    has_defined_price = st.radio(
        "Have you already defined a price for your product/service?", ["Yes", "No"]
    )

    # Submit button
    submit_button = st.button("Submit Form")

    if submit_button:
        # Validate inputs
        if business_type:
            business_data = {
                "business_type": business_type if business_type else "Not provided",
                "has_investment": has_investment,
                "investment_amount": (
                    investment_amount if investment_amount else "Not provided"
                ),
                "store_type": store_type if store_type else "Not provided",
                "rental_status": rental_status if rental_status else "Not provided",
                "exact_location": exact_location if exact_location else "Not provided",
                "sales_channel": sales_channel if sales_channel else "Not provided",
                "competitive_advantages": (
                    competitive_advantages if competitive_advantages else "Not provided"
                ),
                "has_marketing_strategy": has_marketing_strategy,
                "marketing_strategy": (
                    marketing_strategy if marketing_strategy else "Not provided"
                ),
                "has_experience": has_experience,
                "work_structure": work_structure,
                "has_emergency_fund": has_emergency_fund,
                "knows_breakeven": knows_breakeven,
                "has_defined_price": has_defined_price,
            }
            st.success("Form submitted successfully!")
            st.write("Collected data:")
            st.json(business_data)
            return business_data
        else:
            st.error("Please fill in at least the business type.")
            return None
