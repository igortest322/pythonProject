from playwright.sync_api import Playwright, sync_playwright, expect

def test_run3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # page.pause()
    #check dropdown visible
    # expect(page.locator("#dropdown")).to_be_visible()
    #select any option
    page.locator("#dropdown").select_option("1")
    #expect option selected
    expect(page.get_by_text("Option 1"))
    page.screenshot(path="./screenshots/screenshot3.png")

    # page.locator("#dropdown").select_option("2")

    # ---------------------
    context.close()
    browser.close()


#121 with sync_playwright() as playwright:
#     run(playwright)