from UserLoginPage import UserLoginPage


def test_find_continue_btn_on_login_page(browser, base_url):
    user_login_page = UserLoginPage(browser)
    user_login_page.go_to_login_page(base_url)
    user_login_page.find_web_element(user_login_page.CONTINUE_BUTTON)
    user_login_page.find_web_element(user_login_page.INPUT_PASSWORD)


def test_click_Login_without_filling_fields(browser, base_url):
    user_login_page = UserLoginPage(browser)
    user_login_page.go_to_login_page(base_url)
    user_login_page.check_element_appears_after_click(user_login_page.LOGIN_BUTTON, user_login_page.WARNING_ALERT)


def test_create_new_user(browser, base_url):
    new_user = UserLoginPage(browser)
    new_user.go_to_account_reg_page(base_url)
    new_user.enter_first_and_last_name()
    new_user.enter_all_fields()
    new_user.wait_and_click(new_user.PRIVACY_POLICY_CHECKBOX)
    new_user.wait_and_click(new_user.SUBMIT_CONTINUE_BUTTON)
    assert new_user.view_success_notification() == "Your Account Has Been Created!"
