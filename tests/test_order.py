import pytest
import allure
import logging

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.config import BASE_URL
from data.order_data import ORDER_DATA
from locators.main_page_locators import MainPageLocators

logger = logging.getLogger(__name__)


class TestOrder:

    @allure.title("Заказ самоката: успешное оформления заказа")
    @pytest.mark.parametrize(
        "order_button",
        [
            MainPageLocators.HEADER_ORDER_BUTTON,
            MainPageLocators.MIDDLE_ORDER_BUTTON,
        ]
    )
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_success(self, driver, order_button, data):
        page = MainPage(driver)
        page.open(BASE_URL)

        page.click_order_button(order_button)

        order = OrderPage(driver)
        order.fill_order_step_one(data)
        order.fill_order_step_two(data)

        order_number = order.get_order_number()
        logger.info("Номер заказа: %s", order_number)

        assert order.get_order_success_message_element().is_displayed(), (
            "Окно подтверждения заказа не отобразилось"
        )

        assert order_number is not None, (
            "Номер заказа не был получен"
        )
