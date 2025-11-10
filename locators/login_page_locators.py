from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class LoginPageBurgerLocators(BaseLocators):

    # форма входа в аккаунт
    LOGIN_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    LOGIN_FORM = (By.XPATH, "//h2[text()='Вход']")
    FORM_EMAIL = (By.XPATH, "//label[text()='Email']/parent::div/input")
    FORM_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    BUTTON_LOGIN = (By.XPATH, "//button [text() = 'Войти']")
