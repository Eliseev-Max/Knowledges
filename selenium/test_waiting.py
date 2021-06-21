from handler import *


def test_has_title_appeared(browser, base_url):
    TITLE = "Your Store"
    browser.get(base_url)
    wait_title(TITLE, browser, timeout=1)

def test_featured_links(browser, base_url):
    #APPEARING_ELEMENT = r".dropdown-menu .text-center"
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "#cart button").click()
    timeout_handle(browser, "p.text-center")


def test_title_became_Search(browser, base_url):
    TITLE = "Search"
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, ".input-group-btn button").click()
    wait_title(TITLE, browser, timeout=1)