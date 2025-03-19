import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Dict, List, Tuple


# New color palette
primary_color: str = "#007bff"  # Vibrant blue for main elements
secondary_color: str = "#ffc107"  # Yellow for highlight
success_color: str = "#28a745"  # Green for success (profit)
danger_color: str = "#dc3545"  # Red for losses (costs)
background_color: str = "#f8f9fa"  # Light background
text_color: str = "#343a40"  # Dark text


def create_dashboard(monthly_costs, net_profit, investment) -> None:
    """
    Creates a business plan dashboard with financial data visualizations.

    Args:
        df (pd.DataFrame): The main DataFrame (not used in this example).
    """

    monthly_costs: Dict[str, Dict[str, int]] = {
        "title": "Adjusted Monthly Costs",
        "data": {
            "rent": 1200,
            "condominium": 400,
            "property tax": 100,
            "electricity bill": 150,
            "water bill": 50,
            "internet": 100,
            "supermarket": 500,
        },
    }

    net_profit: Dict[str, List[Dict[str, int]]] = {
        "title": "Estimated Net Profit",
        "data": [
            {
                "period": "Month 1",
                "Gross Revenue": 50000,
                "Fixed Costs": 25000,
                "Net Profit": 25000,
            },
            {
                "period": "Month 2",
                "Gross Revenue": 55000,
                "Fixed Costs": 25000,
                "Net Profit": 30000,
            },
            {
                "period": "Month 3",
                "Gross Revenue": 60000,
                "Fixed Costs": 25000,
                "Net Profit": 35000,
            },
            {
                "period": "Month 4",
                "Gross Revenue": 65000,
                "Fixed Costs": 25000,
                "Net Profit": 40000,
            },
            {
                "period": "Month 5",
                "Gross Revenue": 70000,
                "Fixed Costs": 25000,
                "Net Profit": 45000,
            },
        ],
    }

    investment: Dict[str, List[Dict[str, float]]] = {
        "title": "Investment Distribution",
        "data": [
            {
                "Category": "Initial Stock",
                "Value": 35000,
                "Fixed Costs": 25000,
                "Percentage": 29.2,
            },
            {
                "Category": "Rent",
                "Value": 6000,
                "Fixed Costs": 25000,
                "Percentage": 5,
            },
            {
                "Category": "Renovation and Furniture",
                "Value": 10000,
                "Fixed Costs": 25000,
                "Percentage": 8.3,
            },
            {
                "Category": "Equipment",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.2,
            },
            {
                "Category": "Initial Marketing",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.2,
            },
            {
                "Category": "Company Registration",
                "Value": 6500,
                "Fixed Costs": 25000,
                "Percentage": 5.4,
            },
            {
                "Category": "Working Capital",
                "Value": 47500,
                "Fixed Costs": 25000,
                "Percentage": 39.6,
            },
            {
                "Category": "Reserve for Expansion and Emergencies",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.1,
            },
        ],
    }

    # Creating DataFrames
    df_costs: pd.DataFrame = pd.DataFrame(
        list(monthly_costs["data"].items()), columns=["Category", "Value"]
    )
    df_profit: pd.DataFrame = pd.DataFrame(net_profit["data"])
    df_investment: pd.DataFrame = pd.DataFrame(investment["data"])

    # Calculating total investment
    total_investment: float = df_investment["Value"].sum()

    st.markdown(
        f"""
        <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
        .stMetric {{
            background-color: rgba(0,0,0,0); /* Transparent background */
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            color: {text_color}; /* Text color */
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Business Plan Dashboard")

    # Total Investment (Title and Value Side by Side)
    col1, col2 = st.columns(2)

    with col1:
        st.header("Total Investment")

    with col2:
        st.header(f"R$ {total_investment:,.2f}")

    # Monthly Costs
    st.header(monthly_costs["title"])
    st.bar_chart(df_costs.set_index("Category"), color=danger_color)  # Costs in red

    st.write(
        """
    This business plan was developed to... [Add information about the business plan here].
    """
    )

    # Estimated Net Profit
    st.header(net_profit["title"])
    fig_profit: go.Figure = go.Figure()

    # Line for Gross Revenue
    fig_profit.add_trace(
        go.Scatter(
            x=df_profit["period"],
            y=df_profit["Gross Revenue"],
            mode="lines+markers",  # Adds markers
            name="Gross Revenue",
            marker=dict(color=primary_color),
            hovertemplate="Period: %{x}<br>Revenue: R$ %{y}<extra></extra>",  # Adds hover info
        )
    )

    # Line for Fixed Costs
    fig_profit.add_trace(
        go.Scatter(
            x=df_profit["period"],
            y=df_profit["Fixed Costs"],
            mode="lines+markers",  # Adds markers
            name="Fixed Costs",
            marker=dict(color=danger_color),
            hovertemplate="Period: %{x}<br>Costs: R$ %{y}<extra></extra>",  # Adds hover info
        )
    )

    # Line for Net Profit
    fig_profit.add_trace(
        go.Scatter(
            x=df_profit["period"],
            y=df_profit["Net Profit"],
            mode="lines+markers",  # Adds markers
            name="Net Profit",
            marker=dict(color=success_color),
            hovertemplate="Period: %{x}<br>Profit: R$ %{y}<extra></extra>",  # Adds hover info
        )
    )

    fig_profit.update_layout(
        xaxis_title="",
        yaxis_title="Value (R$)",
        yaxis=dict(rangemode="tozero"),  # Y-axis starts from zero
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,  # Places legend at the bottom
            xanchor="center",
            x=0.5,
        ),
    )

    st.plotly_chart(fig_profit)
    st.dataframe(df_profit)

    st.write(
        """
    This business plan was developed to... [Add information about the business plan""")
    
    investment: Dict[str, List[Dict[str, float]]] = {
        "title": "Investment Distribution",
        "data": [
            {
                "Category": "Initial Stock",
                "Value": 35000,
                "Fixed Costs": 25000,
                "Percentage": 29.2,
            },
            {
                "Category": "Rent",
                "Value": 6000,
                "Fixed Costs": 25000,
                "Percentage": 5,
            },
            {
                "Category": "Renovation and Furniture",
                "Value": 10000,
                "Fixed Costs": 25000,
                "Percentage": 8.3,
            },
            {
                "Category": "Equipment",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.2,
            },
            {
                "Category": "Initial Marketing",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.2,
            },
            {
                "Category": "Company Registration",
                "Value": 6500,
                "Fixed Costs": 25000,
                "Percentage": 5.4,
            },
            {
                "Category": "Working Capital",
                "Value": 47500,
                "Fixed Costs": 25000,
                "Percentage": 39.6,
            },
            {
                "Category": "Reserve for Expansion and Emergencies",
                "Value": 5000,
                "Fixed Costs": 25000,
                "Percentage": 4.1,
            },
        ],
    }

    # Creating DataFrames
    df_investment: pd.DataFrame = pd.DataFrame(investment["data"])

    st.markdown(
        f"""
        <style>
        body {{
            background-color: {background_color};
            color: {text_color};
        }}
        .stMetric {{
            background-color: rgba(0,0,0,0); /* Transparent background */
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            color: {text_color}; /* Text color */
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Investment Distribution (Horizontal Bar Chart)
    st.header(investment["title"])

    df_investment = df_investment.sort_values(by="Value", ascending=True)

    fig_investment = go.Figure(
        go.Bar(
            x=df_investment["Value"],
            y=df_investment["Category"],
            orientation="h",
            text=[f'{p:.1f}%' for p in df_investment["Percentage"]],
            textposition="inside",
            marker_color=primary_color,
        )
    )

    fig_investment.update_layout(
        xaxis_title="",
        yaxis_title="",
        xaxis_visible=False,
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)",  # Transparent paper background
    )

    st.plotly_chart(fig_investment)
    st.dataframe(
        df_investment[["Category", "Value", "Fixed Costs"]].sort_values(
            by="Value", ascending=True
        )
    )

    st.write(
        """
    This business plan was developed to... [Add information about the business plan here].
    """
    )