from playwright.sync_api import Playwright, sync_playwright, expect

# Checkboxes:
# 	- navigate to ‘https://the-internet.herokuapp.com/checkboxes’
# 	- read checkboxes states (is selected, is deselected)
# 	- select deselect checkbox
# 	- deselect selected checkbox

def test_checkboxes(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # page.pause()  #for debug in codgen
    # read checkboxes states (is selected, is deselected)
    expect(page.get_by_role("checkbox").nth(1)).to_be_checked()
    expect(page.get_by_role("checkbox").first).not_to_be_checked()
    #select deselect checkbox
    page.get_by_role("checkbox").first.check()
    #deselect selected checkbox
    page.get_by_role("checkbox").first.uncheck()
    expect(page.get_by_role("checkbox").first).not_to_be_checked()
    page.screenshot(path="../Tests01/screenshots/Checkboxes/CHECKBOXES.png")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_checkboxes(playwright)



