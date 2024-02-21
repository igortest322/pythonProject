import requests

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_api_call_endpoint():
    response = requests.get(ENDPOINT, headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    assert response.status_code == 200
    print(response)

def test_api_call_get_by_user_id():
    response = requests.get(ENDPOINT + "/public/v2/users/6129375", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    print(response.json())
    assert response.status_code == 200
    print(response.json()["name"])
    assert response.json()["name"] == "Gov. Vaishno Malik"

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

def test_delete_by_user_id():
    response = requests.delete(ENDPOINT + "/public/v2/users/6129369", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    assert response.status_code == 204





