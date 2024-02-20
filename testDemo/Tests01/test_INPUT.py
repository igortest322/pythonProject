from playwright.sync_api import Playwright, sync_playwright, expect

# Input:
# 	- navigate to ‘https://the-internet.herokuapp.com/inputs’
# 	- fill text field with any number
# 	- verify field is filled as expected

def test_input(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/inputs")
    # page.pause()  #for debug in codgen
    #check spinbutton visible
    expect(page.get_by_role("spinbutton")).to_be_visible()
    #click on field
    page.get_by_role("spinbutton").click()
    #fill the number in field
    page.get_by_role("spinbutton").fill("3")
    #expect filled nubmer
    expect(page.get_by_role("spinbutton")).to_have_value("3")
    page.screenshot(path="../Tests01/screenshots/Input/INPUT.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_input(playwright)