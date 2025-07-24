import os
import requests
from dotenv import load_dotenv
import requests

load_dotenv()  # Memuat variabel dari file .env

api_token = os.getenv("API_TOKEN")

# URL API yang ingin diakses
url = "https://gorest.co.in/public/v2/users/8021535"
headers = {
    "Authorization": f"Bearer {api_token}"
}
partial_update = {
    "name": "Ramadhani Nugroho Updated",
    "status": "inactive"
}

response = requests.patch(url, headers=headers,json=partial_update)
print("Status:", response.status_code)
print("Response:", response.json())
