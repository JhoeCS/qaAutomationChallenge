from playwright.sync_api import Page

class LoginPage:
    """Page Object para la página de Login."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = f"{base_url}/login"
        self.email_input = self.page.locator("#email")
        self.password_input = self.page.locator("#password")
        self.login_button = self.page.locator("#login")
        self.message_label = self.page.locator("#msg")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def get_message(self) -> str:
        # Espera que el texto cambie del valor inicial "..."
        self.message_label.wait_for()
        return self.message_label.inner_text()
