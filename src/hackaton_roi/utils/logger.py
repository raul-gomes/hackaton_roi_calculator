import logging
import uuid
from datetime import datetime

# Configure Logging
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_action(action: str, details: str = "") -> None:
    """
    Logs user actions with a unique identifier.

    Parameters:
    action (str): Description of the action performed.
    details (str): Additional details related to the action.

    Returns:
    None
    """
    action_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"Action ID: {action_id} | Action: {action} | Timestamp: {timestamp} | Details: {details}"
    logging.info(log_entry)
