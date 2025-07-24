import os
import requests
from dotenv import load_dotenv
import requests

load_dotenv()  # Memuat variabel dari file .env

api_token = os.getenv("API_TOKEN")

# URL API yang ingin diakses
url = "https://gorest.co.in/public/v2/users"
headers = {
    "Authorization": f"Bearer {api_token}"
}

# Data pengguna yang akan dibuat
user_data =   {
    "name": "Ramadhani Nugroho",
    "email": "ramadhani_nugroho@gmail.example",
    "gender": "male",
    "status": "active"
  }

response = requests.post(url, json=user_data, headers=headers)

print("Status:", response.status_code)
print("Response:", response.json())

def update_env_id(new_id, env_path=".env"):
    lines = []
    with open(env_path, "r") as f:
        for line in f:
            if line.startswith("ID="):
                lines.append(f"ID={new_id}\n")
            else:
                lines.append(line)
    with open(env_path, "w") as f:
        f.writelines(lines)

update_env_id(response.json().get("id", ""))
