from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class RegisterPageBurgerLocators(BaseLocators):

    # форма регистрации
    NAME_REGISTRATION = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    EMAIL_REGISTRATION = (By.XPATH, "//label[text()='Email']/parent::div/input")
    PASSWORD_REGISTRATION = (By.XPATH,"//input[@type='password']")
    BUTTON_REGISTRATION = (By.XPATH, "//button[text()='Зарегистрироваться']")
