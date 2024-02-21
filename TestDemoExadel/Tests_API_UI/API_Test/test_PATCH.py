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
        'gender': 'female',
        "email":"allasani1.peddana1@15ce.com",
        "status":"active"
    }
    response = requests.patch("https://gorest.co.in/public/v2/users/6615213", headers={"Authorization": "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"}, data=data)
    assert response.status_code == 200
    print(response.json())
    assert response.json()["email"] == "allasani1.peddana1@15ce.com"
    print(response.json()["id"])