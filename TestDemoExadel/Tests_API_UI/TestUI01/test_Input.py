from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkspinbuttonvisible(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/inputs")
    # page.pause()  #for debug in codgen
    #check spinbutton visible
    expect(page.get_by_role("spinbutton")).to_be_visible()
    page.screenshot(path="../screenshots/Input/screenshot4CheckSpinButtonVisible.png")

    # ---------------------
    context.close()
    browser.close()


def test_checkfillednubmer(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/inputs")
    # page.pause()  #for debug in codgen
    #click on field
    page.get_by_role("spinbutton").click()
    #fill the number in field
    page.get_by_role("spinbutton").fill("3")
    #expect filled nubmer
    expect(page.get_by_role("spinbutton")).to_have_value("3")
    page.screenshot(path="../screenshots/Input/screenshot4CheckFilledNubmer.png")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)