import os
import sys
import pytest
import requests
from playwright.sync_api import sync_playwright

# Asegurar que la carpeta del proyecto esté en el path de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

API_BASE_URL = "http://localhost:3000"
WEB_BASE_URL = "http://localhost:4000"

@pytest.fixture(scope="session")
def api_url():
    return API_BASE_URL

@pytest.fixture(scope="session")
def web_url():
    return WEB_BASE_URL

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        # Usar Chrome del sistema si está disponible para evitar descargas adicionales
        try:
            browser = playwright.chromium.launch(channel="chrome", headless=True)
        except Exception:
            browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()
