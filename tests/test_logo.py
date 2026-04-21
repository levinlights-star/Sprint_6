import allure

from data.config import BASE_URL, DZEN_URL
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestLogos:

    @allure.title("Логотип Самоката ведёт на главную страницу Самоката")
    def test_scooter_logo_opens_home(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)

        page.click_order_button(MainPageLocators.HEADER_ORDER_BUTTON)
        page.click_scooter_logo()

        assert page.get_current_url() == BASE_URL

    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)

        page.click_yandex_logo()
        page.switch_to_new_window()
        page.wait_for_dzen_redirect()
        assert DZEN_URL in page.get_current_url(), (
            f"Переход на Дзен не произошёл. Текущий URL: {page.get_current_url()}"
        )
