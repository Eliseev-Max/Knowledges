import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Catalog:

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    LOCATION_OF_CATALOG = "laptop-notebook/"
    LAPTOPS_NOTEBOOKS = (By.CSS_SELECTOR, "#content h2")
    LINK_WINDOWS = (By.PARTIAL_LINK_TEXT, "Windows")
    ADD_TO_CART = (By.CSS_SELECTOR, ".button-group .fa.fa-shopping-cart")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price")
    ALERT_SUCCESS = (By.CSS_SELECTOR, "#product-category .alert.alert-success.alert-dismissible")
    COMPARE_PRODUCT = (By.XPATH, "//*[@class='button-group']/button[@data-original-title='Compare this Product']")
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")

    def go_to_catalog(self, url):
        self.browser.get(url + self.LOCATION_OF_CATALOG)
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
