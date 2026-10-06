from playwright.sync_api import Page
from playwright.sync_api import expect

class BuzzNewsfeedPage:

    def __init__(self, page: Page):
        self.page = page

    def ir_a_buzz(self):

        self.page.locator(
            'a[href="/web/index.php/buzz/viewBuzz"]'
        ).click()

    def agregar_video(self):
        # 1. Esperar a que Buzz esté cargado
        self.page.wait_for_load_state("networkidle")

        # 2. Abrir el modal "Share Video"
        boton_video = self.page.locator("button.oxd-glass-button").filter(
            has_text="Share Video"
        )
        boton_video.wait_for(state="visible")
        boton_video.click()


        # . Esperar a que el campo del modal exista de verdad
        campo_url = self.page.get_by_placeholder("Paste Video URL")
        campo_url.wait_for(state="visible")

        # . Texto del post (el último es el del modal, el primero es el del feed)
        self.page.get_by_placeholder("What's on your mind?").last.fill("zamba")

        # . URL del video
        campo_url.fill("https://www.youtube.com/watch?v=kk4uddaHdDE")

        # . Publicar
        self.page.locator(
            ".orangehrm-buzz-post-modal-actions button[type='submit']"
        ).click()

    def comentar_post_mas_comentado(self):
        comentario_texto = "Excelente publicación, muy interesante."

        self.page.wait_for_load_state("networkidle")

        with self.page.expect_response(lambda r: "buzz" in r.url and r.status == 200):
            self.page.locator(".orangehrm-post-filters-button").filter(
                has_text="Most Commented Posts"
            ).click()

        # El post completo es el contenedor, no solo la cabecera
        primer_post = self.page.locator(".orangehrm-buzz").filter(
            has=self.page.locator(".orangehrm-buzz-post")
        ).first
        primer_post.wait_for(state="visible")



        # Abrir comentarios
        primer_post.locator("i.bi-chat-text-fill").locator("xpath=..").click()

        # Escribir el comentario
        campo = primer_post.get_by_placeholder("Write your comment...")
        campo.fill(comentario_texto)
        campo.press("Enter")

        expect(primer_post).to_contain_text(comentario_texto)