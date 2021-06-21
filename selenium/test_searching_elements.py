# -*-coding: utf-8-*-

from WebPages import *
from handler import element_existence
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LAPTOPS_AND_NOTEBOOKS = "laptop-notebook/"
PRODUCT_CARD = "mp3-players/ipod-classic"
LOGIN_PAGE = "index.php?route=account/login"
ADMIN_LOGIN_PAGE = "admin/"


# Поиск элементов на главной страние
def test_find_elements_on_main_page(browser, base_url):
    element_existence(browser, base_url, MainPage.LOGO_TEXT)
    element_existence(browser, base_url, MainPage.SEARCH_LINE)
    element_existence(browser, base_url, MainPage.FEATURED)


def test_number_of_product_thumbs(browser, base_url):
    browser.get(base_url)
    prod_thumbs = browser.find_elements(*MainPage.PRODUCT_THUMB)
    assert len(prod_thumbs) == 4


# Поиск элементов на странице каталога Laptops&Notebooks
def test_find_elements_in_catalog(browser, base_url):
    CATALOG_PAGE = base_url + LAPTOPS_AND_NOTEBOOKS
    element_existence(browser, CATALOG_PAGE, Catalog.LAPTOPS_NOTEBOOKS)
    element_existence(browser, CATALOG_PAGE, Catalog.LINK_WINDOWS)


# Поиск элементов на странице карточки товара
def test_number_of_thumbnails(browser, base_url):
    browser.get(base_url + PRODUCT_CARD)
    thumbnails = browser.find_elements(*ProductCard.THUMBNAILS)
    assert len(thumbnails) == 3


def test_find_elements_in_prod_card(browser, base_url):
    URL_PROD_CARD = base_url + PRODUCT_CARD
    element_existence(browser, URL_PROD_CARD, ProductCard.TAB_CONTENT)
    element_existence(browser, URL_PROD_CARD, ProductCard.PRICE)

# Поиск элементов на странице логина
def test_find_pwd_field_on_login_page(browser, base_url):
    URL_LOGIN_PAGE = base_url + LOGIN_PAGE
    element_existence(browser, URL_LOGIN_PAGE, LoginPage.INPUT_PASSWORD)


def test_find_continue_btn_on_login_page(browser, base_url):
    URL_LOGIN_PAGE = base_url + LOGIN_PAGE
    element_existence(browser, URL_LOGIN_PAGE, LoginPage.CONTINUE_BUTTON)


def test_click_on_continue_btn(browser, base_url):
    URL_LOGIN_PAGE = base_url + LOGIN_PAGE
    browser.get(URL_LOGIN_PAGE)
    browser.find_element(*LoginPage.CONTINUE_BUTTON).click()


# # Поиск элементов на странице логина в админку
def test_find_elements_on_admin_login_page(browser, base_url):
    ADM_LOGIN_PAGE = base_url + ADMIN_LOGIN_PAGE
    element_existence(browser, ADM_LOGIN_PAGE, AdminLoginPage.INPUT_USERNAME)


def test_click_on_login_button(browser, base_url):
    browser.get(base_url + ADMIN_LOGIN_PAGE)
    browser.find_element(*AdminLoginPage.LOGIN_BUTTON).click()
