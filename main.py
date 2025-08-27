import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    print("API key not found.")
else:
    print(f'Your API key is: {api_key}')
     # Simulated request
    response = requests.get("https://httpbin.org/get", headers={"Authorization": f"Bearer {api_key}"})
    print("Status code:", response.status_code)
    print("Response:", response.json())
    # print("This is cool.")
    # print("wow")