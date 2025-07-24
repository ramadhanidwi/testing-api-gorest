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

response = requests.delete(url,headers=headers)
print("Status:", response.status_code)
