from playwright.sync_api import Playwright, sync_playwright, expect

def test_run1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Open Site
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/%22")
    # page.pause()
    # Expecte Add Element Button
    expect(page.get_by_role("button", name="Add Element")).to_be_visible()
    page.get_by_role("button", name="Add Element").click()

    #Expecte Delete Button
    expect(page.get_by_role("button", name="Delete"))
    page.get_by_role("button", name="Delete").click()

    # Expect DeleteButton invisible
    expect(page.get_by_role("button", name="Delete")).not_to_be_visible()


    # ---------------------
    context.close()
    browser.close()


#print("Passed")

# with sync_playwright() as playwright:
#     run(playwright)