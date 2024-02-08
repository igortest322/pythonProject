from playwright.sync_api import Playwright, sync_playwright, expect


def test_run5(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    # page.pause()
    #check buttons
    expect(page.locator("#file-upload")).to_be_visible()
    expect(page.get_by_role("button", name="Upload")).to_be_visible()
    #choosefile
    page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("test1.txt")
    #upload file
    page.get_by_role("button", name="Upload").click()
    #expect file upload message
    expect(page.get_by_role("heading", name="File Uploaded!"))

    #open download page
    page.goto("https://the-internet.herokuapp.com/download")
    expect(page.get_by_text("test1.txt"))
    #download uplloaded fille
    with page.expect_download() as download_info:
        page.get_by_role("link", name="test1.txt").click()
    download = download_info.value
    page.wait_for_timeout(3000)
    page.screenshot(path="./screenshots/screenshot5.png")
    print(download)



    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
#
# from playwright.sync_api import Page, expect
#
#
# def test_example(page: Page) -> None:
#     page.goto("https://the-internet.herokuapp.com/upload")
#     page.locator("#file-upload").click()
#     page.locator("#file-upload").set_input_files("test1.txt")
#     page.get_by_role("button", name="Upload").click()
#     page.get_by_role("heading", name="File Uploaded!").click()
#     page.goto("https://the-internet.herokuapp.com/download")
#     with page.expect_download() as download_info:
#         page.get_by_role("link", name="test1.txt").click()
#     download = download_info.value