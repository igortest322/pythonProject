import requests

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_api_call_endpoint():
    response = requests.get("https://gorest.co.in/public/v2/users", headers={"Authorization": "Bearer 79c36adee0abd73f7986644e389c5d7b44b604e55d9a92a81de376c80b885d16"})
    assert response.status_code == 200
    print(response)
    print(f"Response Data:\n {response.json()}")