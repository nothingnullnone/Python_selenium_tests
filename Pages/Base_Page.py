from selenium.webdriver.common.by import By

from Utils import Wait_Utils
from Utils.Web_Driver_Utils import Driver


class Base_Page:

    def __init__(self, locator, name):
        self.driver = Driver.get_instance()
        self.locator = locator
        self.name = name

    def get_locator(self):
        return self.locator

    def get_form_name(self):
        return self.name

    def is_form_present(self):
        Wait_Utils.wait_to_be_present((By.XPATH, self.locator))
        return True

    def is_form_visible(self):
        Wait_Utils.wait_to_be_visible((By.XPATH, self.locator))
        return True

    def is_form_invisible(self):
        Wait_Utils.wait_to_be_invisible((By.XPATH, self.locator))
        return True
