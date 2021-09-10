import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPage:

    SEARCH_LINE = (By.CSS_SELECTOR, "[name=search]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn button")
    LOGO_TEXT = (By.CSS_SELECTOR, "#logo a")
    CURRENCY = (By.CSS_SELECTOR, "button .fa.fa-caret-down")
    EURO = (By.NAME, "EUR")
    POUND_STERLING = (By.NAME, "GBP")
    US_DOLLAR = (By.NAME, "USD")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".btn.btn-link.dropdown-toggle strong")
    FEATURED = (By.CSS_SELECTOR, "#content h3")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price")
    PRODUCT_THUMB = (By.CSS_SELECTOR, ".product-thumb")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart button")
    SHOPPING_CART_ALERT = (By.CSS_SELECTOR, "p.text-center")
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, ".button-group i.fa")
    SUCCESS_OR_DISMISS_ALERT = (By.CSS_SELECTOR, ".alert")
    MY_ACCOUNT_CARET = (By.CSS_SELECTOR, ".caret")
    REGISTER = (By.LINK_TEXT, "Register")
    LOGIN = (By.LINK_TEXT, "Login")

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def go_to_mainpage(self, url):
        self.logger.info("Opening source: {}".format(url))
        self.browser.get(url)
        return self

    def find_web_element(self, locator):
        self.logger.info('Searching element: {}'.format(locator))
        try:
            el = self.browser.find_element(*locator)
        except NoSuchElementException as no_elem:
            self.logger.error("Element {} was not found on the page".format(locator))
            raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")
        else:
            return el

    def wait_web_element(self, locator, timeout=2):
        self.logger.info('Waiting for the element {} within {} seconds'.format(locator, timeout))
        try:
            el = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as time_is_up:
            self.logger.error("Element {} was not found on the page".format(locator))
            raise AssertionError(time_is_up, f"Время ожидания элемента {locator[1]} истекло")
        return el

    def choose_currency(self, currency):
        currency_designations = ["USD", "EUR", "GBP"]
        self.logger.info('Choosing currency: {}'.format(currency))
        self.find_web_element(self.CURRENCY).click()

        if currency.upper() not in currency_designations:
            self.logger.error('{} is not among the available currencies'.format(currency))
            print(f"Указанная валюта {currency} отсутствует в перечне доступных")
            return None
        elif currency.upper() == currency_designations[1]:
            self.find_web_element(self.EURO).click()
        elif currency.upper() == currency_designations[2]:
            self.find_web_element(self.POUND_STERLING).click()
        else:
            self.find_web_element(self.US_DOLLAR).click()

    def show_currency_sign(self):
        return self.find_web_element(self.CURRENCY_SIGN).text

    def find_featured_products_parameters(self, locator):
        self.logger.info('Searching several elements with locator: {}'.format(locator))
        return self.browser.find_elements(*locator)
