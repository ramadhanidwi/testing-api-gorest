import os
import requests
from dotenv import load_dotenv
import requests

load_dotenv()  # Memuat variabel dari file .env

api_token = os.getenv("API_TOKEN")

# URL API yang ingin diakses
url = "https://gorest.co.in/public/v2/users/8014332"
headers = {
    "Authorization": f"Bearer {api_token}"
}
partial_update = {
    "status": "inactive"
}

response = requests.patch(url, headers=headers,json=partial_update)
print("Status:", response.status_code)
print("Response:", response.json())
