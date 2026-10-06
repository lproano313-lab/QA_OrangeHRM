from pathlib import Path
from playwright.sync_api import Page

class RecruitmentPage:

    def __init__(self, page: Page):
        self.page = page

    def ir_a_recruitment(self):
        self.page.locator(
            ".oxd-main-menu-item"
        ).filter(
            has_text="Recruitment"
        ).click()

    def agregar_candidate(self):

        # =========================
        # ADD CANDIDATE
        # =========================

        self.page.locator(
            ".orangehrm-header-container button"
        ).click()

        # First Name
        self.page.locator(
            'input[name="firstName"]'
        ).fill("Juan")

        # Middle Name
        self.page.locator(
            'input[name="middleName"]'
        ).fill("Carlos")

        # Last Name
        self.page.locator(
            'input[name="lastName"]'
        ).fill("Prueba")

        # =========================
        # VACANCY
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Vacancy"
        ).locator(
            ".oxd-select-text"
        ).click()

        self.page.locator(
            ".oxd-select-option"
        ).filter(
            has_text="Junior Account Assistant"
        ).click()

        # =========================
        # EMAIL
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Email"
        ).locator("input").fill(
            "juan.prueba.qa@gmail.com"
        )

        # =========================
        # CONTACT NUMBER
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Contact Number"
        ).locator("input").fill(
            "0999999999"
        )

        # =========================
        # KEYWORDS
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Keywords"
        ).locator("input").fill(
            "Python, QA, Automation, Playwright"
        )

        # =========================
        # DATE OF APPLICATION
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Date of Application"
        ).locator("input").fill(
            "2026-10-05"
        )

        # =========================
        # NOTES
        # =========================

        self.page.locator(
            "textarea[placeholder='Type here']"
        ).fill(
            "Candidato para QA Automation"
        )

        # Consentimiento
        self.page.locator(
            'input[type="checkbox"]'
        ).check(force=True)

        # CV / archivo
        ruta_cv = Path("tests/archivos/Prueba_cv.docx").resolve()

        print("CV:", ruta_cv)
        print("Existe:", ruta_cv.exists())

        self.page.locator(
            'input.oxd-file-input[type="file"]'
        ).set_input_files(
            str(ruta_cv)
        )

        # =========================
        # SAVE
        # =========================

        self.page.locator(
            'button[type="submit"]'
        ).click()
    def agregar_vacancy(self):
        # =========================
        # IR A VACANCIES
        # =========================

        self.page.locator(
            "a.oxd-topbar-body-nav-tab-item"
        ).filter(
            has_text="Vacancies"
        ).click()

        # =========================
        # ADD VACANCY
        # =========================

        self.page.get_by_text(
            "Add",
            exact=True
        ).click()

        # =========================
        # VACANCY NAME
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Vacancy Name"
        ).locator(
            "input"
        ).fill(
            "QA Automation Tester"
        )

        # =========================
        # JOB TITLE
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Job Title"
        ).locator(
            ".oxd-select-text"
        ).click()

        self.page.locator(
            ".oxd-select-option"
        ).filter(
            has_text="Software Engineer"
        ).click()

        # =========================
        # DESCRIPTION
        # =========================

        self.page.locator(
            "textarea[placeholder='Type description here']"
        ).fill(
            "Vacante para QA Automation Tester con conocimientos de Python, "
            "Playwright y automatización de pruebas."
        )

        # =========================
        # HIRING MANAGER
        # =========================

        self.page.locator(
            'input[placeholder="Type for hints..."]'
        ).fill("Amelia")

        self.page.locator(
            ".oxd-autocomplete-option"
        ).filter(
            has_text="Amelia Brown"
        ).click()

        # =========================
        # NUMBER OF POSITIONS
        # =========================

        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Number of Positions"
        ).locator(
            "input"
        ).fill(
            "2"
        )

        # =========================
        # SAVE
        # =========================

        self.page.locator(
            'button[type="submit"]'
        ).click()