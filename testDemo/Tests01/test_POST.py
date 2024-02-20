import requests

# POST:
# - create a new user
# - save ID
# - verify response success status

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_post_api_call():
    data = {
        "name":"test21 test1",
        "gender":"male",
        "email":"test.test11112@15ce.com",
        "status":"active"
    }
    response = requests.post(ENDPOINT + "/public/v2/users", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"}, data=data)
    assert response.status_code == 201
    print(response.json())
    assert response.json()["email"] == "test.test11112@15ce.com"
    print(response.json()["id"])