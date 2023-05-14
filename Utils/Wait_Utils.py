from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from Config.Filenames import Filenames
from Utils import JSON_Utils
from Utils.Web_Driver_Utils import Driver

timeout = JSON_Utils.get_json_field(Filenames.cfg_file.value, "timeout")


def wait_to_be_visible(webElementBy):
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(visibility_of_element_located(webElementBy))


def wait_to_be_invisible(webElementBy):
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(invisibility_of_element_located(webElementBy))


def wait_to_be_present(webElementBy):
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(presence_of_element_located(webElementBy))


def wait_to_be_clickable(webElementBy):
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(element_to_be_clickable(webElementBy))


def wait_to_open_new_tab(tabsCount):
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(number_of_windows_to_be(tabsCount + 1))


def wait_for_alert():
    driver = Driver.get_instance()
    WebDriverWait(driver, timeout).until(alert_is_present())
