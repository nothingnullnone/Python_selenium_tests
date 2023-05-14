from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

from Utils.Web_Driver_Utils import Driver
from Utils import Wait_Utils
from Utils.Logger import Logger


class Browser:

    @staticmethod
    def scroll_to_element(locator, name):
        driver = Driver.get_instance()
        Wait_Utils.wait_to_be_present((By.XPATH, locator))
        element = driver.find_element(By.XPATH, locator)
        Logger.log_info(f"Scrolling to the element {name}")
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def switch_to_frame(locator, name):
        driver = Driver.get_instance()
        Wait_Utils.wait_to_be_present((By.XPATH, locator))
        frame = driver.find_element(By.XPATH, locator)
        Logger.log_info("Switching to the " + name + " frame")
        driver.switch_to.frame(frame)

    @staticmethod
    def switch_to_default_content():
        driver = Driver.get_instance()
        Logger.log_info("Switching to the default content")
        driver.switch_to.default_content()

    @staticmethod
    def switch_to_next_tab(tabs_cnt):
        driver = Driver.get_instance()
        orig_window = driver.current_window_handle
        Wait_Utils.wait_to_open_new_tab(tabs_cnt)
        for window_handle in driver.window_handles:
            if window_handle != orig_window:
                Logger.log_info("Switching to the next tab")
                driver.switch_to.window(window_handle)
                break
        return driver.current_window_handle

    @staticmethod
    def switch_to_tab(window_handle):
        driver = Driver.get_instance()
        Logger.log_info(f"Switching to the tab with handle {window_handle}")
        driver.switch_to.window(window_handle)

    @staticmethod
    def close_tab():
        driver = Driver.get_instance()
        Logger.log_info("Closing a tab")
        driver.close()

    @staticmethod
    def get_tab_handle():
        driver = Driver.get_instance()
        return driver.current_window_handle

    @staticmethod
    def get_tabs_count():
        driver = Driver.get_instance()
        return len(driver.window_handles)


class Alerts:

    @staticmethod
    def get_alert():
        driver = Driver.get_instance()
        Wait_Utils.wait_for_alert()
        return driver.switch_to.alert

    @staticmethod
    def get_alert_text(alert):
        Logger.log_info("Getting text from an alert")
        return alert.text

    @staticmethod
    def accept_alert(alert):
        Logger.log_info("Clicking 'OK' in an alert")
        return alert.accept()

    @staticmethod
    def set_alert_input_text(alert, text):
        Logger.log_info(f"Sending {text} to an alert")
        alert.send_keys(text)

    @staticmethod
    def is_alert_present():
        try:
            alert = Driver.get_instance().switch_to.alert
            return True
        except NoAlertPresentException:
            return False
