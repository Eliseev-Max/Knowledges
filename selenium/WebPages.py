from selenium.webdriver.common.by import By


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


class Catalog:
    LAPTOPS_NOTEBOOKS = (By.CSS_SELECTOR, "#content h2")
    LINK_WINDOWS = (By.PARTIAL_LINK_TEXT, "Windows")
    COMPARE_PRODUCT = (By.XPATH, "//*[@class='button-group']/button[@data-original-title='Compare this Product']")
    PRODUCT_COMPARE_1 = (By.LINK_TEXT, "Product Compare (1)")

class ProductCard:
    THUMBNAILS = (By.CSS_SELECTOR, ".image-additional .thumbnail")
    TAB_CONTENT = (By.CSS_SELECTOR, ".tab-content")
    PRICE = (By.XPATH, "//*[@class='list-unstyled']/li/h2")


class LoginPage:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".well .btn")
    INPUT_PASSWORD = (By.NAME, "password")


class AdminLoginPage:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".text-right button")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    NO_MATCHES_ALERT = (By.CSS_SELECTOR, ".panel-body .alert")