import time
import logging
from datetime import datetime
from utils import encode_to_base64, get_token, call_second_api
from config import USER_ID, RETRY_DELAY

def main():
    encoded_id = encode_to_base64(USER_ID)
    logging.info(f"Encoded ID: {encoded_id}")

    token = get_token(encoded_id)
    if not token:
        logging.error("Failed to retrieve token. Exiting.")
        return

    logging.info(f"Retrieved Token: {token}")

    try:
        while True:
            response = call_second_api(token)
            if response:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                logging.info(f"[{timestamp}] Second API Response: {response}")
            else:
                token = get_token(encoded_id)
                if not token:
                    logging.error("Failed to retrieve a new token. Exiting.")
                    break
                logging.info(f"New Token Retrieved: {token}")

            logging.info(f"Calling API again in {RETRY_DELAY} seconds... (Press CTRL+C to exit)")
            time.sleep(RETRY_DELAY)
    except KeyboardInterrupt:
        logging.info("Process interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
