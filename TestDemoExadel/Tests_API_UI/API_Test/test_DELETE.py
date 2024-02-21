import requests

# DELETE:
# - delete user
# - verify response success status
# - verify user removed

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_delete_by_user_id():
    response = requests.delete("https://gorest.co.in/public/v2/users/6615213", headers={"Authorization": "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"})
    assert response.status_code == 204