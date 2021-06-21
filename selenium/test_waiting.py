from handler import *


def test_has_title_appeared(browser, base_url):
    TITLE = "Your Store"
    browser.get(base_url)
    wait_title(TITLE, browser, timeout=1)

def test_featured_links(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "#cart button").click()
    timeout_handle(browser, "p.text-center")


def test_title_became_Search(browser, base_url):
    TITLE = "Search"
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, ".input-group-btn button").click()
    wait_title(TITLE, browser, timeout=1)


# Что ещё проверить?
# <i class="fa fa-heart"></i> - нажать на сердечко, Появится надпись
#   You must login or create an account to save MacBook to your wish list!
# Нажать на стрелочки ("Compare this product") - появится надпись
#  Success: You have added MacBook to your product comparison!
# Свипперы <div class="swiper-pagination carousel0 swiper-pagination-clickable swiper-pagination-bullets">
#   <span class="swiper-pagination-bullet swiper-pagination-bullet-active"></span>
# Каталог: нажатие List/ Grid
#   Sort by
#
#
#