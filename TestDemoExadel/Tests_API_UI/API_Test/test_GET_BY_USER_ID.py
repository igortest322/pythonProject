import requests

# GET:
# - get user by ID
# - verify response success status
# - verify that response user is expected

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_api_call_get_by_user_id():
    response = requests.get("https://gorest.co.in/public/v2/users/6615213", headers={"Authorization": "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"})
    print(response.json())
    assert response.status_code == 200
    print(response.json()["name"])
    assert response.json()["name"] == "test212 test1"