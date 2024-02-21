from playwright.sync_api import Playwright, sync_playwright, expect

# Login Form:
# 	- navigate to ‘https://the-internet.herokuapp.com/login’
# 	- fill credentials (you could find them on the page) and click login
# 	- verify that user logged in, success message appears

def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    # page.pause()  #for debug in codgen
    #check fields+button
    expect(page.get_by_label("Username")).to_be_visible()
    expect(page.get_by_label("Password")).to_be_visible()
    expect(page.get_by_role("button", name=" Login")).to_be_visible()
    # fill username
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    #Fill Passowrd
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    #click login button
    page.get_by_role("button", name=" Login").click()
    #check login status message
    expect(page.get_by_text("You logged into a secure area")).to_be_visible()
    page.screenshot(path="../screenshots/Login/LoginYouLogged.png")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_login(playwright)