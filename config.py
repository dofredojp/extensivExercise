import os
from dotenv import load_dotenv

load_dotenv()

API_AUTH_URL = os.getenv("API_AUTH_URL")
API_DATA_URL = os.getenv("API_DATA_URL")
USER_ID = os.getenv("USER_ID")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT")) 
RETRY_DELAY = int(os.getenv("RETRY_DELAY")) 
