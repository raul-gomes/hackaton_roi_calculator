import time
from hackaton_roi.utils.settings import EnvConfig
from openai import OpenAI
from utils.logger import log_action


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
        api_key=EnvConfig().openai_api_key
    )  # Replace with your API key logic

    retries = 3
    for attempt in range(retries):
        try:
            response = client.responses.create(
                model="gpt-4",
                instructions="Você é um consultor de negócios especializado em análise de ROI.",
                input=prompt,
            )
            log_action("Text generation completed", f"Response: {response.output}")
            return response.output

        except Exception as e:
            log_action(f"Attempt {attempt + 1} failed", str(e))
            time.sleep(2**attempt)  # Exponential backoff

            if attempt == retries - 1:
                raise e  # Re-raise after final attempt
