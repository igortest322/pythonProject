import requests

ENDPOINT = "https://gorest.co.in"
response = requests.get(ENDPOINT)

def test_api_call_endpoint():
    response = requests.get(ENDPOINT, headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
    assert response.status_code == 200
    print(response)