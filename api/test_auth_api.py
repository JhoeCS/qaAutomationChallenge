import pytest

class TestRegisterApi:
    """Pruebas de la API REST para el endpoint /register."""

    def test_tc_reg_01_register_successful(self, api_session, api_url):
        payload = {
            "email": "usuario.valido@correo.com",
            "password": "password123"
        }
        response = api_session.post(f"{api_url}/register", json=payload)
        data = response.json()
        assert response.status_code in [200, 201]
        assert data.get("msg") == "SAVED"

    def test_tc_reg_02_register_boundary_password_5_chars(self, api_session, api_url):
        payload = {
            "email": "limite5@correo.com",
            "password": "12345"
        }
        response = api_session.post(f"{api_url}/register", json=payload)
        data = response.json()
        # Según el requerimiento de mínimo 5 caracteres, 5 caracteres debe ser aceptado.
        assert response.status_code in [200, 201]
        assert data.get("msg") == "SAVED"

    def test_tc_reg_03_register_password_less_than_5_chars(self, api_session, api_url):
        payload = {
            "email": "invalido@correo.com",
            "password": "1234"
        }
        response = api_session.post(f"{api_url}/register", json=payload)
        data = response.json()
        assert response.status_code == 422
        assert data.get("msg") == "INVALID"

    def test_tc_reg_04_register_email_without_at_symbol(self, api_session, api_url):
        payload = {
            "email": "usuariocorreo.com",
            "password": "password123"
        }
        response = api_session.post(f"{api_url}/register", json=payload)
        data = response.json()
        assert response.status_code == 422
        assert data.get("msg") == "INVALID"

    def test_tc_reg_05_register_empty_fields(self, api_session, api_url):
        payload = {
            "email": "",
            "password": ""
        }
        response = api_session.post(f"{api_url}/register", json=payload)
        data = response.json()
        assert response.status_code == 422
        assert data.get("msg") == "REQUIRED"


class TestLoginApi:
    """Pruebas de la API REST para el endpoint /login."""

    def test_tc_log_01_login_successful(self, api_session, api_url):
        payload = {
            "email": "usuario.valido@correo.com",
            "password": "password123"
        }
        response = api_session.post(f"{api_url}/login", json=payload)
        data = response.json()
        assert response.status_code in [200, 201]
        assert data.get("msg") == "LOGIN VALID"

    def test_tc_log_02_login_boundary_password_5_chars(self, api_session, api_url):
        payload = {
            "email": "limite5@correo.com",
            "password": "12345"
        }
        response = api_session.post(f"{api_url}/login", json=payload)
        data = response.json()
        assert response.status_code in [200, 201]
        assert data.get("msg") == "LOGIN VALID"

    def test_tc_log_03_login_password_less_than_5_chars(self, api_session, api_url):
        payload = {
            "email": "usuario@correo.com",
            "password": "1234"
        }
        response = api_session.post(f"{api_url}/login", json=payload)
        data = response.json()
        assert response.status_code in [401, 422]
        assert data.get("msg") == "INVALID"

    def test_tc_log_04_login_email_without_at_symbol(self, api_session, api_url):
        payload = {
            "email": "usuariocorreo.com",
            "password": "password123"
        }
        response = api_session.post(f"{api_url}/login", json=payload)
        data = response.json()
        assert response.status_code in [401, 422]
        assert data.get("msg") == "INVALID"

    def test_tc_log_05_login_empty_fields(self, api_session, api_url):
        payload = {
            "email": "",
            "password": ""
        }
        response = api_session.post(f"{api_url}/login", json=payload)
        data = response.json()
        assert response.status_code == 422
        assert data.get("msg") == "REQUIRED"
