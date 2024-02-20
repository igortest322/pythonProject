from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkfieldsandbutton(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    # page.pause()  #for debug in codgen
    #check fields+button
    expect(page.get_by_label("Username")).to_be_visible() and expect(page.get_by_label("Password")).to_be_visible() and expect(page.get_by_role("button", name=" Login")).to_be_visible()
    page.screenshot(path="../screenshots/Login/screenshot4CheckFieldsAndDutton.png")

    # ---------------------
    context.close()
    browser.close()


def test_loginstatus(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    # page.pause()  #for debug in codgen
    #fill username
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    #Fill Passowrd
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    #click login button
    page.get_by_role("button", name=" Login").click()
    #check login status message
    expect(page.get_by_text("You logged into a secure area")).to_be_visible()
    page.screenshot(path="../screenshots/Login/screenshot4LoginStatus.png")

    # ---------------------
    context.close()
    browser.close()

def test_logoutbuttoncheck(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    #page.pause()  #for debug in codgen
    #fill username
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    #Fill Passowrd
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    #click login button
    page.get_by_role("button", name=" Login").click()
    #check logout button
    expect(page.get_by_role("link", name="Logout")).to_be_visible()
    page.screenshot(path="../screenshots/Login/screenshot4LogoutButtonCheck.png")

    # ---------------------
    context.close()
    browser.close()


def test_logoutstatus(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    #page.pause()  #for debug in codgen
    #fill username
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("tomsmith")
    #Fill Passowrd
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("SuperSecretPassword!")
    #click login button
    page.get_by_role("button", name=" Login").click()
    #click logout button
    page.get_by_role("link", name="Logout").click()
    #check logout status
    expect(page.get_by_text("You logged out of the secure")).to_be_visible()
    page.screenshot(path="../screenshots/Login/screenshot4LogOutStatus.png")

    # ---------------------
    context.close()
    browser.close()
