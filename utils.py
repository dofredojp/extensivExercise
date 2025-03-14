import base64
import requests
import time
import logging
from config import API_AUTH_URL, API_DATA_URL, REQUEST_TIMEOUT, RETRY_DELAY

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def encode_to_base64(input_string):
    """Encodes a string to Base64."""
    return base64.b64encode(input_string.encode("utf-8")).decode("utf-8")

def get_token(encoded_value):
    """Retrieves an authentication token from the API."""
    headers = {"Authorization": f"Basic {encoded_value}"}
    
    try:
        response = requests.get(API_AUTH_URL, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json().get("data")  # Extract token
    except requests.exceptions.RequestException as e:
        logging.error(f"Error getting token: {e}")
        return None

def call_second_api(token):
    """Calls the second API using the provided token."""
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(API_DATA_URL, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        if response.status_code == 401:
            logging.warning("Token expired. Fetching new token...")
            return None  # Indicate expired token

        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling second API: {e}")
        return None
