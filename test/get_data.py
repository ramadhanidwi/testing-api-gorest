import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Memuat variabel dari file .env

api_token = os.getenv("API_TOKEN")
# id = os.getenv("ID")
# id_int = int(id)

# URL API yang ingin diakses
url = "https://gorest.co.in/public/v2/users/8014332"
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Kirim permintaan GET
response = requests.get(url,headers=headers)

# Cek status dan tampilkan data
if response.status_code == 200:
    user_data = response.json()
    print(type(user_data))
    print("ID:", user_data["id"])
    print("Nama:", user_data["name"])
    print("Email:", user_data["email"])
    print("Gender:", user_data["gender"])
    print("Status:", user_data["status"])
else:
    print("Gagal mengakses API:", response.status_code)
