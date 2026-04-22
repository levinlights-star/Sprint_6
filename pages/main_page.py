import logging
import allure

from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class MainPage(BasePage):

    @allure.step("Нажать на вопрос {index} в разделе FAQ")
    def click_faq_question(self, index, timeout=10):
        elements = self.wait(timeout).until(
            EC.visibility_of_all_elements_located(
                MainPageLocators.FAQ_QUESTION)
        )
        elements[index].click()
        logger.info(f"Найден таб {index}: {elements[index].text}")

    @allure.step("Получить текст ответа на вопрос {index} в разделе FAQ")
    def get_faq_answer(self, index, timeout=10):
        answers = self.wait(timeout).until(
            EC.presence_of_all_elements_located(MainPageLocators.FAQ_ANSWER)
        )
        answer_text = answers[index].text
        logger.info(f"Текст ответа для таба {index}: {answer_text}")
        return answer_text

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self, button_locator):
        self.click_element(button_locator)

    @allure.step("Нажать на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
