from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext, Page, expect

# def test_get(user_api_request_context: APIRequestContext):
#     response = user_api_request_context.get(url="https://gorest.co.in/public/v2/users/6139763", headers={"Authorization": "Bearer 76d9a7ab301b6e59339597face88a679c05c7724d61352b3982e827f2eb205d6"})
#     print(response)



# def test_get_user_happy_flow(user_api_request_context: APIRequestContext) -> None:
#     response = user_api_request_context.get(url="https://gorest.co.in/public/v2/users/6139763")
#     assert response.status == 200
#
#     json_response = response.json()
#     print("Get User API Response - Happy Flow:\n{}".format(json_response))
#     assert json_response["data"]["id"] == 6139763


# def test_get_users():
#     with sync_playwright() as p:
#         request_context = p.request.new_context()
#
#         response = request_context.get("https://gorest.co.in/public/v2/users/6129371")  # Replace with your API endpoint
#
#         assert response.status == 200
#         assert response.json() == [{
#         "id": 6129371,
#         "name": "Gaurang Kapoor",
#         "email": "gaurang_kapoor@goldner-torp.test",
#         "gender": "female",
#         "status": "inactive"
#     }]  # Replace with expected data
#
#         request_context.close()
#
# if __name__ == "__main__":
#     test_get_users()