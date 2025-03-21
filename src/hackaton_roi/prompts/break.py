sections = [
    "executive_summary",
    "market_and_competitive_analysis",
    "investment_structure_and_operational_costs",
    "monetization_model_and_pricing",
    "financial_projections_break_even_and_ROI",
    "compliance_regulation_and_expansion",
    "references_and_sources_cited",
    "conclusion_and_next_steps"
]

generated_report = {}

for section in sections:
    prompt = f"""
    Generate the section {section} for the business report. 
    Ensure a detailed response with 300-500 words. 
    Use structured insights, financial analysis, and competitive research. 
    The business is {tipo_negocio}, located in {localizacao}. 
    Consider an investment of {investimento_inicial} and a target audience of {publico_alvo}. 
    """
    
    response = call_openai_api(prompt)  # Chamada para o GPT-4o-mini
    generated_report[section] = response["text"]

# Junta as seções no JSON final
final_report_json = json.dumps(generated_report, indent=4)

for section in sections:
    previous_sections = "\n".join(
        [f"{key}: {generated_report[key]}" for key in generated_report.keys()]
    )

    prompt = f"""
    Continue generating the business report.  
    Here is what has been generated so far:\n{previous_sections}  
    Now, generate the next section: {section}.  
    Ensure consistency with previous sections, and provide at least 300-500 words.  
    """

    response = call_openai_api(prompt)
    generated_report[section] = response["text"]
