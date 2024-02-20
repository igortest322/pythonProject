import requests

# GET:
# - get user by ID
# - verify response success status
# - verify that response user is expected

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_api_call_get_by_user_id():
    response = requests.get(ENDPOINT + "/public/v2/users/6129375", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    print(response.json())
    assert response.status_code == 200
    print(response.json()["name"])
    assert response.json()["name"] == "Gov. Vaishno Malik"