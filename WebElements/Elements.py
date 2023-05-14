from selenium.webdriver.common.by import By

from Utils import Wait_Utils
from Utils.Logger import Logger
from Utils.Web_Driver_Utils import Driver


class Base_Element:

    def __init__(self, locator, name):
        self.driver = Driver.get_instance()
        self.locator = locator
        self.name = name

    def get_locator(self):
        return self.locator

    def get_element_name(self):
        return self.name

    def is_element_present(self):
        Wait_Utils.wait_to_be_present((By.XPATH, self.locator))
        return True

    def click(self):
        Wait_Utils.wait_to_be_clickable((By.XPATH, self.locator))
        element = self.driver.find_element(By.XPATH, self.locator)
        Logger.log_info(f"Clicking {self.name}")
        element.click()

    def get_text(self):
        Wait_Utils.wait_to_be_present((By.XPATH, self.locator))
        element = self.driver.find_element(By.XPATH, self.locator)
        Logger.log_info(f"Getting text from {self.name}")
        return element.text


class Button(Base_Element):
    def __init__(self, locator, name):
        super().__init__(locator=locator, name=name)


class Label(Base_Element):
    def __init__(self, locator, name):
        super().__init__(locator=locator, name=name)


class Link(Base_Element):
    def __init__(self, locator, name):
        super().__init__(locator=locator, name=name)


class Text_Box(Base_Element):
    def __init__(self, locator, name):
        super().__init__(locator=locator, name=name)

    def enter_text(self, text):
        Wait_Utils.wait_to_be_present((By.XPATH, self.locator))
        element = self.driver.find_element(By.XPATH, self.locator)
        Logger.log_info(f"Entering {text} into the {self.name} text box")
        element.send_keys(text)

    def clear(self):
        Wait_Utils.wait_to_be_present((By.XPATH, self.locator))
        element = self.driver.find_element(By.XPATH, self.locator)
        Logger.log_info(f"Clearing the {self.name} text box")
        element.clear()
