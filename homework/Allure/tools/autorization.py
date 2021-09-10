import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

MAIN_URL = "http://172.19.16.229/"


class LoginOnAdminPage:

    LOCATION = '/admin/'
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".text-right button")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger('Admin\'s_autorization')

    def go_to(self, url):
        self.logger.info("Going to the {}".format(url))
        self.browser.get(url + self.LOCATION)

    def enter_username(self, username):
        self.logger.info("Enter \'{}\' in the field \'Username\'".format(username))
        username_field = self.browser.find_element(*self.INPUT_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        self.logger.info("Enter \'{}\' in the field \'Password\'".format(password))
        pwd_field = self.browser.find_element(*self.INPUT_PASSWORD)
        pwd_field.clear()
        pwd_field.send_keys(password)

    def submit(self):
        self.logger.info("Clicking on the Submit button")
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def submit_with_ENTER(self):
        self.logger.info("Pushing the ENTER button on the keyboard")
        self.browser.find_element(*self.LOGIN_BUTTON).send_keys(Keys.ENTER)

    def log_in(self, url, username, password):
        self.go_to(url)
        self.enter_username(username)
        self.enter_password(password)
        self.submit_with_ENTER()
