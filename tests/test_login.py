from playwright.sync_api import Page
from pages.login_page import LoginPage
def test_login_exitoso(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(page)
    login.iniciar_sesion("Admin", "admin123")
    assert page.locator(".oxd-topbar-header-title").inner_text() == "Dashboard"
