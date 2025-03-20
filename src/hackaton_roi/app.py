import streamlit as st
import pandas as pd
from string import Template
from utils.logger import log_action
from utils.file_handler import process_uploaded_file
from utils.manual_input import collect_manual_input
from utils.analytics import create_dashboard
from utils.openai_utils import generate_text


def handle_input():
    """Handles user input via file upload or manual entry."""
    st.markdown(
        "<h3 style='text-align: center;'>Select Data Input Method</h3>",
        unsafe_allow_html=True,
    )
    input_choice = st.radio(
        "Choose an input method:", ["Upload Document", "Manual Entry"]
    )
    log_action("Input method selected", f"Method: {input_choice}")
    if input_choice == "Upload Document":
        uploaded_file = st.file_uploader("Upload your file (CSV, XLSX, XLS)")
        if uploaded_file:
            log_action("File uploaded", f"Filename: {uploaded_file.name}")
            return process_uploaded_file(uploaded_file)
    elif input_choice == "Manual Entry":
        return collect_manual_input()
    return None


def generate_analysis(df):
    """Generates analysis based on user-provided data."""
    if df is not None:
        file_path = "src/hackaton_roi/prompts/main_prompt.md"
        with open(file_path, "r", encoding="utf-8") as file:
            prompt_template = file.read()
            prompt = prompt_template.format(DADOS_DO_USUARIO=str(df))
            log_action("Prompt generated", f"Prompt: {prompt}")

        monthly_costs = generate_text(prompt)
        net_profit = generate_text(prompt)
        investment = generate_text(prompt)
        log_action(
            "Analysis generated",
            f"Monthly Costs: {monthly_costs}, Net Profit: {net_profit}, Investment: {investment}",
        )
        create_dashboard(monthly_costs, net_profit, investment)
    else:
        st.error("No data provided. Please upload a file or enter data manually.")


def main():
    """Main function for the Streamlit application."""
    st.title("Business and Expense Analysis")

    # Step 1: Choose input method
    st.markdown(
        "<h3 style='text-align: center;'>Select Data Input Method</h3>",
        unsafe_allow_html=True,
    )
    input_choice = st.radio(
        "Choose an input method:", ["Upload Document", "Manual Entry"]
    )
    df = None

    log_action("Input method selected", f"Method: {input_choice}")

    if input_choice == "Upload Document":
        uploaded_file = st.file_uploader("Upload your file (CSV, XLSX, XLS)")
        if uploaded_file:
            log_action("File uploaded", f"Filename: {uploaded_file.name}")
            df = process_uploaded_file(uploaded_file)
            log_action("File processed", f"Data: {df}")
            if df is None:  # Explicitly check if the dict is empty
                st.error(
                    "The uploaded file is empty or invalid. Please upload a valid file."
                )
                log_action("File processing failed", "Uploaded file is empty")
                return

    elif input_choice == "Manual Entry":
        df = collect_manual_input()
        if not df:  # Check if manual input returned None
            st.error("Please fill at leat one fields.")
            log_action("Manual input failed", "Empty form")
            return

    # Step 2: Generate Analysis (Single Button for Both Input Methods)
    if df is not None:  # Ensure valid data exists
        file_path = "src/hackaton_roi/prompts/main_prompt.md"
        with open(file_path, "r", encoding="utf-8") as file:
            prompt_template = file.read()
            prompt = prompt_template.format(**{"DADOS_DO_USUARIO": str(df)})
            log_action("Prompt generated", f"Prompt: {prompt}")

        if st.button("Generate Analysis"):
            monthly_costs = generate_text(prompt)
            net_profit = generate_text(prompt)
            investment = generate_text(prompt)
            log_action(
                "Analysis generated",
                f"Monthly Costs: {monthly_costs}, Net Profit: {net_profit}, Investment: {investment}",
            )
            create_dashboard(monthly_costs, net_profit, investment)
    else:
        st.warning("Please provide valid input data to proceed.")


if __name__ == "__main__":
    log_action("Application started")
    main()
