import requests

try:
    url = input("Enter the URL to make a request: ")
    response = requests.get(url)
    print("Request successful!")
    print("Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("An error occurred while making the request:", e)
except requests.exceptions.ConnectionError as e:
    print("Connection Error:", e)
except requests.exceptions.Timeout as e:
    print("Request timed out:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution completed.")