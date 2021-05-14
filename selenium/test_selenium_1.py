import pytest


@pytest.mark.parametrize("url, title",[("https://yandex.ru", "Яндекс"),("https://google.com", "Google")])
def test_title_yandex(browser, url, title):
    browser.get(url)
    current_title = browser.title
    assert current_title == title