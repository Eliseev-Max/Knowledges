# -*-coding: utf-8-*-

from WebPages import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LAPTOPS_AND_NOTEBOOKS = "laptop-notebook/"
PRODUCT_CARD = "mp3-players/ipod-classic"
LOGIN_PAGE = "index.php?route=account/login"
ADMIN_LOGIN_PAGE = "admin/"


# Поиск элементов на главной страние
def test_find_elements_on_main_page(browser, base_url):
    browser.get(base_url)
    browser.find_element(*MainPage.LOGO_TEXT)
    browser.find_element(*MainPage.SEARCH_LINE)
    browser.find_element(*MainPage.FEATURED)


def test_number_of_product_thumbs(browser, base_url):
    browser.get(base_url)
    prod_thumbs = browser.find_elements(*MainPage.PRODUCT_THUMB)
    assert len(prod_thumbs) == 4


# Поиск элементов на странице каталога Laptops&Notebooks
def test_find_elements_in_catalog(browser, base_url):
    browser.get(base_url + LAPTOPS_AND_NOTEBOOKS)
    browser.find_element_by_partial_link_text("Windows")
    browser.find_element(*Catalog.LAPTOPS_NOTEBOOKS)


# Поиск элементов на странице карточки товара
def test_number_of_thumbnails(browser, base_url):
    browser.get(base_url + PRODUCT_CARD)
    thumbnails = browser.find_elements(*ProductCard.THUMBNAILS)
    assert len(thumbnails) == 3


def test_find_elements_in_prod_card(browser, base_url):
    browser.get(base_url + PRODUCT_CARD)
    browser.find_element(*ProductCard.TAB_CONTENT)
    browser.find_element(*ProductCard.PRICE)


# Поиск элементов на странице логина
def test_find_pwd_field_on_login_page(browser, base_url):
    browser.get(base_url + LOGIN_PAGE)
    browser.find_element(*LoginPage.INPUT_PASSWORD).click()


def test_find_continue_btn_on_login_page(browser, base_url):
    browser.get(base_url + LOGIN_PAGE)
    browser.find_element(*LoginPage.CONTINUE_BUTTON).click()


# Поиск элементов на странице логина в админку
def test_find_elements_on_admin_login_page(browser, base_url):
    browser.get(base_url + ADMIN_LOGIN_PAGE)
    browser.find_element(*AdminLoginPage.INPUT_USERNAME)
    browser.find_element(*AdminLoginPage.LOGIN_BUTTON).click()