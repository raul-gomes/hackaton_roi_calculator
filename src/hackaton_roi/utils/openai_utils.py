import time

#from hackaton_roi.settings import EnvConfig
from openai import OpenAI, api_key
from utils.logger import log_action
import re
import json

import os
from dotenv import load_dotenv

load_dotenv()

def generate_text(prompt: str) -> str:
    """
    Sends a request to the OpenAI API to complete the text based on the provided prompt.

    Args:
        prompt (str): The input text prompt for the OpenAI API.

    Returns:
        str: The generated text from the OpenAI API.
    """
    log_action("Text generation started", f"Prompt: {prompt}")
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
        # api_key=EnvConfig().openai_api_key
    )   # Replace with your API key logic

    retries = 3
    for attempt in range(retries):
        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                instructions="You are an elite business consultant with expertise in feasibility analysis, ROI calculation, financial strategy, and business growth. Your task is to generate a comprehensive business report in JSON format based on the user input provided.",
                input=prompt,
            )
            log_action(
                "Text generation completed",
                f"Response: {response.output[0].content[0].text}",
            )
            json_pattern = r"```json\n(.*?)\n```"
            json_match = re.search(
                json_pattern, str(response.output[0].content[0].text), re.DOTALL
            )
            json_string = json_match.group(1)
            print(json_string)
            data_dict = json.loads(json_string)

            log_action("JSON data extracted", f"Data: {data_dict}")
            # Converter a string JSON para um dicionário Python

            return data_dict

        except Exception as e:
            log_action(f"Attempt {attempt + 1} failed", str(e))
            time.sleep(2**attempt)  # Exponential backoff

            if attempt == retries - 1:
                raise e  # Re-raise after final attempt
