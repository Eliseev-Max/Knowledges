import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UserLoginPage:

    MAIN_URL = "http://172.19.16.229/"
    LOGIN_PAGE = "index.php?route=account/login"
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".well .btn.btn-primary")
    FIRST_NAME_FIELD = ()
    LAST_NAME_FIELD = ()
    EMAIL_FIELD = ()
    TELEPHONE_FIELD = ()
    PASSWORD_FIELD = ()
    PASSWORD_CONFIRM_FIELD = ()
    PRIVACY_POLICY_CHECKBOX = ()
    SUBMIT_REGISTRATION_FORM = ()
    # Your Account Has Been Created
    SUCCESS_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.pull-right .btn.btn-primary')

    def __init__(self, browser):
        self.browser = browser

    def go_to_login_page(self):
        self.browser.get(self.MAIN_URL + self.LOGIN_PAGE)

    def go_to_account_reg_page(self):
        self.go_to_login_page()
        WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON))

    @staticmethod
    def generate_name():
        abc = "abcdefghijklmnopqrstuvwxyz"
        return "".join(random.sample(abc, random.randint(5, 10))).capitalize()

    @staticmethod
    def generate_email():
        return self.generate_name() + "@testmail.com"

    def enter_first_and_last_name(self):
        pass

    def enter_email(self):
        pass

    def enter_telephone(self):
        pass

    def enter_and_confirm_password(self):
        pass

    def submit_form(self):
        pass
    #
    # def submit(self):
    #     self.browser.find_element(*self.LOGIN_BUTTON).click()
    #
    # def submit_with_ENTER(self):
    #     self.browser.find_element(*self.LOGIN_BUTTON).send_keys(Keys.ENTER)
    #
    # def log_in(self, url, username, password):
    #     self.go_to(url)
    #     self.enter_username(username)
    #     self.enter_password(password)
    #     self.submit_with_ENTER()
