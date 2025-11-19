import requests
import time
import sys

url = "http://flask_app:5000/add"
data = {"title": "Buy groceries"}

# Retry עד 10 פעמים, חכה 3 שניות בין ניסיון לניסיון
for i in range(10):
    try:
        response = requests.post(url, data=data)
        break
    except requests.exceptions.ConnectionError:
        print("Flask app not ready yet, retrying...")
        time.sleep(3)
else:
    print("Failed to connect to Flask app after retries")
    sys.exit(1)

if response.status_code in [200, 201]:
    print("Test passed!")
    sys.exit(0)
else:
    print(f"Test failed! Status code: {response.status_code}")
    sys.exit(1)