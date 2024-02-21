import requests

# PATCH:
# - replace or update user
# - verify response success status
# - verify user is updated by sending GET request

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_patch_api_call():
    data = {
        "name":"Allasani1 Peddana1",
        "email":"allasani1.peddana1@15ce.com",
        "status":"active"
    }
    response = requests.patch(ENDPOINT + "/public/v2/users/6139877", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"}, data=data)
    assert response.status_code == 200
    print(response.json())
    assert response.json()["email"] == "allasani1.peddana1@15ce.com"
    print(response.json()["id"])