import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from MainPage import MainPage

@allure.title("Открытие сайта")
@allure.description("Проверка загрузки главной страницы")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitai_gorod(): 
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome() 
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()

@allure.title("Поиск книги на кириллице")
@allure.description("Проверка получения книг на кириллице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_rus_ui(browser):
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на кириллице"):
        main_page = MainPage(browser)
        main_page.set_cookie_policy()
        text = main_page.search_book_rus_ui('Слово пацана')
        assert text.startswith(
            "Показываем результаты по запросу «Слово пацана»")

@allure.title("Поиск книги на латинице")
@allure.description("Проверка получения книг на латинице")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.positive_test
def test_search_book_eng_ui(browser):
    with allure.step("Открытие веб-страницы в Chrome, поиск книги на латинице"):
        main_page = MainPage(browser)
        main_page.set_cookie_policy()
        text = main_page.search_book_eng_ui('Geroi nashego vremeni')
        assert text.startswith(
            "Показываем результаты по запросу «Geroi nashego vremeni»")

@allure.title("Поиск по символам ")
@allure.description("Проверка поиска по символам ")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_search_invalid_ui(browser):
    with allure.step("Открытие веб-страницы в Chrome, ввод символов "):
        main_page = MainPage(browser)
        main_page.set_cookie_policy()
        text = main_page.search_invalid_ui('))))))))))')
        assert text.startswith("Похоже, у нас такого нет")


@allure.title("Поиск по каталогу")
@allure.description("Тест проверяет корректное выполнение поиска, используя каталог")
@allure.feature("READ")
@allure.severity("normal")
@pytest.mark.positive_test
def test_catalog_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        browser = webdriver.Chrome()
        main_page = MainPage(browser) 
        main_page.set_cookie_policy()
        text = main_page.catalog_search() 
    with allure.step("Проверка текста в выбранной категории каталога"):
        assert text.startswith ("ПОЭЗИЯ И СТИХИ")


@allure.title("Пустая корзина")
@allure.description("Проверка пустой корзины")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui_test
@pytest.mark.negative_test
def test_get_empty_cart(browser):
    with allure.step("Открытие веб-страницы в Chrome, заходим в корзину"):
        main_page = MainPage(browser)
        main_page.set_cookie_policy()
        text = main_page.get_empty_cart()
        assert text.startswith("В корзине ничего нет")