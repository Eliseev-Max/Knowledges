from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_LINE = (By.CSS_SELECTOR, "[name=search]")
    LOGO_TEXT = (By.CSS_SELECTOR, "#logo a")
    FEATURED = (By.CSS_SELECTOR, "#content h3")
    PRODUCT_THUMB = (By.CSS_SELECTOR,".product-thumb")


class Catalog:
    LAPTOPS_NOTEBOOKS = (By.CSS_SELECTOR, "#content h2")
    LINK_WINDOWS = (By.PARTIAL_LINK_TEXT, "Windows")


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