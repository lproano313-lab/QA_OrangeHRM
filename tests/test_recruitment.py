from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage


def test_agregar_vacancy(page: Page):

    page.goto(
        "https://opensource-demo.orangehrmlive.com/"
    )

    login = LoginPage(page)
    login.iniciar_sesion(
        "Admin",
        "admin123"
    )

    recruitment = RecruitmentPage(page)
    recruitment.ir_a_recruitment()
    recruitment.agregar_vacancy()


def test_agregar_candidate(page: Page):

    page.goto(
        "https://opensource-demo.orangehrmlive.com/"
    )

    login = LoginPage(page)
    login.iniciar_sesion(
        "Admin",
        "admin123"
    )

    recruitment = RecruitmentPage(page)
    recruitment.ir_a_recruitment()
    recruitment.agregar_candidate()