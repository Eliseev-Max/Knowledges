import random
from Catalog import Catalog


# Поиск элементов на странице каталога Laptops&Notebooks
def test_find_elements_in_catalog(browser, base_url):
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    cat.find_web_element(Catalog.LAPTOPS_NOTEBOOKS)
    cat.find_web_element(Catalog.LINK_WINDOWS)
    cat.find_web_element(Catalog.CART_TOTAL)
    cat.find_web_element(Catalog.PRODUCT_COMPARE_LINK)


def test_add_to_cart(browser, base_url):
    """ Проверяем добавление товара в корзину """
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    all_buttons_to_add = cat.find_all_specified_elements(cat.ADD_TO_CART)
    random.choice(all_buttons_to_add).click()
    cat.wait_web_element(Catalog.ALERT_SUCCESS)


def test_add_to_comparation(browser, base_url):
    """ Проверяем добавление товара к сравнению """
    cat = Catalog(browser)
    cat.go_to_catalog(base_url)
    all_buttons_to_compare = cat.find_all_specified_elements(cat.COMPARE_PRODUCT)
    random.choice(all_buttons_to_compare).click()
    cat.wait_web_element(Catalog.ALERT_SUCCESS)
    assert cat.wait_web_element(cat.PRODUCT_COMPARE_LINK).text == "Product Compare (1)"