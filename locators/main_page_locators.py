from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators


class MainPageBurgerLocators(BaseLocators):

    # Локатор кнопки "Конструктор"
    Button_constructor = (By.XPATH, "//p[(text() = 'Конструктор')]")

    # Локатор кнопки "Лента заказов"
    Button_order_feed = (By.XPATH, "//p[text() = 'Лента Заказов']")

    # Локатор "Личный кабинет"
    Button_personal_account = (By.XPATH, "//p [text() = 'Личный Кабинет']")

    # Локатор раздела "Начинки"
    Tab_ingredients = [By.XPATH, "//span [@class = 'text text_type_main-default' and text() = 'Начинки']"]

    # Локатор раздела "Булки"
    Tab_buns = [By.XPATH, "//span [@class = 'text text_type_main-default' and text() = 'Булки']"]

    # Локатор Начинки "Говяжий метеорит"
    Ingredient_beef_meteorite = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa70']"]

    # Локатор "Флюоресцентная булка"
    Bun_fluorescent = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']"]

    # Счетчик ингредиента
    Ingredient_counter = [By.XPATH, "//a [@href = '/ingredient/61c0c5a71d1f82001bdaaa70']//p [@class = 'counter_counter__num__3nue1']"]

    # Локатор всплывающего окна с деталями Начинки "Говяжий метеорит"
    Popup_window_with_ingredient_details = [By.CLASS_NAME, "Modal_modal_opened__3ISw4"]

    # Заголовок "Детали ингредиента" на всплывающем окне с деталями начинки "Говяжий метеорит"
    Header_on_popup_window = [By.XPATH, "//h2 [@class = 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10' and text() = 'Детали ингредиента']"]

    # Кнопка закрытия всплывающего окна
    Button_close_popup_window = [By.XPATH, "//div [@class = 'Modal_modal__container__Wo2l_']/ button"]

    # Секция оформления заказа
    Section_burger_order = [By.XPATH, "//section [@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']"]

    # Секция Соберите бургер
    Section_burger_constructor = [By.XPATH, "// section [@class = 'BurgerIngredients_ingredients__1N8v2']"]

    # Заголовок "Соберите бургер"
    Header_constructor_burger = [By.XPATH,"// h1 [@class = 'text text_type_main-large mb-5 mt-10' and text() = 'Соберите бургер']"]

    # Кнопка "Оформить заказ"
    Button_order = [By.XPATH, "//button[(text() = 'Оформить заказ')]"]

    # Всплывающее окно с номером заказа
    Popup_number_order = [By.XPATH, "// div [@class = 'Modal_modal__container__Wo2l_']"]

    # Идентификатор заказа
    id_order = (By.XPATH, "// h2 [@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8' and text() != '9999']")

    # Кнопка Х на всплывающем окне с номером заказа
    button_x_popup_window = (By.XPATH, "//button [@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")