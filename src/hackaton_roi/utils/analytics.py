import streamlit as st
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def create_dashboard(data):
    """
    Create a dynamic dashboard based on the provided JSON data.

    Args:
        data (dict): JSON data containing business analysis information
    """
    # Display report metadata
    st.title("Business Analysis Dashboard")

    # Executive Summary Section
    st.header("Executive Summary")
    if data["executive_summary"]["overview"]:
        st.write(data["executive_summary"]["overview"])

    # Display initial conditions in metrics
    if any(data["executive_summary"]["initial_conditions_summary"].values()):
        col1, col2, col3 = st.columns(3)

        business_type = data["executive_summary"]["initial_conditions_summary"][
            "business_type"
        ]
        if business_type:
            col1.metric("Business Type", business_type)

        location = data["executive_summary"]["initial_conditions_summary"]["location"]
        if location:
            # Use a container with text instead of metric to avoid text cutting
            with col2.container():
                st.markdown("**Location**")
                st.write(location)

        target = data["executive_summary"]["initial_conditions_summary"][
            "target_audience_estimate"
        ]
        if target:
            # Use a container with text instead of metric to avoid text cutting
            with col3.container():
                st.markdown("**Target Audience**")
                st.write(target)

    # Key terms explanation
    if any(data["executive_summary"]["explanation_of_key_terms"].values()):
        with st.expander("Key Financial Terms"):
            for term, definition in data["executive_summary"][
                "explanation_of_key_terms"
            ].items():
                if definition:
                    st.markdown(f"**{term}**: {definition}")

    # Market and Competitive Analysis Section
    st.header("Market and Competitive Analysis")
    if data["market_and_competitive_analysis"]["overview"]:
        st.write(data["market_and_competitive_analysis"]["overview"])

    # Key market trends
    if data["market_and_competitive_analysis"]["key_market_trends"]:
        st.subheader("Key Market Trends")
        for trend in data["market_and_competitive_analysis"]["key_market_trends"]:
            st.markdown(f"- {trend}")

    # Competitors analysis
    direct_competitors = data["market_and_competitive_analysis"][
        "competitors_analysis"
    ]["direct_competitors"]
    indirect_competitors = data["market_and_competitive_analysis"][
        "competitors_analysis"
    ]["indirect_competitors"]

    if any(direct_competitors) or any(indirect_competitors):
        st.subheader("Competitive Landscape")

        # Create tabs for direct and indirect competitors
        tab1, tab2 = st.tabs(["Direct Competitors", "Indirect Competitors"])

        with tab1:
            if any(direct_competitors):
                for comp in direct_competitors:
                    if comp["name"]:
                        with st.expander(comp["name"]):
                            if comp["description"]:
                                st.write(f"**Description**: {comp['description']}")
                            if comp["strengths"]:
                                st.write(f"**Strengths**: {comp['strengths']}")
                            if comp["weaknesses"]:
                                st.write(f"**Weaknesses**: {comp['weaknesses']}")
                            if comp["user_business_differentiation"]:
                                st.write(
                                    f"**Differentiation**: {comp['user_business_differentiation']}"
                                )

        with tab2:
            if any(indirect_competitors):
                for comp in indirect_competitors:
                    if comp["name"]:
                        with st.expander(comp["name"]):
                            if comp["description"]:
                                st.write(f"**Description**: {comp['description']}")
                            if comp["user_business_differentiation"]:
                                st.write(
                                    f"**Differentiation**: {comp['user_business_differentiation']}"
                                )

    # Investment Structure Section
    st.header("Investment Structure and Operational Costs")
    if data["investment_structure_and_operational_costs"]["overview"]:
        st.write(data["investment_structure_and_operational_costs"]["overview"])

    # Initial investment and monthly costs
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Initial Investment")

        # Check if there's data to display
        init_inv_data = data["investment_structure_and_operational_costs"][
            "initial_investment"
        ]["breakdown_by_items"]
        if any(init_inv_data.values()):
            # Create horizontal bar chart instead of pie chart
            fig = px.bar(
                y=list(init_inv_data.keys()),
                x=list(init_inv_data.values()),
                title="Initial Investment Breakdown",
                orientation="h",
                labels={"x": "Amount ($)", "y": "Category"},
                color=list(init_inv_data.keys()),
                color_discrete_sequence=px.colors.qualitative.Bold,
                text_auto=True,
            )
            fig.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)

            # Display total
            total = data["investment_structure_and_operational_costs"][
                "initial_investment"
            ]["total_estimated"]
            if total:
                st.metric("Total Initial Investment", f"${total:,}")

            # Display consultant notes
            notes = data["investment_structure_and_operational_costs"][
                "initial_investment"
            ]["consultant_notes"]
            if notes:
                st.info(f"**Consultant Notes**: {notes}")

    with col2:
        st.subheader("Monthly Operational Costs")

        # Check if there's data to display
        monthly_costs = data["investment_structure_and_operational_costs"][
            "monthly_operational_costs"
        ]["breakdown_by_items"]
        if any(monthly_costs.values()):
            # Create bar chart for monthly costs
            fig = px.bar(
                y=list(monthly_costs.keys()),
                x=list(monthly_costs.values()),
                title="Monthly Operational Costs",
                labels={"x": "Amount ($)", "y": "Category"},
                color=list(monthly_costs.keys()),
                color_discrete_sequence=px.colors.qualitative.Pastel,  # Use a different colorful palette
                text_auto=True,  #
            )
            fig.update_layout(yaxis={"categoryorder": "total ascending"})
            st.plotly_chart(fig, use_container_width=True)

            # Display total
            total = data["investment_structure_and_operational_costs"][
                "monthly_operational_costs"
            ]["total_estimated"]
            if total:
                st.metric("Total Monthly Costs", f"${total:,}")

            # Display consultant notes
            notes = data["investment_structure_and_operational_costs"][
                "monthly_operational_costs"
            ]["consultant_notes"]
            if notes:
                st.info(f"**Consultant Notes**: {notes}")

    # Financial Projections Section
    st.header("Financial Projections, Break-Even, and ROI")
    if data["financial_projections_break_even_and_ROI"]["overview"]:
        st.write(data["financial_projections_break_even_and_ROI"]["overview"])

    # 3-Year Financial Projection
    yearly_data = data["financial_projections_break_even_and_ROI"][
        "3_year_financial_projection"
    ]["yearly_projections"]
    if any(yearly_data):
        st.subheader("3-Year Financial Projection")

        # Create DataFrame for the chart
        df = pd.DataFrame(yearly_data)

        # Create line chart
        fig = go.Figure()

        # Add traces for revenue, expenses, and profit
        if "revenue" in df.columns and df["revenue"].sum() > 0:
            fig.add_trace(
                go.Scatter(
                    x=df["year"],
                    y=df["revenue"],
                    mode="lines+markers",
                    name="Revenue",
                    line=dict(color="green", width=3),
                )
            )

        if "expenses" in df.columns and df["expenses"].sum() > 0:
            fig.add_trace(
                go.Scatter(
                    x=df["year"],
                    y=df["expenses"],
                    mode="lines+markers",
                    name="Expenses",
                    line=dict(color="red", width=3),
                )
            )

        if "profit" in df.columns and df["profit"].sum() != 0:
            fig.add_trace(
                go.Scatter(
                    x=df["year"],
                    y=df["profit"],
                    mode="lines+markers",
                    name="Profit",
                    line=dict(color="blue", width=3),
                )
            )

        fig.update_layout(
            title="3-Year Financial Projection",
            xaxis_title="Year",
            yaxis_title="Amount ($)",
            hovermode="x unified",
        )

        st.plotly_chart(fig, use_container_width=True)

    # Break-even and ROI analysis
    col1, col2 = st.columns(2)

    break_even_time = data["financial_projections_break_even_and_ROI"][
        "break_even_analysis"
    ]["estimated_break_even_time"]
    if break_even_time:
        # Use a container with text instead of metric to avoid text cutting
        with col1.container():
            st.markdown("**Estimated Break-Even Time**")
            st.write(break_even_time)

    payback_period = data["financial_projections_break_even_and_ROI"][
        "ROI_and_payback_analysis"
    ]["estimated_payback_period"]
    if payback_period:
        # Use a container with text instead of metric to avoid text cutting
        with col2.container():
            st.markdown("**Estimated Payback Period**")
            st.write(payback_period)

    # Compliance and Regulation Section
    st.header("Compliance, Regulation, and Expansion")
    if data["compliance_regulation_and_expansion"]["overview"]:
        st.write(data["compliance_regulation_and_expansion"]["overview"])

    # Required licenses and regulations
    licenses = data["compliance_regulation_and_expansion"][
        "required_licenses_and_regulations"
    ]
    if any(licenses):
        st.subheader("Required Licenses and Regulations")

        for license_item in licenses:
            if license_item["license_or_regulation"]:
                with st.expander(license_item["license_or_regulation"]):
                    if license_item["description"]:
                        st.write(f"**Description**: {license_item['description']}")
                    if license_item["how_to_obtain_or_comply"]:
                        st.write(
                            f"**How to Obtain/Comply**: {license_item['how_to_obtain_or_comply']}"
                        )

    # International expansion
    expansion_data = data["compliance_regulation_and_expansion"][
        "international_expansion_opportunities"
    ]
    if expansion_data["feasibility"] or expansion_data["recommended_strategies"]:
        st.subheader("International Expansion Opportunities")

        col1, col2 = st.columns(2)

        if expansion_data["feasibility"]:
            # Use a container with text instead of metric to avoid text cutting
            with col1.container():
                st.markdown("**Feasibility**")
                st.write(expansion_data["feasibility"])

        if expansion_data["recommended_strategies"]:
            # Use a container instead of info to avoid text cutting
            with col2.container():
                st.markdown("**Recommended Strategies**")
                st.write(expansion_data["recommended_strategies"])

    # Conclusion and Next Steps Section
    st.header("Conclusion and Next Steps")
    if data["conclusion_and_next_steps"]["overview"]:
        st.write(data["conclusion_and_next_steps"]["overview"])

    # Key insights
    insights = data["conclusion_and_next_steps"]["key_insights"]
    if insights:
        st.subheader("Key Insights")
        for insight in insights:
            st.markdown(f"- {insight}")

    # Recommended actions
    actions = data["conclusion_and_next_steps"]["recommended_actions"]
    if any(actions):
        st.subheader("Recommended Actions")

        # Create a DataFrame for the actions
        actions_data = []
        for action in actions:
            if action["action_description"]:
                actions_data.append(
                    {
                        "Step": action["step"],
                        "Action": action["action_description"],
                        "Priority": action["priority_level"],
                        "Timeframe": action["recommended_timeframe"],
                    }
                )

        if actions_data:
            df = pd.DataFrame(actions_data)
            # Display the dataframe without the index
            st.dataframe(df, use_container_width=True, hide_index=True)

            # References and Sources Section
    st.header("References and Sources")
    sources = data["references_and_sources_cited"]
    if sources:
        for i, source in enumerate(sources, 1):
            if source["source_name"]:
                with st.expander(f"{i}. {source['source_name']}"):
                    if source["description"]:
                        st.write(f"**Description**: {source['description']}")
                    if source["link_or_reference"]:
                        st.write(f"**Reference**: {source['link_or_reference']}")
                    if source["methodology_if_estimate"]:
                        st.write(
                            f"**Methodology**: {source['methodology_if_estimate']}"
                        )


# Example usage:
# import json
# with open('data.json', 'r') as f:
#     data = json.load(f)
# create_dashboard(data)
