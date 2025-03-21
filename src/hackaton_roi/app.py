import streamlit as st
import pandas as pd
import json

from string import Template
from utils.logger import log_action
from utils.file_handler import process_uploaded_file
from utils.manual_input import collect_manual_input
from utils.analytics import create_dashboard
from utils.openai_utils import generate_text

st.set_page_config(layout="wide")

import streamlit as st
from utils.logger import log_action

def collect_manual_input() -> dict:
    """
    Collects manual data input from the user and processes it with a single button.

    Returns:
        dict: Dictionary containing manually entered data or None if validation fails.
    """
    
    st.header("Business Questionnaire")
    
    business_type = st.text_input(
        "What is your type of business?",
        help="Example: 'I want to open a unisex clothing store in my neighborhood.'",
        key="business_type_input"
    )
    
    has_investment = st.radio("Do you already have a defined investment amount?", ["Yes", "No"])
    investment_amount = None
    if has_investment == "Yes":
        investment_amount = st.text_input("How much is the investment amount?")
    
    store_type = st.selectbox(
        "Will your company be physical, online, or hybrid?", 
        ["", "Physical", "Online", "Hybrid"]
    )
    
    rental_status = st.selectbox(
        "Do you already have a location or will you need to rent/buy a space?",
        ["", "I already have a location", "I'll need to rent", "I'll need to buy", "Not applicable"]
    )
    
    exact_location = st.text_input(
        "What is the desired location of the business?",
        help="Example: 'Goiânia neighborhood, Belo Horizonte.'"
    )
    
    sales_channel = st.multiselect(
        "How do you plan to sell?", 
        ["Physical store", "Online", "Marketplace", "Franchise", "Other"]
    )
    
    competitive_advantages = st.text_area("What are your main competitive advantages?")
    
    has_marketing_strategy = st.radio("Do you have an initial marketing strategy?", ["Yes", "No"])
    marketing_strategy = None
    if has_marketing_strategy == "Yes":
        marketing_strategy = st.text_area("Describe your initial marketing strategy:")
    
    has_experience = st.radio("Do you have any experience selling this product/service?", ["Yes", "No"])
    
    work_structure = st.radio(
        "Will you work alone or hire employees?", 
        ["Alone", "With employees", "Haven't decided yet"]
    )
    
    has_emergency_fund = st.radio(
        "Do you have any money set aside for emergencies in case the business takes time to profit?", 
        ["Yes", "No"]
    )
    
    knows_breakeven = st.radio(
        "Do you know how to calculate how much you need to sell to cover your costs?", 
        ["Yes", "No"]
    )
    
    has_defined_price = st.radio(
        "Have you already defined a price for your product/service?", 
        ["Yes", "No"]
    )
    
    submit_button = st.button("Submit Form")
    
    if submit_button:
        if business_type:
            business_data = {
                "business_type": business_type if business_type else "Not provided",
                "has_investment": has_investment,
                "investment_amount": investment_amount if investment_amount else "Not provided",
                "store_type": store_type if store_type else "Not provided",
                "rental_status": rental_status if rental_status else "Not provided",
                "exact_location": exact_location if exact_location else "Not provided",
                "sales_channel": sales_channel if sales_channel else "Not provided",
                "competitive_advantages": competitive_advantages if competitive_advantages else "Not provided",
                "has_marketing_strategy": has_marketing_strategy,
                "marketing_strategy": marketing_strategy if marketing_strategy else "Not provided",
                "has_experience": has_experience,
                "work_structure": work_structure,
                "has_emergency_fund": has_emergency_fund,
                "knows_breakeven": knows_breakeven,
                "has_defined_price": has_defined_price
            }
            
            log_action("Form submitted successfully!", f"Data: {business_data}")
            return business_data
        else:
            log_action("Manual input failed", "Business type is required")
            st.error("Please fill in at least the business type.")
            return None

def main():
    """Main function for the Streamlit application."""
    st.title("Business and Expense Analysis")

    data = collect_manual_input()

    if not data: 
        st.error("Please fill at leat one fields.")
        log_action("Manual input failed", "Empty form")
        return


    if data is not None:
        file_path = "src/hackaton_roi/prompts/main_prompt.md"
        with open(file_path, "r", encoding="utf-8") as file:
            prompt_template = file.read()
            
            template = Template(prompt_template)
            prompt = template.safe_substitute(data)
            log_action("Prompt created", f"Prompt: {prompt}")

            data = generate_text(prompt)
            
            log_action(
                "Analysis generated", {data},
            )

            create_dashboard(data)
    else:
        st.warning("Please provide valid input data to proceed.")


if __name__ == "__main__":
    log_action("Application started")
    main()
