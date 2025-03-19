import streamlit as st
from utils.logger import log_action
from utils.file_handler import process_uploaded_file
from utils.manual_input import collect_manual_input
from utils.analytics import calculate_expense_percentage, create_chart

def main():
    """
    Main function for the Streamlit application.
    """
    st.title("Business and Expense Analysis")

    # Step 1: Choose input method
    st.markdown("<h3 style='text-align: center;'>Select Data Input Method</h3>", unsafe_allow_html=True)
    input_choice = st.radio("Choose an input method:", ["Upload Document", "Manual Entry"])
    
    df = None

    if input_choice == "Upload Document":
        uploaded_file = st.file_uploader("Upload your file (CSV, XLSX, XLS)")
        if uploaded_file:
            df = process_uploaded_file(uploaded_file)

    elif input_choice == "Manual Entry":
        df = collect_manual_input()

    if df is not None and not df.empty:
        st.success("Data successfully processed!")

        # Step 2: Expense analysis
        expense_data = {
            "Rent": 1200, "Condominium": 400, "Property Tax": 100,
            "Electricity Bill": 150, "Water Bill": 50, "Internet": 100, "Supermarket": 500
        }
        df_expenses = calculate_expense_percentage(expense_data)

        col1, col2 = st.columns([1, 1.5])

        with col1:
            st.dataframe(df_expenses.style.set_properties(**{'font-size': '16pt'}))

        with col2:
            fig = create_chart(df_expenses)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    log_action("Application started")
    main()