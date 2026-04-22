import pytest
import allure
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver

    driver.quit()


# Принудительно переименовать собранные тесты после коллекции и раскодировать обратно в русский текст
def pytest_collection_modifyitems(items):
    for item in items:
        try:
            item._nodeid = item._nodeid.encode("utf-8").decode("utf-8")
            item.name = item.name.encode("utf-8").decode("utf-8")
        except Exception:
            pass