import allure
import re

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    @allure.step("Заполнить шаг 1: 'Для кого самокат'")
    def fill_order_step_one(self, data: dict):
        with allure.step("Заполнить Имя"):
            self.type(OrderPageLocators.NAME, data["name"])
        with allure.step("Заполнить Фамилию"):
            self.type(OrderPageLocators.SURNAME, data["surname"])
        with allure.step("Заполнить Адрес"):
            self.type(OrderPageLocators.ADDRESS, data["address"])
        with allure.step("Кликнуть по метро"):
            self.click_element(OrderPageLocators.METRO)
        with allure.step("Выбрать станцию метро"):
            self.click_element(OrderPageLocators.METRO_OPTION(data["metro"]))
        with allure.step("Заполнить номер телефона"):
            self.type(OrderPageLocators.PHONE, data["phone"])
        with allure.step("Кликнуть по кнопке 'Далее'"):
            self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color: str):
        color_locators = {
            "black": OrderPageLocators.COLOR_BLACK,
            "grey": OrderPageLocators.COLOR_GREY,
        }
        self.click_element(color_locators[color])

    @allure.step("Заполнить шаг 2: 'Про аренду'")
    def fill_order_step_two(self, data: dict):
        with allure.step("Заполнить дату 'Когда привезти самокат'"):
            self.type(OrderPageLocators.DATE, data["date"])
        with allure.step("Закрыть календарик"):
            date_input = self.wait().until(
                EC.visibility_of_element_located(OrderPageLocators.DATE)
            )
            date_input.send_keys(Keys.ESCAPE)
        with allure.step("Кликнуть по 'Срок аренды'"):
            self.click_element(OrderPageLocators.RENT)
        with allure.step("Выбрать срок аренды"):
            self.click_element(OrderPageLocators.RENT_OPTION(data["rent"]))
        with allure.step("Выбрать цвет самоката"):
            self.select_scooter_color(data["color"])
        with allure.step("Заполнить поле комментарий"):
            self.type(OrderPageLocators.COMMENT, data["comment"])
        with allure.step("Кликнуть по кнопке 'Заказать'"):
            self.click_element(OrderPageLocators.ORDER_BUTTON)
        with allure.step("Кликнуть по кнопке 'Да' в модальном окне"):
            self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        with allure.step("Ждать окно подтверждения заказа"):
            self.wait().until(EC.visibility_of_element_located(
                OrderPageLocators.ORDER_SUCCESS_MESSAGE))

    @allure.step("Получить номер заказа")
    def get_order_number(self, timeout=10):
        def _number_ready(driver):
            try:
                element = self.find_element(OrderPageLocators.ORDER_NUMBER)
                text = (element.text or element.get_attribute(
                    "innerText") or "").strip()
                match = re.search(r"\d+", text)
                return match.group() if match else None
            except:
                return None

        number = self.wait(timeout).until(_number_ready)
        return number if number else None

    @allure.step("Получить элемент окна успешного заказа")
    def get_order_success_message_element(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
