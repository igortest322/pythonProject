from playwright.sync_api import Page, expect


def test_example1(page: Page) -> None:

    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    # Expecte Add Element Button
    expect(page.get_by_role("button", name="Add Element")).to_be_visible()
    page.get_by_role("button", name="Add Element").click()
    #Expecte Delete Button
    expect(page.get_by_role("button", name="Delete"))
    page.get_by_role("button", name="Delete").click()
    #Expect DeleteButton invisible
    expect(page.get_by_role("button", name="Delete")).not_to_be_visible()