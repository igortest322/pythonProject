from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkbuttons(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    # page.pause()  #for debug in codgen
    #check buttons
    expect(page.locator("#file-upload")).to_be_visible() and expect(page.get_by_role("button", name="Upload")).to_be_visible()
    page.screenshot(path="../screenshots/UploadDownload/screenshot5CheckButtons.png")

    # ---------------------
    context.close()
    browser.close()


def test_fileuploaded(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    # page.pause()  #for debug in codgen
    #choosefile
    page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("test1.txt")
    #upload file
    page.get_by_role("button", name="Upload").click()
    #expect file upload message
    expect(page.get_by_role("heading", name="File Uploaded!"))
    page.screenshot(path="../screenshots/UploadDownload/screenshot5FileUploaded.png")

    # ---------------------
    context.close()
    browser.close()


def test_checkuploadedfile (playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://the-internet.herokuapp.com/upload")
    # # page.pause()  #for debug in codgen
    # #choosefile
    # page.locator("#file-upload").click()
    # page.locator("#file-upload").set_input_files("test1.txt")
    # #upload file
    # page.get_by_role("button", name="Upload").click()
    #open download page
    page.goto("https://the-internet.herokuapp.com/download")
    # page.pause()  #for debug in codgen
    #check uploaded file on downloaded page
    expect(page.get_by_text("test1.txt"))
    page.screenshot(path="../screenshots/UploadDownload/screenshot5CheckUploadedFile.png")

    # ---------------------
    context.close()
    browser.close()


def test_downloaduplloadedfille(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://the-internet.herokuapp.com/upload")
    # # page.pause()  #for debug in codgen
    # #choosefile
    # page.locator("#file-upload").click()
    # page.locator("#file-upload").set_input_files("test1.txt")
    # #upload file
    # page.get_by_role("button", name="Upload").click()
    #open download page
    page.goto("https://the-internet.herokuapp.com/download")
    # page.pause()  #for debug in codgen
    #download uplloaded fille
    with page.expect_download() as download_info:
        page.get_by_role("link", name="test1.txt").click()
        assert download_info.value.suggested_filename == "test1.txt"
    download = download_info.value
    # page.screenshot(path="./screenshots/UploadDownload/screenshot5DownloadUplloadedFille.png")
    page.wait_for_timeout(3000)
    print(download)

    # ---------------------
    context.close()
    browser.close()

# with sync_playwright() as playwright:
#     run(playwright)
