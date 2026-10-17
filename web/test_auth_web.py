import pytest
from playwright.sync_api import expect

try:
    from web.pages.register_page import RegisterPage
    from web.pages.login_page import LoginPage
except ModuleNotFoundError:
    from pages.register_page import RegisterPage
    from pages.login_page import LoginPage

class TestRegisterWeb:
    """Pruebas E2E de interfaz de usuario para Registro."""

    def test_tc_reg_01_web_register_successful(self, page, web_url):
        register_page = RegisterPage(page, web_url)
        register_page.navigate()
        register_page.register("usuario.web@correo.com", "password123")
        
        # Validar que el mensaje en pantalla sea SAVED
        expect(register_page.message_label).to_have_text("SAVED", timeout=5000)

    def test_tc_reg_02_web_register_boundary_password_5_chars(self, page, web_url):
        register_page = RegisterPage(page, web_url)
        register_page.navigate()
        register_page.register("limite5.web@correo.com", "12345")
        
        # Según requerimiento, 5 caracteres debe ser aceptado
        expect(register_page.message_label).to_have_text("SAVED", timeout=5000)

    def test_tc_reg_03_web_register_password_less_than_5_chars(self, page, web_url):
        register_page = RegisterPage(page, web_url)
        register_page.navigate()
        register_page.register("usuario.web@correo.com", "1234")
        
        expect(register_page.message_label).to_have_text("INVALID", timeout=5000)

    def test_tc_reg_04_web_register_missing_at_symbol(self, page, web_url):
        register_page = RegisterPage(page, web_url)
        register_page.navigate()
        register_page.register("usuariocorreo.com", "password123")
        
        expect(register_page.message_label).to_have_text("INVALID", timeout=5000)

    def test_tc_reg_05_web_register_empty_fields(self, page, web_url):
        register_page = RegisterPage(page, web_url)
        register_page.navigate()
        register_page.register("", "")
        
        expect(register_page.message_label).to_have_text("REQUIRED", timeout=5000)


class TestLoginWeb:
    """Pruebas E2E de interfaz de usuario para Login."""

    def test_tc_log_01_web_login_successful(self, page, web_url):
        login_page = LoginPage(page, web_url)
        login_page.navigate()
        login_page.login("usuario.web@correo.com", "password123")
        
        expect(login_page.message_label).to_have_text("LOGIN VALID", timeout=5000)

    def test_tc_log_02_web_login_boundary_password_5_chars(self, page, web_url):
        login_page = LoginPage(page, web_url)
        login_page.navigate()
        login_page.login("limite5.web@correo.com", "12345")
        
        expect(login_page.message_label).to_have_text("LOGIN VALID", timeout=5000)

    def test_tc_log_03_web_login_password_less_than_5_chars(self, page, web_url):
        login_page = LoginPage(page, web_url)
        login_page.navigate()
        login_page.login("usuario.web@correo.com", "1234")
        
        expect(login_page.message_label).to_have_text("INVALID", timeout=5000)

    def test_tc_log_04_web_login_missing_at_symbol(self, page, web_url):
        login_page = LoginPage(page, web_url)
        login_page.navigate()
        login_page.login("usuariocorreo.com", "password123")
        
        expect(login_page.message_label).to_have_text("INVALID", timeout=5000)

    def test_tc_log_05_web_login_empty_fields(self, page, web_url):
        login_page = LoginPage(page, web_url)
        login_page.navigate()
        login_page.login("", "")
        
        expect(login_page.message_label).to_have_text("REQUIRED", timeout=5000)
