import requests
import sys
import time

FLASK_URL = "http://app:5000/add"
DATA = {"title": "Buy groceries"}
MAX_RETRIES = 10
WAIT_SECONDS = 3

def wait_for_flask():
    """Retry connecting to Flask until it's ready."""
    for i in range(MAX_RETRIES):
        try:
            print(f"Trying to connect to Flask ({i+1}/{MAX_RETRIES})...")
            response = requests.post(FLASK_URL, data=DATA, allow_redirects=False)
            print(f"Received response! Status code: {response.status_code}")
            return response
        except requests.exceptions.ConnectionError as e:
            print(f"Flask not ready yet: {e}. Retrying in {WAIT_SECONDS}s...")
            time.sleep(WAIT_SECONDS)
    print("Failed to connect to Flask after retries.")
    sys.exit(1)

def check_response(response):
    """Check if the response indicates success."""
    if response.status_code in [200, 201, 302]:
        print("Test passed!")
        sys.exit(0)
    else:
        print(f"Test failed! Status code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting test: Add Todo item to Flask app")
    response = wait_for_flask()
    check_response(response)
