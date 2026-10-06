from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def iniciar_sesion(self, usuario, password):
        self.page.get_by_placeholder("Username").fill(usuario)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator(".orangehrm-login-button").click()
