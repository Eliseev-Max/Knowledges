from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


MAIN = "http://172.19.16.229/"
LAPTOPS_AND_NOTEBOOKS = MAIN + "laptop-notebook"
DESKTOPS = MAIN + "desktops"
PRODUCT_CARD = MAIN + "mp3-players/ipod-classic"
LOGIN_PAGE = MAIN + "index.php?route=account/login"
ADMIN_LOGIN_PAGE = MAIN + "admin/"

browser.get(MAIN)        # Главная

# browser.get(LAPTOPS_AND_NOTEBOOKS)     # Каталог лэптопов и ноутбуков
#
# browser.get(DESKTOPS)        # Каталог десктопов
#
# browser.get(PRODUCT_CARD)    # Карточка товара
#
# browser.get(LOGIN_PAGE)
#
# browser.get(ADMIN_LOGIN_PAGE)