import allure
from locators.order_feed_page_locators import OrderFeedBurgerLocators
from locators.urls import ORDER_FEED_PAGE_URL
from pages.base_page import BasePage

class OrderFeedPageBurger(BasePage):

    @allure.step('Открытие страницы "Лента заказов"')
    def open(self):
        self.open_url(ORDER_FEED_PAGE_URL)
        self.wait_visibility(OrderFeedBurgerLocators.Counter_for_all_time)

    @allure.step('Получаем значение счетчика "Выполнено за все время"')
    def text_counter_value_all_time(self):
        return int(self.text(OrderFeedBurgerLocators.Counter_for_all_time))

    @allure.step('Получаем значение счетчика "Выполнено за сегодня"')
    def text_counter_value_today(self):
        return int(self.text(OrderFeedBurgerLocators.Counter_for_today))

    @allure.step('Получение списка заказов из раздела "В работе"')
    def list_order_ids_in_progress(self):
        self.wait_visibility(OrderFeedBurgerLocators.Orders_in_progress)
        return  map(
            lambda li: int(li.text),
            self.find_list(OrderFeedBurgerLocators.Orders_in_progress)
        )