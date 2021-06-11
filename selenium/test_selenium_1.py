import pytest
import selenium


# @pytest.mark.parametrize("url, title",[
#     ("http://172.19.16.229/", "Your Store"),
#     ("https://yandex.ru", "Яндекс"),
#     ("https://google.com", "Google")
# ])
# def test_title_yandex(browser, url, title):
#     browser.get(url)
#     current_title = browser.title
#     assert current_title == title

def test_base_url(browser, base_url):
    browser.get(base_url)
    assert browser.find_element_by_css_selector("#logo")