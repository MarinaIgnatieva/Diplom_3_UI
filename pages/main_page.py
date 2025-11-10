import allure
from locators.main_page_locators import MainPageBurgerLocators
from locators.urls import ORDER_FEED_PAGE_URL, MAIN_PAGE_BURGER_URL
from pages.base_page import BasePage


class MainPageBurger(BasePage):

    @allure.step('Кликаем на кнопку Лента заказов')
    def click_button_order_feed(self):
        self.click_on_element(MainPageBurgerLocators.Button_order_feed)
        self.wait_url_contains(ORDER_FEED_PAGE_URL)

    @allure.step('Кликаем на кнопку Конструктор')
    def click_button_constructor(self):
        self.click_on_element(MainPageBurgerLocators.Button_constructor)
        self.wait_url_contains(MAIN_PAGE_BURGER_URL)

    @allure.step('Кликаем на раздел Начинка')
    def click_on_tab_ingredients(self):
        self.click_on_element(MainPageBurgerLocators.Tab_ingredients)
        self.wait_visibility(MainPageBurgerLocators.Ingredient_beef_meteorite)

    @allure.step('Кликаем на Ингредиент в разделе Начинки')
    def click_on_ingredient(self):
        self.click_on_element(MainPageBurgerLocators.Ingredient_beef_meteorite)
        self.wait_visibility(MainPageBurgerLocators.Popup_window_with_ingredient_details)

    @allure.step('Закрываем всплывающее окно с деталями ингредиента')
    def click_X_on_popup(self):
        self.click_on_element(MainPageBurgerLocators.Button_close_popup_window)
        self.wait_visibility(MainPageBurgerLocators.Section_burger_constructor)

    @allure.step('Получаем текст заголовка на всплавающем окне')
    def text_header_on_popup(self):
        return self.text(MainPageBurgerLocators.Header_on_popup_window)

    @allure.step('Проверка видимости popup')
    def text_header_visibile(self):
        return len(self.find_list(MainPageBurgerLocators.Popup_window_with_ingredient_details))>0

    @allure.step('Перетянуть ингредиент в заказ')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_elements(MainPageBurgerLocators.Ingredient_beef_meteorite,
                                    MainPageBurgerLocators.Section_burger_order)

    @allure.step('Получить значение на счетчике ингредиента')
    def ingredient_counter_value(self):
        return int(self.text(MainPageBurgerLocators.Ingredient_counter))

    @allure.step('Оформить заказ')
    def order(self):
        self.wait_dissapear(MainPageBurgerLocators.LOADING_OVERLAY)
        self.scroll(MainPageBurgerLocators.Bun_fluorescent)
        self.drag_and_drop_elements(MainPageBurgerLocators.Bun_fluorescent,
                                    MainPageBurgerLocators.Section_burger_order)

        self.click_on_element(MainPageBurgerLocators.Tab_ingredients)
        self.scroll(MainPageBurgerLocators.Ingredient_beef_meteorite)
        self.drag_and_drop_elements(MainPageBurgerLocators.Ingredient_beef_meteorite,
                                    MainPageBurgerLocators.Section_burger_order)

        self.click_on_element(MainPageBurgerLocators.Button_order)
        self.wait_visibility(MainPageBurgerLocators.Popup_number_order)

    @allure.step('Получить идентификатор заказа')
    def id_order(self):
        self.wait_visibility(MainPageBurgerLocators.id_order)
        return int(self.text(MainPageBurgerLocators.id_order))

    @allure.step('Закрыть всплывающее окно с номером заказа')
    def close_popup_with_id_order(self):
        self.wait_clickable_and_click(MainPageBurgerLocators.button_x_popup_window)
        self.wait_visibility(MainPageBurgerLocators.Button_order_feed)

    @allure.step('Открыть главную страницу')
    def open_main_url(self):
        self.open_url(MAIN_PAGE_BURGER_URL)
