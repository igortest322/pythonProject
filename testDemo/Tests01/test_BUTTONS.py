from playwright.sync_api import Playwright, sync_playwright, expect

# Buttons:
# 	- navigate to ‘https://the-internet.herokuapp.com/add_remove_elements/’
# 	- click ‘Add Element’ button to add element
# 	- click ‘Remove’ button to remove element

def test_buttons(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Open Site
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/%22")
    # page.pause()  #for debug in codgen
    # Add Element Button
    page.get_by_role("button", name="Add Element").click()
    # Click Delete Button
    page.get_by_role("button", name="Delete").click()
    # Expect DeleteButton invisible
    expect(page.get_by_role("button", name="Delete")).not_to_be_visible()
    page.screenshot(path="../Tests01/screenshots/Buttons/Buttons.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_buttons(playwright)