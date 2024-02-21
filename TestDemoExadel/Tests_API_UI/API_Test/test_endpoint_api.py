import requests
import random
import string
import json

ENDPOINT = "https://gorest.co.in/public/v2"
API_KEY = "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"
response = requests.get(ENDPOINT)
# Generate random data
random_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
random_email = f"{random_name}@{random_name}.com"
random_gender = random.choice(["male", "female"])
random_status = random.choice(["active", "inactive"])

def test_api_call_endpoint():
    response = requests.get(ENDPOINT + "/users", headers={"Authorization": API_KEY})
    # Assert status code
    assert response.status_code == 200, f"Error: Unexpected status code {response.status_code}"
    # Print response
    print(response)
    # Print response data
    print(f"Response Data:\n {response.json()}")

def test_post_api_call():
    data = {
        "name": random_name,
        "gender": random_gender,
        "email": random_email,
        "status": random_status
    }
    # Print generated data
    print("Posted data:", data)
    # POST request
    response = requests.post("https://gorest.co.in/public/v2/users", headers={"Authorization": API_KEY},  data=data)
    # Assert status code
    assert response.status_code == 201
    # Print response data
    print("Response data:", response.json())
    created_user_data = response.json()
    # created_user_name = response.json()["name"]
    # created_user_gender = response.json()["gender"]
    # created_user_email = response.json()["email"]
    # created_user_status = response.json()["status"]
    # created_user_id = response.json()["id"]
    # print(f"Created user ID: {created_user_id}")
    # print(f"Created user name: {created_user_name}")
    # print(f"Created user gender: {created_user_gender}")
    # print(f"Created user email: {created_user_email}")
    # print(f"Created user status: {created_user_status}")
    # Assert posted data
    assert response.json()["name"] == random_name
    assert response.json()["email"] == random_email
    assert response.json()["gender"] == random_gender
    assert response.json()["status"] == random_status
    # Prepare dictionary for saving
    data_to_save = {
        "created_user_name": created_user_data["name"],
        "created_user_gender": created_user_data["gender"],
        "created_user_email": created_user_data["email"],
        "created_user_status": created_user_data["status"],
        "created_user_id": created_user_data["id"]
    }
    # Save user data to JSON for later use for api_call_get_by_user_id
    with open("created_user_data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)

def test_api_call_get_by_user_id():
    # Read saved user ID
    with open("created_user_data.json", "r") as f:
        user_data = json.load(f)
        user_id = user_data["created_user_id"]

    response = requests.get(f"https://gorest.co.in/public/v2/users/{user_id}", headers={"Authorization": API_KEY})
    assert response.status_code == 200
    print("GET response data:",response.json())
    # Assert retrieved user ID matches saved ID
    assert response.json()["id"] == user_id, "Retrieved user ID doesn't match saved ID"
    print(response.json()["id"])

def test_patch_api_call():
    data_updated = {
        "name": random_name,
        "gender": random_gender,
        "email": random_email,
        "status": random_status
    }

    with open("created_user_data.json", "r") as f:
        user_data = json.load(f)
        user_id = user_data["created_user_id"]

    response = requests.patch(f"https://gorest.co.in/public/v2/users/{user_id}", headers={"Authorization": API_KEY}, data=data_updated)
    assert response.status_code == 200
    print(response.json()["id"])
    assert response.json()["id"] == user_id, "Retrieved user ID doesn't match saved ID"
    print("PATCH response data:", response.json())

def test_delete_by_user_id():
    with open("created_user_data.json", "r") as f:
        user_data = json.load(f)
        user_id = user_data["created_user_id"]

    response = requests.delete(f"https://gorest.co.in/public/v2/users/{user_id}", headers={"Authorization": API_KEY})
    assert response.status_code == 204


