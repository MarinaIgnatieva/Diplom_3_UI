import allure

from locators.login_page_locators import LoginPageBurgerLocators
from locators.main_page_locators import MainPageBurgerLocators
from locators.urls import LOGIN_BURGER_URL
from pages.base_page import BasePage

class LoginPageBurger(BasePage):
    @allure.step('Авторизация пользователя')
    def login_user(self, email, password):
        self.open_url(LOGIN_BURGER_URL)
        self.send_keys(LoginPageBurgerLocators.FORM_EMAIL, email)
        self.send_keys(LoginPageBurgerLocators.FORM_PASSWORD, password)
        self.wait_dissapear(LoginPageBurgerLocators.LOADING_OVERLAY)
        self.wait_clickable_and_click(LoginPageBurgerLocators.BUTTON_LOGIN)
        self.wait_visibility(MainPageBurgerLocators.Button_order)

