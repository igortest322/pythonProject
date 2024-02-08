from playwright.sync_api import Playwright, sync_playwright, expect


def test_run4(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    # page.pause()
    #check fields+button
    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name=" Login")).to_be_visible()
    #fill username
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    #Fill Passowrd
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    #click login button
    page.get_by_role("button", name=" Login").click()
    #check login status message
    expect(page.get_by_text("You logged into a secure area"))
    page.screenshot(path="./screenshots/screenshot4.png")

    #page.get_by_role("link", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

# from playwright.sync_api import Page, expect
#
# def test_example(page: Page) -> None:
#     page.goto("https://the-internet.herokuapp.com/login")
#     page.get_by_label("Username").click()
#     page.get_by_label("Username").fill("tomsmith")
#     page.get_by_label("Password").click()
#     page.get_by_label("Password").fill("SuperSecretPassword!")
#     page.get_by_role("button", name=" Login").click()
#     page.get_by_text("You logged into a secure area").click()
#     page.get_by_role("link", name="Logout").click()
