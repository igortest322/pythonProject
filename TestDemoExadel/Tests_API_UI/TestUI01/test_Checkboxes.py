from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkboxesvisible(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # page.pause()  #for debug in codgen
    #checkboxes are visible on the webpage
    expect(page.locator("#checkboxes")).to_be_visible()
    page.screenshot(path="../screenshots/Checkboxes/screenshot2CheckboxesVisible.png")

    # ---------------------
    context.close()
    browser.close()


def test_readcheckboxesstates(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # page.pause()  #for debug in codgen
    #read checkboxes states (is selected, is deselected)
    expect(page.get_by_role("checkbox").nth(1)).to_be_checked() and expect(page.get_by_role("checkbox").first).not_to_be_checked()
    page.screenshot(path="../screenshots/Checkboxes/screenshot2ReadCheckboxesStates.png")

    # ---------------------
    context.close()
    browser.close()


def test_selectdeselectcheckbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # page.pause()  #for debug in codgen
    #select deselected checkbox
    page.get_by_role("checkbox").first.check()
    expect(page.get_by_role("checkbox").first).to_be_checked()
    page.screenshot(path="../screenshots/Checkboxes/screenshot2SelectDeselectCheckbox.png")

    # ---------------------
    context.close()
    browser.close()


def test_deselectselectedcheckbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # page.pause()  #for debug in codgen
    #select deselect checkbox
    page.get_by_role("checkbox").first.check()
    #deselect selected checkbox
    page.get_by_role("checkbox").first.uncheck()
    expect(page.get_by_role("checkbox").first).not_to_be_checked()
    page.screenshot(path="../screenshots/Checkboxes/screenshot2DeselectSelectedCheckbox.png")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
