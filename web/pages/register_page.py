from playwright.sync_api import Page

class RegisterPage:
    """Page Object para la página de Registro."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/register"
        self.email_input = self.page.locator("#email")
        self.password_input = self.page.locator("#password")
        self.register_button = self.page.locator("#register")
        self.message_label = self.page.locator("#msg")

    def navigate(self):
        self.page.goto(self.url)

    def register(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.register_button.click()

    def get_message(self) -> str:
        # Espera que el texto cambie del valor inicial "..."
        self.message_label.wait_for()
        return self.message_label.inner_text()
