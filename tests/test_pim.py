from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.pim_page import PimPage


def test_agregar_empleado(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(page)
    login.iniciar_sesion("Admin", "admin123")

    pim = PimPage(page)
    pim.ir_a_pim()
    pim.agregar_empleado()
    pim.editar_empleado()