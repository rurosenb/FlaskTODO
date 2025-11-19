import requests
import sys

def test_add_item():
    url = "http://flask_app:5000/add"  # זה ה-service name מ-Docker Compose
    data = {"title": "Buy groceries"}

    try:
        response = requests.post(url, data=data)
    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    if response.status_code in [200, 201]:
        print(f"Success! Status code: {response.status_code}")
        sys.exit(0)
    else:
        print(f"Failed! Status code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    test_add_item()