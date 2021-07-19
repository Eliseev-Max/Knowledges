# -*-coding: utf-8-*-

import time
from MainPage import MainPage

CURRENCY = dict({"USD": "$", "EUR": "€", "GBP": "£"})
CURRENCY_LIST = list(CURRENCY.keys())


def test_find_elements_on_main_page(browser, base_url):
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    main_page.find_web_element(MainPage.FEATURED)
    main_page.find_web_element(MainPage.LOGO_TEXT)
    main_page.find_web_element(MainPage.SEARCH_LINE)


def test_number_of_product_thumbs(browser, base_url):
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    assert len(main_page.find_featured_products_parameters(MainPage.PRODUCT_THUMB)) == 4


def test_check_sign_with_changing_currency(browser, base_url):
    """ Проверяем смену знака валюты при смене валюты в хедере главной страницы """
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    for cur in CURRENCY_LIST:
        main_page.choose_currency(cur)
        assert main_page.show_currency_sign() == CURRENCY[cur]
        time.sleep(1)

def test_currency_of_product_price(browser, base_url):
    """ Проверяем смену денежного выражения цены избранных товаров при смене валюты """
    main_page = MainPage(browser)
    main_page.go_to_mainpage(base_url)
    for cur in CURRENCY_LIST:
        main_page.choose_currency(cur)
        prod_list = main_page.find_featured_products_parameters(MainPage.PRODUCT_PRICE)
        for price in prod_list:
            assert CURRENCY[cur] in price.text
        time.sleep(1)
