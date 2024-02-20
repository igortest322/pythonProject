from playwright.sync_api import Playwright, sync_playwright, expect

# Dropdown:
# 	- navigate to ‘https://the-internet.herokuapp.com/dropdown’
# 	- select any option from dropdown
# 	- verify option is selected
def test_dropdown(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # page.pause()  #for debug in codgen
    #select option
    page.locator("#dropdown").select_option("1")
    #expect option selected
    expect(page.get_by_text("Option 1"))
    # page.locator("#dropdown").select_option("2")
    page.screenshot(path="../Tests01/screenshots/Dropdown/DROPDOWN.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_dropdown(playwright)