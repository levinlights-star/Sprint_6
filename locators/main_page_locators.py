from selenium.webdriver.common.by import By
# Локаторы страницы {BASE_URL}


class MainPageLocators:
    # Заголовок "Вопросы о важном"
    FAQ_HEADER = (
        By.XPATH, "//div[contains(@class, 'Home_SubHeader') and contains(text(), 'Вопросы о важном')]")
    # FAQ вопрос
    FAQ_QUESTION = (
        By.XPATH, "//div[@data-accordion-component='AccordionItem']//div[@role='button']")
    # FAQ ответ
    FAQ_ANSWER = (
        By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']//p")

    # Кнопка "Заказать" в шапке сайта
    HEADER_ORDER_BUTTON = (
        By.XPATH, "//button[contains(@class,'Button_Button') and text()='Заказать']")
    # Кнопка "Заказать" в середине контента
    MIDDLE_ORDER_BUTTON = (
        By.XPATH, "(//button[contains(@class,'Button_Button') and text()='Заказать'])[2]")

    # Логотип "Самоката"
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    # Логотип "Яндекса"
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
