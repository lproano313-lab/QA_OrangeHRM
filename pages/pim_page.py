from playwright.sync_api import Page


class PimPage:

    def __init__(self, page: Page):
        self.page = page

    def ir_a_pim(self):
        self.page.locator(
            'a[href="/web/index.php/pim/viewPimModule"]'
        ).click()

    def agregar_empleado(self):
        # =========================
        # ADD EMPLOYEE
        # =========================

        self.page.locator(
            ".orangehrm-header-container button"
        ).click()

        # First Name
        self.page.locator(
            'input[name="firstName"]'
        ).fill("carla")

        # Middle Name
        self.page.locator(
            'input[name="middleName"]'
        ).fill("caza")

        # Last Name
        self.page.locator(
            'input[name="lastName"]'
        ).fill("Prueba1")

        # Employee ID
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Employee Id"
        ).locator("input").fill("2525")

        # Guardar empleado
        self.page.locator(
            'button[type="submit"]'
        ).click()

    def editar_empleado(self):
        # =========================
        # EMPLOYEE LIST
        # =========================

        self.page.locator(
            "a.oxd-topbar-body-nav-tab-item"
        ).filter(
            has_text="Employee List"
        ).click()

        # Buscar empleado
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Employee Name"
        ).locator("input").fill(
            "carla caza Prueba1"
        )

        # Search
        self.page.locator(
            'button[type="submit"]'
        ).click()

        # Editar primer resultado
        self.page.locator(
            ".oxd-table-cell-actions button"
        ).first.click()

        # =========================
        # PERSONAL DETAILS
        # =========================

        # Other Id
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Other Id"
        ).locator("input").fill("OT123")

        # Driver's License Number
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Driver's License Number"
        ).locator("input").fill("LIC123456")

        # License Expiry Date
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="License Expiry Date"
        ).locator("input").fill("2030-12-31")

        # Nationality
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Nationality"
        ).locator(".oxd-select-text").click()

        self.page.locator(
            ".oxd-select-option"
        ).filter(
            has_text="Ecuador"
        ).click()

        # Marital Status
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Marital Status"
        ).locator(".oxd-select-text").click()

        self.page.locator(
            ".oxd-select-option"
        ).filter(
            has_text="Married"
        ).click()

        # Date of Birth
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Date of Birth"
        ).locator("input").fill("1999-01-15")

        # Gender - Male
        self.page.locator(
            'input[type="radio"][value="1"]'
        ).check(force=True)

        # Blood Type
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Blood Type"
        ).locator(".oxd-select-text").click()

        self.page.locator(
            ".oxd-select-option"
        ).filter(
            has_text="A+"
        ).click()

        # Test Field
        self.page.locator(
            ".oxd-input-group"
        ).filter(
            has_text="Test_Field"
        ).locator("input").fill("Prueba QA")

        # =========================
        # CAMBIAR FOTO
        # =========================


        self.page.locator(
            ".orangehrm-edit-employee-image-wrapper"
        ).click()

        # Subir imagen directamente
        self.page.locator(
            'input[type="file"]'
        ).set_input_files(
            "tests/archivos/serpiente.jpg"
        )
        # Guardar foto
        self.page.locator(
            "button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space"
        ).click()