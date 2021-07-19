from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Product:

    def __init__(self, browser):
        self.browser = browser

    LOCATION_OF_PRODUCT = "mp3-players/ipod-classic"
    THUMBNAILS = (By.CSS_SELECTOR, ".image-additional .thumbnail")
    TAB_CONTENT = (By.CSS_SELECTOR, ".tab-content")
    PRICE = (By.XPATH, "//*[@class='list-unstyled']/li/h2")

    def go_to_product_page(self, url):
        self.browser.get(url + self.LOCATION_OF_PRODUCT)
        return self

    def find_web_element(self, locator):
        try:
            el = self.browser.find_element(*locator)
        except NoSuchElementException as no_elem:
            raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")
        else:
            return el

    def find_all_specified_elements(self, locator):
        return self.browser.find_elements(*locator)

    def wait_web_element(self, locator, timeout=2):
        try:
            el = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as time_is_up:
            raise AssertionError(time_is_up, f"Время ожидания элемента {locator[1]} истекло")
        return el
