import pytest

def test_title_yandex(browser):
    browser.get("https://yandex.ru")
    current_title = browser.title
    assert current_title == "Яндекс"