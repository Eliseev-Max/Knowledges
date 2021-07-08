import time
from tools.autorization import *
from AdminPage import AdminPage
from tools.handler import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Реализовать генератор рандомных названий
# Реализовать один метод по созданию нового продукта

AUTORIZED_USER = (By.CSS_SELECTOR, "li.dropdown")
PRODUCT_NAME = "Xiaomi Redmi 9"
META_TAG_TITLE = "Xiaomi, Redmi"
MODEL = "Redmi 9"
PRICE = "150"
ALERT_SUCCESS = (By.CSS_SELECTOR, "div .close" )

# Проверяем процедуру авторизации
# def test_autorization_on_admin_page(browser, base_url):
#     autorization = LoginOnAdminPage(browser)
#     autorization.go_to(base_url)
#     autorization.enter_username("user")
#     autorization.enter_password("bitnami")
# #    autorization.submit()
#     autorization.submit_with_ENTER()
#     handle_timeout(browser, AUTORIZED_USER)

def test_add_new_product(browser, base_url):
    LoginOnAdminPage(browser).log_in(base_url, "user", "bitnami")
    admin = AdminPage(browser)
    admin.go_to_new_product_editor()
    admin.fill_product_name(PRODUCT_NAME)
    admin.fill_meta_tag_title(META_TAG_TITLE)
    admin.go_to_tab_Data()
    admin.fill_model_field(MODEL)
    admin.fill_price_field(PRICE)
    admin.save_new_product()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(ALERT_SUCCESS)).click()
    # Проверить появление alert
    time.sleep(5)

# def test_log_in(browser, base_url):
#     LoginOnAdminPage(browser).log_in(base_url, "user", "bitnami")


