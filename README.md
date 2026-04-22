# Sprint_6
Структура проекта
Sprint_6/



├── allure_results                               # для Allure-отчётов
│
├── data/
│   └── config.py                                # URL сайта
│   └── faq_data.py                              # Тестовые данные для FAQ
│   └── order_data.py                            # Тестовые данные для заказа самоката
│
├── locators/
│   └── main_page_locators.py                    # Локаторы для главной страницы
│   └── order_page_locators.py                   # Локаторы для страницы заказа самоката
│
├── pages/
│   └── base_page.py                             # page object основные
│   └── main_page.py                             # page object главной страницы
│   └── order_page.py                            # page object страницы заказа самоката
│
├── tests/
│   └── test_faq.py                              # Тесты на проверку FAQ
│   └── test_logo.py                             # Тесты переходов по лого
│   └── test_order.py                            # Тесты заказа самоката
│
├── gitignore                                    # Файл для игнорирования файлов в Git
├── conftest.py                                  # Фикстуры
├── pytest.ini                                   # Файл конфигурации pytest
├── README.md                                    # Описание проекта
└── requirements.txt                             # Список внешних зависимостей




Запуск тестов: pytest tests -v
Сфформировать отчёт в формате веб-страницы: allure serve allure_results 


Пример выполнения: tests/test_faq.py::TestFAQ::test_faq_answers[0-Сутки — 400 рублей. Оплата курьеру — наличными или картой.]
--------------------------------------------------------------------------------------------- live log call 
INFO     pages.main_page:main_page.py:21 Найден таб 0: Сколько это стоит? И как оплатить?
INFO     pages.main_page:main_page.py:29 Текст ответа для таба 0: Сутки — 400 рублей. Оплата курьеру — наличными или картой.
PASSED                                                                                                                [  7%] 
tests/test_faq.py::TestFAQ::test_faq_answers[1-Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, 
можете просто сделать несколько заказов — один за другим.]
---------------------------------------------------------------------------------------------