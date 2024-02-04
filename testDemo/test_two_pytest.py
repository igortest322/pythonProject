from playwright.sync_api import Page, expect


def test_example2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    #checkboxes are visible on the webpage
    expect(page.locator("#checkboxes")).to_be_visible()
    #read checkboxes states (is selected, is deselected)
    expect(page.get_by_role("checkbox").nth(1)).to_be_checked()
    expect(page.get_by_role("checkbox").first).not_to_be_checked()
    #select deselect checkbox
    page.get_by_role("checkbox").first.check()
    expect(page.get_by_role("checkbox").first).to_be_checked()
    #deselect selected checkbox
    page.get_by_role("checkbox").first.uncheck()
    expect(page.get_by_role("checkbox").first).not_to_be_checked()