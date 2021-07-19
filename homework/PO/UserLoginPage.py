import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from AdminPage import AdminPage as AP

class UserLoginPage:

    LOGIN_PAGE = "index.php?route=account/login"
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".well .btn.btn-primary")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[value=Login]")
    WARNING_ALERT = (By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    INPUT_PASSWORD = (By.NAME, "password")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE_FIELD = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM_FIELD = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME,"agree")
    SUBMIT_CONTINUE_BUTTON = (By.CSS_SELECTOR, ".pull-right .btn.btn-primary")
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, "#content h1")

    def __init__(self, browser):
        self.browser = browser

    def go_to_login_page(self, url):
        self.browser.get(url + self.LOGIN_PAGE)
        return self

    def go_to_account_reg_page(self, url):
        self.go_to_login_page(url)
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON)).click()
        return self

    def find_web_element(self,locator):
        try:
            el = self.browser.find_element(*locator)
        except NoSuchElementException as no_elem:
            raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")
        return el

    def check_element_appears_after_click(self, clickable_elem, expected_elem):
        self.find_web_element(clickable_elem).click()
        try:
            WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(expected_elem))
        except TimeoutException as time_is_up:
            raise AssertionError(time_is_up, f"Время ожидания элемента {expected_elem[1]} истекло")

    @staticmethod
    def generate_name():
        ABC = "abcdefghijklmnopqrstuvwxyz"
        return "".join(random.sample(ABC, random.randint(5, 10))).capitalize()

    @staticmethod
    def generate_email():
        return f"{AP.random_string_generator()}@test.com"

    def find_and_fill_the_field(self, web_element_field, text):
        web_element_field.clear()
        web_element_field.send_keys(text)

    def enter_first_and_last_name(self):
        first_name = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        last_name = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        self.find_and_fill_the_field(first_name, self.generate_name())
        self.find_and_fill_the_field(last_name, self.generate_name())

    def enter_email(self):
        email_field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        self.find_and_fill_the_field(email_field, self.generate_email())

    def enter_telephone(self):
        telephone_field = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.TELEPHONE_FIELD))
        phone_number = "+71234567890"
        self.find_and_fill_the_field(telephone_field, phone_number)

    def enter_and_confirm_password(self):
        password = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        confirm_pwd = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PASSWORD_CONFIRM_FIELD))
        generated_pwd = AP.random_string_generator()
        self.find_and_fill_the_field(password, generated_pwd)
        self.find_and_fill_the_field(confirm_pwd, generated_pwd)

    def enter_all_fields(self):
        self.enter_first_and_last_name()
        self.enter_email()
        self.enter_telephone()
        self.enter_and_confirm_password()

    def agree_with_privacy_policy(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.PRIVACY_POLICY_CHECKBOX)).click()

    def submit_form(self):
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SUBMIT_CONTINUE_BUTTON)).click()

    def view_success_notification(self):
        notification = WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.SUCCESS_NOTIFICATION))
        return notification.text
