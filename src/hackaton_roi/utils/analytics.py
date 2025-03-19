import pandas as pd
import plotly.express as px
from utils.logger import log_action

def calculate_expense_percentage(data: dict) -> pd.DataFrame:
    """
    Calculates the percentage of each expense category.

    Args:
        data (dict): Dictionary containing expense values.

    Returns:
        pd.DataFrame: DataFrame with absolute values and percentage of total expenses.
    """
    total_expense = sum(data.values())
    df = pd.DataFrame(list(data.items()), columns=["Category", "Value"])
    df["Percentage"] = ((df["Value"] / total_expense) * 100).round(2)
    df = df.sort_values(by="Percentage", ascending=True)

    log_action("Expense percentage calculated", f"Total Expense: {total_expense}")
    return df

def create_chart(df: pd.DataFrame):
    """
    Generates a horizontal bar chart for expense distribution.

    Args:
        df (pd.DataFrame): DataFrame with category percentages.

    Returns:
        plotly.graph_objects.Figure: Generated chart.
    """
    fig = px.bar(
        df, y="Category", x="Percentage",
        orientation="h", text=df["Percentage"].apply(lambda x: f"{x:.1f}%"),
    )
    
    fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(title="", tickfont=dict(size=16)),
        margin=dict(l=200, r=10, t=30, b=30),
        height=500
    )

    log_action("Expense chart generated", f"Categories: {len(df)}")
    return fig