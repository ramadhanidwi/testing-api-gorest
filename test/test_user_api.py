import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "https://gorest.co.in/public/v2/users"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

@pytest.fixture(scope="module")
def user_id():
    # CREATE
    user_data = {
        "name": "Prof. Malik Al Hadi",
        "email": "Al_hadimalik@gmail.example",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(BASE_URL, json=user_data, headers=HEADERS)
    assert response.status_code == 201
    user = response.json()
    yield user["id"]
    # DELETE (teardown)
    requests.delete(f"{BASE_URL}/{user['id']}", headers=HEADERS)

def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id

def test_update_user(user_id):
    update_data = {"status": "inactive"}
    response = requests.put(f"{BASE_URL}/{user_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200
    user = response.json()
    assert user["status"] == "inactive"

def test_delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}", headers=HEADERS)
    assert response.status_code == 204

def test_get_user_after_delete(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
    assert response.status_code ==404