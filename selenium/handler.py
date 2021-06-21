from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def element_existence(driver, url, tuple_By_element):
    driver.get(url)
    try:
        driver.find_element(*tuple_By_element)
    except NoSuchElementException as no_elem:
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except Exception as err:
        raise AssertionError(err)


def wait_title(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError("title не успел подгрузиться")


def timeout_handle(driver, selector, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        raise AssertionError("Селектор {} не обнаружен".format(selector))