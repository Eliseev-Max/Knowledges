from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPage:

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

    def seek_element(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException as no_elem:
            raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")

    import random
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    from selenium.webdriver.support import expected_conditions as EC
    from AdminPage import AdminPage as AP

       
# def find_web_element(self, locator):
#     try:
#         el = self.browser.find_element(*locator)
#     except NoSuchElementException as no_elem:
#         raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")
#     return el
#
# def check_element_appears_after_click(self, clickable_elem, expected_elem):
#     self.find_web_element(clickable_elem).click()
#     try:
#         WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(expected_elem))
#     except TimeoutException as time_is_up:
#         raise AssertionError(time_is_up, f"Время ожидания элемента {expected_elem[1]} истекло")


    def find_and_fill_the_field(self, web_element_field, text):
        web_element_field.clear()
        web_element_field.send_keys(text)

