import pytest
from selenium import webdriver
from helper import generate_email, generate_password
from locators.urls import MAIN_PAGE_BURGER_URL
from pages.login_page import LoginPageBurger
from pages.register_page import RegisterPage


class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

# Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture
def driver(request):

    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    driver.get(MAIN_PAGE_BURGER_URL)
    yield driver
    driver.quit()

@pytest.fixture
def new_user(driver):
    page = RegisterPage(driver)
    name = 'Marina999'
    email = generate_email()
    password = generate_password(6)

    page.registration_user(name, email,password)

    return {
        'email': email,
        'password': password
    }

@pytest.fixture
def login_user(driver,new_user):
    page = LoginPageBurger(driver)
    page.login_user(new_user['email'], new_user['password'])
    return True


