import time
from UserLoginPage import UserLoginPage
from tools.handler import handle_timeout


def test_create_new_user(browser, base_url):
    new_user = UserLoginPage(browser)
    new_user.go_to_account_reg_page(base_url)
    new_user.enter_first_and_last_name()
    new_user.enter_all_fields()
    new_user.agree_with_privacy_policy()
    new_user.submit_form()
    assert new_user.view_success_notification() == "Your Account Has Been Created!"
