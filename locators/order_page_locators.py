from selenium.webdriver.common.by import By

# Локаторы страницы заказа самоката "{BASE_URL}/order"


class OrderPageLocators:
    # ФОС "Для кого самокат"
    # Имя
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    # Фамилия
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Адрес
    ADDRESS = (
        By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Метро
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")

    def METRO_OPTION(text): return (
        By.XPATH, f"//div[contains(@class,'select-search__select')]//div[text()='{text}']")
    # Номер телефона
    PHONE = (
        By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # ФОС "Про аренду"
    # Когда привезти самокат
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Срок аренды
    RENT = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")

    def RENT_OPTION(text): return (
        By.XPATH, f"//div[contains(@class,'Dropdown-menu')]//div[text()='{text}']")
    # Цвет самоката
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    # Комментарий для курьера
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка "Заказать"
    ORDER_BUTTON = (
        By.XPATH, "//div[@class='Order_Content__bmtHS']//button[text()='Заказать']")

    # Всплывающее окно подтверждения
    # Кнопка "Да"
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Окно с информацией о заказе
    # Сообщение "Заказ оформлен"
    ORDER_SUCCESS_MESSAGE = (
        By.XPATH, "//div[contains(@class,'Order_ModalHeader') and contains(text(),'Заказ оформлен')]")
    # Текст с номером заказа
    ORDER_NUMBER = (By.XPATH, "//*[contains(., 'Номер заказа')]")
