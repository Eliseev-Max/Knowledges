from handler import *
from WebPages import *


LAPTOPS_AND_NOTEBOOKS = "laptop-notebook/"
PRODUCT_CARD = "mp3-players/ipod-classic"
LOGIN_PAGE = "index.php?route=account/login"
ADMIN_LOGIN_PAGE = "admin/"


# Поиск элементов на Главной странице
def test_has_title_appeared(browser, base_url):
    TITLE = "Your Store"
    wait_title(browser, base_url, TITLE, timeout=2)


def test_click_shopping_cart_button(browser, base_url):
    find_element_after_click(browser, base_url, MainPage.CART_BUTTON, MainPage.SHOPPING_CART_ALERT)


def test_make_title_Search(browser, base_url):
    TITLE = "Search"
    wait_title(browser, base_url, TITLE, click=MainPage.SEARCH_BUTTON)


def test_message_adding_in_wish_list(browser, base_url):
    find_element_after_click(browser, base_url, MainPage.ADD_TO_WISH_LIST, MainPage.SUCCESS_OR_DISMISS_ALERT)


def test_My_Account_drop_down_list(browser, base_url):
    find_element_after_click(browser, base_url, MainPage.MY_ACCOUNT_CARET, MainPage.REGISTER, timeout=0.5)
    find_element_after_click(browser, base_url, MainPage.MY_ACCOUNT_CARET, MainPage.LOGIN, timeout=0.5)


# Laptops & Notebooks


def test_add_product_to_comparison(browser, base_url):
    URL = base_url + LAPTOPS_AND_NOTEBOOKS
    find_element_after_click(browser, URL, Catalog.COMPARE_PRODUCT, Catalog.PRODUCT_COMPARE_1)


def test_click_Login_without_filling_fields(browser, base_url):
    URL = base_url + ADMIN_LOGIN_PAGE
    find_element_after_click(browser, URL, AdminLoginPage.LOGIN_BUTTON, AdminLoginPage.NO_MATCHES_ALERT)