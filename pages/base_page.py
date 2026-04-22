import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    def wait(self, timeout=10):
        return WebDriverWait(self.driver, timeout)

    @allure.step("Проскроллить страницу до элемента {locator}")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait(timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        return element

    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator, timeout=10):
        element = self.wait(timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Внести текст в инпут {locator}")
    def type(self, locator, value: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)
        return element

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Переключение в новую вкладку")
    def switch_to_new_window(self, timeout=10):
        self.wait(timeout).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait(timeout).until(lambda d: d.current_url != "about:blank")
        return True

    @allure.step("Ожидание редиректа на Дзен")
    def wait_for_dzen_redirect(self, timeout=10):
        self.wait(timeout).until(
            lambda d: "https://dzen.ru/" in d.current_url and "sso.dzen.ru" not in d.current_url
        )
        return True
