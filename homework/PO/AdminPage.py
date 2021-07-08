from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    CATALOG = (By.LINK_TEXT, "Catalog")
    PRODUCTS = (By.LINK_TEXT, "Products")

    # Локаторы кнопок добавления и сохранения нового товара
    ADD_NEW = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')

    # Локатор вкладки Data
    DATA_TAB = (By.LINK_TEXT, "Data")

    # Локаторы обязательных полей свойств товара
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')

    MODEL_FIELD = (By.CSS_SELECTOR, '#input-model')

    # Локаторы необязательных полей (для наглядности)
    PRICE_FIELD = (By.CSS_SELECTOR, '#input-price')


    def __init__(self, browser):
        self.browser = browser

    def go_to_new_product_editor(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CATALOG)).click()
        WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(self.PRODUCTS)).click()
        WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(self.ADD_NEW)).click()

    def fill_the_field(self, web_element_field, text):
        web_element_field.clear()
        web_element_field.send_keys(text)

    def fill_product_name(self, name):
        prod_name = WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(self.PRODUCT_NAME_FIELD))
        self.fill_the_field(prod_name, name)

    def fill_meta_tag_title(self, text):
        meta_tag_title = self.browser.find_element(*self.META_TAG_TITLE)
        self.fill_the_field(meta_tag_title, text)

    def go_to_tab_Data(self):
        self.browser.find_element(*self.DATA_TAB).click()

    # Перед вызовом метода перейти на вкладку  Data
    def fill_model_field(self, text):
        model = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.MODEL_FIELD))
        self.fill_the_field(model, text)

    def fill_price_field(self, price):
        price_field = self.browser.find_element(*self.PRICE_FIELD)
        self.fill_the_field(price_field, price)

    def save_new_product(self):
        self.browser.find_element(*self.SAVE_BUTTON).click()

    # def add_new_product(self, description):
    #     self.browser.implicity_wait(2)
    #     prod_name = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRODUCT_NAME_FIELD))
    #     meta_tag_title = self.browser.find_element(*self.META_TAG_TITLE)
    #     self.fill_the_field(prod_name, description)
    #     self.fill_the_field(meta_tag_title, description)
    #     model = self.browser.find_element(*self.MODEL_FIELD)
