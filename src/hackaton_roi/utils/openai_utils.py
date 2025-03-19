from hackaton_roi.utils.logger import log_action
from hackaton_roi.utils.settings import EnvConfig
from openai import OpenAI


import json


def generate_text(prompt: str) -> json:
    """
    Sends a request to the OpenAI API to complete the text based on the provided prompt.

    Args:
        prompt (str): The input text prompt for the OpenAI API.

    Returns:
        str: The generated text from the OpenAI API.
    """
    log_action("Text generation started", f"Prompt: {prompt}")
    client = OpenAI(
        api_key=EnvConfig().openai_api_key
        )
    
    response = client.responses.create(
        model="gpt-4",
        instructions="Você é um consultor de negócios especializado em análise de ROI.",
        input=prompt,
    )

    log_action("Text generation completed", f"Response: {response.output}")
    return response.output
