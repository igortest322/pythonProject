from playwright.sync_api import Playwright, sync_playwright, expect


#Fuction test_ExpectAddButtonElements checks that the elements are on the page and are visible
def test_ExpectAddButtonElements(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Open Site
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/%22")
    # page.pause()  #for debug in codgen
    # Expecte Add Element Button
    expect(page.get_by_role("button", name="Add Element")).to_be_visible()
    page.screenshot(path="../screenshots/Buttons/screenshot1ExpectAddButtonElements.png")

    # ---------------------
    context.close()
    browser.close()


#Fuction test_ExpecteDeleteButton checks that the Delete Button visible
def test_ExpecteDeleteButton(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Open Site
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/%22")
    # page.pause()  #for debug in codgen
    # Add Element Button
    page.get_by_role("button", name="Add Element").click()
    #Expecte Delete Button
    expect(page.get_by_role("button", name="Delete")).to_be_visible()
    page.screenshot(path="../screenshots/Buttons/screenshot1ExpecteDeleteButton.png")

    # ---------------------
    context.close()
    browser.close()


#Fuction test_ExpecteDeleteButton checks that the Delete Button visible
def test_ExpectDeleteButtoninvisible(playwright: Playwright) -> None:
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
    page.screenshot(path="../screenshots/Buttons/screenshot1ExpectDeleteButtonInvisible.png")

    # ---------------------
    context.close()
    browser.close()


#print("Passed")

# with sync_playwright() as playwright:
#     run(playwright)