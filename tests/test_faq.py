import pytest
import allure

from pages.main_page import MainPage
from data.config import BASE_URL
from data.faq_data import FAQ_ANSWERS

from locators.main_page_locators import MainPageLocators


class TestFAQ:

    @allure.title("FAQ Отображение ответов по клику на вопрос")
    @allure.description("FAQ: при клике на вопрос отображается корректный текст ответа")
    @pytest.mark.parametrize(
        "index, answer", FAQ_ANSWERS,
    )
    def test_faq_answers(self, driver, index, answer):
        allure.dynamic.title(f"FAQ: вопрос {index}")

        page = MainPage(driver)

        with allure.step("Открыть страницу {BASE_URL}"):
            page.open(BASE_URL)

        with allure.step("Прокрутить страницу до блока FAQ"):
            page.scroll_to_element(MainPageLocators.FAQ_HEADER)

        with allure.step(f"Кликнуть по вопросу FAQ с индексом {index}"):
            page.click_faq_question(index)

        with allure.step("Получить текст ответа"):
            answer_text = page.get_faq_answer(index)
            allure.attach(answer_text, name="Фактический ответ",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(answer, name="Ожидаемый ответ",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверить, что текст ответа корректный"):
            assert answer in answer_text, (
                f"{answer_text} - текст ответа не совпадает с {answer}"
            )
