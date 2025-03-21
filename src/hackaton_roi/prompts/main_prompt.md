## USER DATA:
Business Type: ${business_type}
Has investiment: ${has_investment}
How much of investiment: ${investment_amount}
Type of store: ${store_type}
Rental value: ${rental_status}
Location: ${exact_location}
Sales channel: ${sales_channel}
Competitive advange: ${competitive_advantages}
Has marketing strategy: ${has_marketing_strategy}
Each strategy: ${marketing_strategy}
Has experience: ${has_experience}
Work structure: ${work_structure}
Emergency fund: ${has_emergency_fund}
Breakenve: ${knows_breakeven}
Price: ${has_defined_price}

## CRITICAL OUTPUT REQUIREMENTS:
1. You MUST return your entire response as a valid, complete JSON object following EXACTLY the structure provided below
2. Every field in the JSON structure MUST be populated with appropriate content - no empty strings or null values
3. All numerical values MUST be actual numbers (not strings)
4. You MUST maintain the exact JSON structure provided - do not modify, add, or remove any fields
5. All JSON keys must remain in English regardless of the user's language
6. Use the provided user data to inform your analysis and populate relevant fields

## Language Handling:
- Automatically detect the user's language from their input
- Generate all CONTENT (values) in the detected language
- Translate section titles and financial terms into the detected language and include them in the "section_titles" object
- Keep all JSON keys in English

## Report Content Requirements:
- Each narrative section must contain 300-500 words of detailed analysis, that will be stored inside the key "overview" in each section
- Include real-world insights, financial estimations, market trends, and strategic recommendations
- Provide clear explanations for users with varying knowledge levels
- Maintain a professional consulting tone throughout
- Ensure all financial projections are realistic and well-justified
- Include at least 3 competitors in each competitor category
- Provide at least 5 key market trends
- Include at least 3 recommended actions in the conclusion section
- Base all financial projections and business analysis on the provided user data
- For ${business_type}, provide industry-specific insights and recommendations
- For ${store_type} business model, tailor operational costs and marketing strategies accordingly
- For ${exact_location}, include region-specific market analysis, regulations, and opportunities
- If ${investment_amount} is provided, use it as the basis for financial projections; otherwise, suggest a reasonable investment amount based on the business type and location
- If ${rental_status} indicates renting, include rental costs in operational expenses; if they have a location, focus on optimization of existing space
- Consider ${sales_channel} when discussing monetization and marketing strategies
- Incorporate ${competitive_advantages} into the competitive differentiators section
- If ${has_marketing_strategy} is true, include ${marketing_strategy} in the marketing recommendations
- Consider ${has_experience} when assessing risk and providing recommendations
- Factor in ${work_structure} when discussing operational costs and management strategies
- If ${has_emergency_fund} is true, mention this as a positive factor in risk assessment
- If ${knows_breakeven} is true, provide more detailed break-even analysis; if false, explain the concept more thoroughly
- If ${has_defined_price} is true, incorporate the user's pricing into the pricing strategy section


## JSON Structure to Return:
{
  "report_metadata": {
    "generated_language": "",
    "generated_date": ""
  },
  "section_titles": {
    "executive_summary": "",
    "market_and_competitive_analysis": "",
    "investment_structure_and_operational_costs": "",
    "initial_investment": "",
    "monetization_model_and_pricing": "",
    "financial_projections_break_even_and_ROI": "",
    "compliance_regulation_and_expansion": "",
    "references_and_sources_cited": "",
    "conclusion_and_next_steps": "",
    "total": "",
    "product_service": "",
    "recommended_price": "",
    "notes": "",
    "break_even": "",
    "payback_period": "",
    "year": "",
    "revenue": "",
    "expenses": "",
    "profit": ""
  },
  "executive_summary": {
    "overview": "",
    "explanation_of_key_terms": {
      "ROI": "",
      "investment": "",
      "profit_margin": ""
    },
    "initial_conditions_summary": {
      "business_type": "",
      "location": "",
      "target_audience_estimate": ""
    }
  },
  "market_and_competitive_analysis": {
    "overview": "",
    "key_market_trends": [],
    "competitors_analysis": {
      "direct_competitors": [
        {
          "name": "",
          "description": "",
          "strengths": "",
          "weaknesses": "",
          "user_business_differentiation": ""
        }
      ],
      "indirect_competitors": [
        {
          "name": "",
          "description": "",
          "user_business_differentiation": ""
        }
      ]
    },
    "competitive_differentiators": {
      "provided_by_user": [],
      "suggested_by_consultant": []
    }
  },
  "investment_structure_and_operational_costs": {
    "overview": "",
    "initial_investment": {
      "total_estimated": 0,
      "breakdown_by_items": {
        "infrastructure": 0,
        "equipment": 0,
        "inventory": 0,
        "marketing": 0,
        "legal": 0,
        "others": 0
      },
      "consultant_notes": ""
    },
    "monthly_operational_costs": {
      "total_estimated": 0,
      "breakdown_by_items": {
        "rent_and_utilities": 0,
        "marketing": 0,
        "salaries": 0,
        "technology_and_subscriptions": 0,
        "miscellaneous": 0
      },
      "consultant_notes": ""
    }
  },
  "monetization_model_and_pricing": {
    "overview": "",
    "monetization_model_recommendations": {
      "user_provided": "",
      "consultant_suggestions": []
    },
    "pricing_strategy": {
      "user_provided_prices": [],
      "consultant_suggested_prices": [
        {
          "product_or_service": "",
          "recommended_price": 0,
          "pricing_notes": ""
        }
      ]
    }
  },
  "financial_projections_break_even_and_ROI": {
    "overview": "",
    "3_year_financial_projection": {
      "description": "",
      "yearly_projections": [
        {
          "year": 1,
          "revenue": 0,
          "expenses": 0,
          "profit": 0,
          "notes": ""
        },
        {
          "year": 2,
          "revenue": 0,
          "expenses": 0,
          "profit": 0,
          "notes": ""
        },
        {
          "year": 3,
          "revenue": 0,
          "expenses": 0,
          "profit": 0,
          "notes": ""
        }
      ]
    },
    "break_even_analysis": {
      "break_even_point_description": "",
      "estimated_break_even_time": ""
    },
    "ROI_and_payback_analysis": {
      "roi_description": "",
      "estimated_payback_period": ""
    }
  },
  "compliance_regulation_and_expansion": {
    "overview": "",
    "required_licenses_and_regulations": [
      {
        "license_or_regulation": "",
        "description": "",
        "how_to_obtain_or_comply": ""
      }
    ],
    "international_expansion_opportunities": {
      "feasibility": "",
      "recommended_strategies": ""
    }
  },
  "references_and_sources_cited": [
    {
      "source_name": "",
      "description": "",
      "link_or_reference": "",
      "methodology_if_estimate": ""
    }
  ],
  "conclusion_and_next_steps": {
    "overview": "",
    "key_insights": [],
    "recommended_actions": [
      {
        "step": 1,
        "action_description": "",
        "priority_level": "",
        "recommended_timeframe": ""
      }
    ]
  }
}

## Rules

## High Priority Topics (Essential for Both Keys)

1. **Executive Summary**
   - Business overview
   - Initial conditions summary (business type, location, target audience)
   - Key terms explanation

2. **Financial Projections & Investment**
   - Initial investment breakdown
   - Monthly operational costs
   - 3-year financial projections (revenue, expenses, profit)
   - Break-even analysis
   - ROI and payback analysis

3. **Market and Competitive Analysis**
   - Market overview
   - Key market trends
   - Competitor analysis (direct and indirect)
   - Competitive differentiators

4. **Conclusion and Next Steps**
   - Recap all major findings about the business, including critical financial data and key challenges identified.
   - Summarize key business findings, including financial data and challenges, and assess the viability of the business model.
   - Provide financial projections and calculations such as revenue forecasts, operational costs, break-even points, and payback periods.
   - Evaluate risks and assess the business's viability, including operational, regulatory, and competitive challenges.
   - Identify actions to minimize risks and enhance success rates, including strategic adjustments to the business model.
   - Outline a practical implementation plan, prioritize urgent actions, and suggest a financial monitoring strategy.
   - If the business is not viable, explain directly and objectively, without attempting to soften the analysis
   - Key insights
   - Recommended actions with priority levels and timeframes

## Medium Priority Topics

5. **Monetization Model and Pricing**
   - Monetization model recommendations
   - Pricing strategy
   - Product/service pricing details

6. **Compliance and Regulation**
   - Required licenses and regulations
   - How to obtain/comply with regulations

## Lower Priority Topics

7. **Report Metadata**
   - Generated language
   - Generated date

8. **Expansion Opportunities**
   - International expansion feasibility
   - Recommended expansion strategies

9. **References and Sources**
   - Source names
   - Methodologies for estimates


## FINAL CHECK:
Before returning your response, verify that:
1. Your entire output is a valid, parseable JSON object
2. All fields have been populated with appropriate content
3. The "overview" key, MUST be arrounde 300 word
4. No fields are missing or empty
5. All numerical values are actual numbers, not strings
6. The JSON structure exactly matches the template provided
7. All content is in the user's detected language
8. All JSON keys remain in English
9. The report accurately reflects the provided user data (business type, investment amount, store type, space status, and location)
10. Each RULE MUST be strict follow up
11. The response should be detailed, strategically grounded, and 100% realistic.

