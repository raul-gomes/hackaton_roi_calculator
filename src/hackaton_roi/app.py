from hackaton_roi.utils.analytics import create_dashboard
from hackaton_roi.utils.file_handler import process_uploaded_file
from hackaton_roi.utils.manual_input import collect_manual_input
from hackaton_roi.utils.openai_utils import generate_text
import streamlit as st
import pandas as pd

from string import Template

from utils.logger import log_action

def main():
    """
    Main function for the Streamlit application.
    """
    st.title("Business and Expense Analysis")

    # Step 1: Choose input method
    st.markdown("<h3 style='text-align: center;'>Select Data Input Method</h3>", unsafe_allow_html=True)
    input_choice = st.radio("Choose an input method:", ["Upload Document", "Manual Entry"])
    
    df = None
    log_action("Input method selected", f"Method: {input_choice}")
    if input_choice == "Upload Document":
        uploaded_file = st.file_uploader("Upload your file (CSV, XLSX, XLS)")
        log_action("File uploaded", f"Filename: {uploaded_file}")
        if uploaded_file:
            df = process_uploaded_file(uploaded_file)
            log_action("File processed", f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    elif input_choice == "Manual Entry":
        df = collect_manual_input()
        log_action("Manual input collected", f"Data: {df}")


    if st.button("Generate Analysis"):
        
        file_path = "src/hackaton_roi/prompts/main_prompt.md"
        with open(file_path, "r", encoding='utf-8') as file:
            prompt = file.read()
            prompt = Template(prompt).safe_substitute(df)
        
        log_action("Prompt generated", f"Prompt: {prompt}")
        monthly_costs = generate_text(prompt)
        net_profit = generate_text(prompt)
        investment = generate_text(prompt)
        
        log_action("Analysis generated", f"Monthly Costs: {monthly_costs}, Net Profit: {net_profit}, Investment: {investment}")
        create_dashboard(monthly_costs, net_profit, investment)

if __name__ == "__main__":
    log_action("Application started")
    main()