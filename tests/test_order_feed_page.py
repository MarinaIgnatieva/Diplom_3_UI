import allure
from pages.order_feed_page import OrderFeedPageBurger
from pages.main_page import MainPageBurger

class TestOrderFeedPage:

    @allure.title('Проверка счетчика "Выполнено за все время"')
    @allure.description('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_increas_counter_for_all_time(self, driver, login_user):
        with allure.step('Определяем показатель счетчика до оформления заказа'):
            order_page = OrderFeedPageBurger(driver)
            order_page.open()
            before = order_page.text_counter_value_all_time()

        with allure.step('Оформляем заказ и получаем идентификатор заказа'):
            main_page = MainPageBurger(driver)
            main_page.open_main_url()
            main_page.order()
            main_page.id_order()

        with allure.step('Определяем показатель счетчика после оформления заказа'):
            order_page.open()
            after = order_page.text_counter_value_all_time()

        assert after - before == 1

    @allure.title('Проверка счетчика "Выполнено за сегодня"')
    @allure.description('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_increas_counter_for_today(self, driver, login_user):
        with allure.step('Определяем показатель счетчика до оформления заказа'):
            order_page = OrderFeedPageBurger(driver)
            order_page.open()
            before = order_page.text_counter_value_today()
        with allure.step('Оформляем заказ и получаем идентификатор заказа'):
            main_page = MainPageBurger(driver)
            main_page.open_main_url()
            main_page.order()
            main_page.id_order()
        with allure.step('Определяем показатель счетчика после оформления заказа'):
            order_page.open()
            after = order_page.text_counter_value_today()

        assert after - before == 1

    @allure.title('Проверка раздела "В работе"')
    @allure.description('После оформления заказа его номер появляется в разделе «В работе»')
    def test_increas_counter_for_all_time(self, driver, login_user):
        order_page = OrderFeedPageBurger(driver)
        with allure.step('Оформляем заказ и получаем номер заказа'):
            main_page = MainPageBurger(driver)
            main_page.open_main_url()
            main_page.order()
            id_order = main_page.id_order()
        with allure.step('Открываем страницу Лента заказов и проверяем номер заказа'):
            order_page.open()

        assert id_order in order_page.list_order_ids_in_progress()
