import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    @allure.step('Поиск элемента')
    def find(self, locators):
        return self.driver.find_element(*locators)

    @allure.step('Поиск списка элементов')
    def find_list(self, locators):
        return self.driver.find_elements(*locators)


    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locators):
        self.find(locators).click()


    @allure.step('Заполнение данными')
    def send_keys(self, locators, data):
        self.find(locators).send_keys(data)


    @allure.step('Получить текст элемента')
    def text(self, locators):
        return self.find(locators).text


    @allure.step('Дождаться,пока элемент станет кликабельным')
    def wait_clickable(self, locators):
        return self.wait.until(expected_conditions.element_to_be_clickable(locators))


    @allure.step('Дождаться,кода элемент станет кликабельным, и кликнуть на него')
    def wait_clickable_and_click(self, locators):
        return self.wait_clickable(locators).click()

    def wait_dissapear(self, locators):
        return self.wait.until_not(expected_conditions.visibility_of_element_located(locators))


    @allure.step('Дождаться,когда эелемент станет видимым')
    def wait_visibility(self, locators):
        return self.wait.until(expected_conditions.visibility_of_element_located(locators))


    @allure.step('Дождаться, когда в адресной строке появится адрес')
    def wait_url_contains(self, data):
        return self.wait.until(expected_conditions.url_contains(data))


    @allure.step('Скролл до элемента')
    def scroll(self, locators):
        element = self.find(locators)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element


    @allure.step('Дождаться открытия второй вкладки')
    def wait_second_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))


    @allure.step('Переключиться на новую вкладку')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])


    @allure.step('Определение актуального адреса страницы')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Открытие страницы')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Перетащить объект')
    def drag_and_drop_elements(self, drag, drop):
        source = self.find(drag)
        target = self.find(drop)

        js_script = """
        var source = arguments[0];
        var target = arguments[1];
        var dragEvent = new DragEvent('dragstart', {
            dataTransfer: new DataTransfer(),
            bubbles: true,
            cancelable: true
        });
        source.dispatchEvent(dragEvent);

        var dropEvent = new DragEvent('drop', {
            dataTransfer: dragEvent.dataTransfer,
            bubbles: true,
            cancelable: true
        });
        target.dispatchEvent(dropEvent);

        var dragEndEvent = new DragEvent('dragend', {
            dataTransfer: dragEvent.dataTransfer,
            bubbles: true,
            cancelable: true
        });
        source.dispatchEvent(dragEndEvent);
        """


        self.driver.execute_script(js_script, source, target)
