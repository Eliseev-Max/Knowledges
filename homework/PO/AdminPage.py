import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    AUTORIZED_USER = (By.CSS_SELECTOR, "li.dropdown")
    CATALOG = (By.LINK_TEXT, "Catalog")
    PRODUCTS = (By.LINK_TEXT, "Products")
    # Локаторы кнопок добавления и сохранения нового товара
    ADD_NEW = (By.CSS_SELECTOR, '.fa.fa-plus')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[data-original-title="Save"]')
    DELETE_BUTTON = (By.CSS_SELECTOR,".btn.btn-danger")
    # Локатор вкладки Data
    DATA_TAB = (By.LINK_TEXT, "Data")
    # Локаторы обязательных полей свойств товара
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#input-name1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
    MODEL_FIELD = (By.CSS_SELECTOR, '#input-model')
    # Локаторы необязательных полей (для наглядности)
    PRICE_FIELD = (By.CSS_SELECTOR, '#input-price')
    # Сообщение об успешном добавлении товара
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    # Чекбоксы
    CHECKBOX = (By.NAME,"selected[]")

    def __init__(self, browser):
        self.browser = browser

    def go_to_product_list(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CATALOG)).click()
        WebDriverWait(self.browser, 1).until(EC.visibility_of_element_located(self.PRODUCTS)).click()
        return self

    def go_to_new_product_editor(self):
        self.go_to_product_list()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.ADD_NEW)).click()
        return self

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

    @staticmethod
    def random_string_generator():
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = lower_case.upper()
        numbers = "0123456789"
        symbols = lower_case + upper_case + numbers
        return "".join(random.sample(symbols, random.randint(5, 9)))

    def add_new_product(self):
        self.browser.implicitly_wait(2)
        prod_name = self.browser.find_element(*self.PRODUCT_NAME_FIELD)
        meta_tag_title = self.browser.find_element(*self.META_TAG_TITLE)
        self.fill_the_field(prod_name, self.random_string_generator())
        self.fill_the_field(meta_tag_title, self.random_string_generator())
        self.go_to_tab_Data()
        model = self.browser.find_element(*self.MODEL_FIELD)
        price = self.browser.find_element(*self.PRICE_FIELD)
        self.fill_the_field(model, self.random_string_generator())
        self.fill_the_field(price, random.randint(150,400))
        self.browser.find_element(*self.SAVE_BUTTON).click()

    def choose_products(self, *serial_number):
        checkboxes = self.browser.find_elements(*self.CHECKBOX)
        for el in serial_number:
            checkboxes[int(el)-1].click()

    def delete_products(self):
        self.browser.find_element(*self.DELETE_BUTTON).click()
        WebDriverWait(self.browser, 2).until(EC.alert_is_present())
        self.browser.switch_to.alert.accept()