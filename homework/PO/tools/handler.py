from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def element_existence(driver, url, locator):
    driver.get(url)
    try:
        driver.find_element(*locator)
    except NoSuchElementException as no_elem:
        raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")


def wait_title(driver, url, title, click = False, timeout=3):
    driver.get(url)
    try:
        if click is not False:
            driver.find_element(*click).click()
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except NoSuchElementException as no_elem:
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except TimeoutException:
        raise AssertionError("title не успел подгрузиться")


def handle_timeout(driver, locator, timeout=3):
    try:
        elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        raise AssertionError("Веб-элемент {} не обнаружен".format(locator[1]))
    else:
        return elem


def find_element_after_click(driver, url, elem_to_click, required_locator, timeout=2):
    driver.get(url)
    try:
        driver.find_element(*elem_to_click).click()
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(required_locator))
    except NoSuchElementException as no_elem:
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except TimeoutException as time_is_up:
        raise AssertionError(time_is_up, "Время ожидания элемента истекло")


def find_and_fill_the_field(driver, locator, text, timeout=2):
    el = handle_timeout(driver, locator, timeout=timeout).clear()
    el.send_keys(text)