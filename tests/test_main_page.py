import allure
from pages.main_page import MainPageBurger
from locators.urls import MAIN_PAGE_BURGER_URL, ORDER_FEED_PAGE_URL


class TestMainPage:

    @allure.title('Проверка перехода по кнопке Лента заказов')
    @allure.description('При нажатии на кнопку Лента заказов открывается страница Лента заказов')
    def test_click_on_order_feed(self, driver):
        page = MainPageBurger(driver)
        page.click_button_order_feed()

        assert ORDER_FEED_PAGE_URL == page.current_url()

    @allure.title('Проверка перехода по кнопке Конструктор')
    @allure.description('При нажатии на кнопку Конструктор открывается главная страница с конструктором заказов')
    def test_click_on_constructor(self, driver):
        page = MainPageBurger(driver)
        page.click_button_order_feed()
        page.click_button_constructor()

        assert MAIN_PAGE_BURGER_URL == page.current_url()

    @allure.title('Проверка открытия всплывающего окна с деталями игредиента')
    @allure.description('При нажатии на ингредиент всплывает окно с деталями ингредиента')
    def test_open_popup_after_click_on_ingredient(self, driver):
        page = MainPageBurger(driver)
        page.click_on_tab_ingredients()
        page.click_on_ingredient()

        assert page.text_header_on_popup() == 'Детали ингредиента'

    @allure.title('Проверка закрытия всплывающего окна с деталями игредиента')
    @allure.description('При нажатии на крестик всплывающее окно с деталями ингредиента закрывается')
    def test_closed_popup_after_click_on_x(self, driver):
        page = MainPageBurger(driver)
        page.click_on_tab_ingredients()
        page.click_on_ingredient()
        page.click_X_on_popup()

        assert not page.text_header_visibile()

    @allure.title('Проверка увеличения счетчика ингредиента')
    @allure.description('При добавлении ингредиента в заказ счетчик ингредиента увеличивается')
    def test_increas_ingredient_counter(self, driver):
        page = MainPageBurger(driver)
        before = page.ingredient_counter_value()
        page.drag_and_drop_ingredient()
        after = page.ingredient_counter_value()

        assert after - before == 1
