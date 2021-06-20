from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_featured_links(browser, base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR, "#cart button").click()
    wdw = WebDriverWait(browser, 2, poll_frequency=0.5)
    wdw.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu .text-center")))

# Запилить в отдельный модуль обработчик Timeout Exception