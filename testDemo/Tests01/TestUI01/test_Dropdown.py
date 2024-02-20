from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkdropdownvisible(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # page.pause()  #for debug in codgen
    #check dropdown visible
    expect(page.locator("#dropdown")).to_be_visible()
    page.screenshot(path="../screenshots/Dropdown/screenshot3CheckDropdownVisible.png")

    # ---------------------
    context.close()
    browser.close()


def test_optionselected(playwright: Playwright) -> None:
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
    page.screenshot(path="../screenshots/Dropdown/screenshot3OptionSelected.png")

    # ---------------------
    context.close()
    browser.close()


#121 with sync_playwright() as playwright:
#     run(playwright)