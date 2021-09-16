import allure
from tools.autorization import *
from AdminPage import AdminPage
from tools.handler import *

USERNAME = "user"
PASSWORD = "bitnami"
# Данные для ввода в поля при создании нового товара
PRODUCT_NAME = "Xiaomi Redmi 9"
META_TAG_TITLE = "Xiaomi, Redmi"
MODEL = "Redmi 9"
PRICE = "150"


# Проверяем процедуру авторизации
@allure.title("Проверка авторизации администратора")
@allure.description("Переходим на страницу авторизации администратора и заполняем поля Username и Password "\
                    "значениями {} и {} соответственно".format(USERNAME, PASSWORD))
def test_autorization_on_admin_page(browser, base_url):
    autorization = LoginOnAdminPage(browser)
    autorization.go_to(base_url)
    autorization.enter_username(USERNAME)
    autorization.enter_password(PASSWORD)
    autorization.submit()
    # autorization.submit_with_ENTER()
    handle_timeout(browser, AdminPage(browser).AUTORIZED_USER)


# Проверяем добавление нового товара
# def test_add_new_product(browser, base_url):
#     LoginOnAdminPage(browser).log_in(base_url, "user", "bitnami")
#     admin = AdminPage(browser)
#     admin.go_to_new_product_editor()
#     admin.fill_product_name(PRODUCT_NAME)
#     admin.fill_meta_tag_title(META_TAG_TITLE)
#     admin.go_to_tab_Data()
#     admin.fill_model_field(MODEL)
#     admin.fill_price_field(PRICE)
#     admin.save_new_product()
#     handle_timeout(browser, admin.ALERT_SUCCESS, timeout=2)


# Проверяем добавление нового товара со вводом сгенерированных случайным образом строк в поля
@allure.title("Добавление нового товара")
@allure.description("Проверяем добавление нового товара со вводом сгенерированных случайным образом строк в поля")
def test_add_new_product(browser, base_url):
    LoginOnAdminPage(browser).log_in(base_url, "user", "bitnami")
    admin = AdminPage(browser)
    admin.go_to_new_product_editor().add_new_product()
    handle_timeout(browser, admin.ALERT_SUCCESS, timeout=2)

@allure.title("Удаление товара с заданным ID")
@allure.description("Удаляем товар с ID=20")
def test_delete_element(browser, base_url):
    LoginOnAdminPage(browser).log_in(base_url, "user", "bitnami")
    admin = AdminPage(browser)
    admin.go_to_product_list()
    admin.choose_products(20)
    admin.delete_products()
    handle_timeout(browser, admin.ALERT_SUCCESS, timeout=2)
