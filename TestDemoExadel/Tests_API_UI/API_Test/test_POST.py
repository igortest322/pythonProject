import requests

# POST:
# - create a new user
# - save ID
# - verify response success status

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_post_api_call():
    data = {
        "name":"test212 test1",
        "gender":"male",
        "email":"test.test111122@15ce.com",
        "status":"active"
    }
    response = requests.post("https://gorest.co.in/public/v2/users", headers={"Authorization": "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"}, data=data)
    assert response.status_code == 201
    print(response.json())
    assert response.json()["email"] == "test.test111122@15ce.com"
    print(response.json()["id"])