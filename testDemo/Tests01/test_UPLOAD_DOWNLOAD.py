from playwright.sync_api import Playwright, sync_playwright, expect

# Upload/Download file:
# 	- navigate to ‘https://the-internet.herokuapp.com/upload’
# 	- upload file (e.g. .txt)
# 	- verify success message appears
# 	- navigate to ‘https://the-internet.herokuapp.com/download’
# 	- download uploaded file from step 2
# 	- verify that file successfully downloaded
def test_downloaduplloadedfille(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    # # page.pause()  #for debug in codgen
    #choosefile
    page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("test1.txt")
    #upload file
    page.get_by_role("button", name="Upload").click()
    #open download page
    page.goto("https://the-internet.herokuapp.com/download")
    #download uplloaded fille
    with page.expect_download() as download_info:
        page.get_by_role("link", name="test1.txt").click()
        assert download_info.value.suggested_filename == "test1.txt"
    download = download_info.value
    assert "test1.txt" == download.suggested_filename
    page.wait_for_timeout(3000)
    print(download.path())


    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_downloaduplloadedfille(playwright)
