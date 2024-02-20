import requests

# DELETE:
# - delete user
# - verify response success status
# - verify user removed

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_delete_by_user_id():
    response = requests.delete(ENDPOINT + "/public/v2/users/6129369", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    assert response.status_code == 204