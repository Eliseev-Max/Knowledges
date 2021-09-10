import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = logging.getLogger('EventHandler')


def element_existence(driver, url, locator):
    logger.info("Opening source: {}".format(url))
    driver.get(url)
    try:
        logger.info("Searching element: {}".format(locator))
        driver.find_element(*locator)
    except NoSuchElementException as no_elem:
        logger.error("Element \"{}\" not found on page".format(locator))
        raise AssertionError(no_elem, f"Селектор {locator[1]} не обнаружен")


def wait_title(driver, url, title, click=False, timeout=3):
    logger.info("Opening source: {}".format(url))
    driver.get(url)
    try:
        if click:
            logger.info("Clicking the element \"{}\"".format(click))
            driver.find_element(*click).click()
        logger.info("Waiting for the title \"{}\" to appear within {} seconds".format(title, timeout))
        WebDriverWait(driver, timeout).until(EC.title_is(title))
    except NoSuchElementException as no_elem:
        logger.error("No such title (\"{}\") on this page".format(title))
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except TimeoutException:
        logger.error("Time to load title is up")
        raise AssertionError("title не успел подгрузиться")


def handle_timeout(driver, locator, timeout=3):
    logger.info("Waiting for element {} within {} seconds".format(locator, timeout))
    try:
        elem = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        logger.error("Element \"{}\" not found on page".format(locator))
        raise AssertionError("Веб-элемент {} не обнаружен".format(locator[1]))
    else:
        return elem


def find_element_after_click(driver, url, elem_to_click, required_locator, timeout=2):
    logger.info("Opening source: {}".format(url))
    driver.get(url)
    try:
        logger.info("Clicking on {} and waiting for {} within {}".format(elem_to_click, required_locator, timeout))
        driver.find_element(*elem_to_click).click()
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(required_locator))
    except NoSuchElementException as no_elem:
        logger.error("No such element (\"{}\") on this page".format(elem_to_click))
        raise AssertionError(no_elem, "Данный селектор не обнаружен")
    except TimeoutException as time_is_up:
        logger.error("Item timed out ")
        raise AssertionError(time_is_up, "Время ожидания элемента истекло")


def find_and_fill_the_field(driver, locator, text, timeout=2):
    logger.info("Filling the field: {}".format(locator))
    el = handle_timeout(driver, locator, timeout=timeout).clear()
    el.send_keys(text)