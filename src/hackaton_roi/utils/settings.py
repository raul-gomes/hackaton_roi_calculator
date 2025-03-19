import os
from dotenv import load_dotenv
from hackaton_roi.utils.logger import log_action

class EnvConfig:
    """
    Class to load and store environment variables.
    """

    def __init__(self, dotenv_path: str = ".env"):
        """
        Initializes the EnvConfig class and loads environment variables.

        Args:
            dotenv_path (str): Path to the .env file.
        """
        log_action("Environment configuration started")
        load_dotenv(dotenv_path=dotenv_path)
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        log_action("Environment configuration completed")


    def validate(self) -> None:
        """
        Validates if the required environment variables are set.
        """
        if not self.openai_api_key:
            raise ValueError("The environment variable OPENAI_API_KEY is not set.")