import allure
from locators.login_page_locators import LoginPageBurgerLocators
from locators.register_page_locators import RegisterPageBurgerLocators
from locators.urls import ORDER_FEED_PAGE_URL, MAIN_PAGE_BURGER_URL, REGISTER_BURGER_URL
from pages.base_page import BasePage



class RegisterPage(BasePage):
    @allure.step('Регистрация пользователя')
    def registration_user(self,name, email, password):
        self.open_url(REGISTER_BURGER_URL)
        self.send_keys(RegisterPageBurgerLocators.NAME_REGISTRATION, name)
        self.send_keys(RegisterPageBurgerLocators.EMAIL_REGISTRATION,email)
        self.send_keys(RegisterPageBurgerLocators.PASSWORD_REGISTRATION, password)
        self.click_on_element(RegisterPageBurgerLocators.BUTTON_REGISTRATION)
        self.wait_visibility(LoginPageBurgerLocators.BUTTON_LOGIN)
