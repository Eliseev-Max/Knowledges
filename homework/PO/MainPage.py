from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPage:

    URL = "http://192.168.1.50/"
    SEARCH_LINE = (By.CSS_SELECTOR, "[name=search]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn button")
    LOGO_TEXT = (By.CSS_SELECTOR, "#logo a")
    FEATURED = (By.CSS_SELECTOR, "#content h3")
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

    def seek_element(self, tuple_By_element):
        #self.tuple_By_elements = tuple_By_element
        try:
            self.browser.find_element(*tuple_By_element)
        except NoSuchElementException as no_elem:
            raise AssertionError(no_elem, "Данный селектор не обнаружен")
