import random
from Product import Product


# Поиск элементов на странице карточки товара
def test_find_elements_on_product_page(browser, base_url):
    prod = Product(browser)
    prod.go_to_product_page(base_url)
    prod.find_web_element(Product.TAB_CONTENT)
    prod.find_web_element(Product.PRICE)


# Проверка количества миниатюр изображения товара
def test_number_of_thumbnails(browser, base_url):
    prod = Product(browser)
    prod.go_to_product_page(base_url)
    assert len(prod.find_all_specified_elements(Product.THUMBNAILS)) == 3