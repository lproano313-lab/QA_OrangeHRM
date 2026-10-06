from playwright.sync_api import Page


def test_abrir_orangehrm(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")

    print(page.title())
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.locator(".orangehrm-login-button").click()

    assert page.locator(".oxd-topbar-header-title").inner_text() == "Dashboard"

