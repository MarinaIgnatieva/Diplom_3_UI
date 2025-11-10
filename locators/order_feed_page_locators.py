from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class OrderFeedBurgerLocators(BaseLocators):

    # Счетчик "Выполнено за все время"
    Counter_for_all_time = (By.XPATH, "//p [text() = 'Выполнено за все время:']/following-sibling::p")

    # Счетчик "Выполнено за сегодня"
    Counter_for_today = (By.XPATH, "//p [text() = 'Выполнено за сегодня:']/following-sibling::p")

    # Раздел "В работе"
    Orders_in_progress = (By.XPATH, "//ul [@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li[text() != 'Все текущие заказы готовы!']")




