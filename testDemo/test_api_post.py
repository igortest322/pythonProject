from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext, Page, expect

@pytest.fuxture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://gorest.co.in"
    )
    yield request_context
    request_context.dispose()