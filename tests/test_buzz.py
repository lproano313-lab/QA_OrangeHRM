from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.buzz_newsfeed import BuzzNewsfeedPage


def test_agregar_video(page: Page):

    page.goto(
        "https://opensource-demo.orangehrmlive.com/"
    )

    login = LoginPage(page)
    login.iniciar_sesion(
        "Admin",
        "admin123"
    )

    buzz = BuzzNewsfeedPage(page)

    buzz.ir_a_buzz()

    buzz.agregar_video()

def test_comentar_post(page: Page):
        page.goto(
            "https://opensource-demo.orangehrmlive.com/"
        )

        login = LoginPage(page)
        login.iniciar_sesion(
            "Admin",
            "admin123"
        )

        buzz = BuzzNewsfeedPage(page)
        buzz.ir_a_buzz()
        buzz.comentar_post_mas_comentado()