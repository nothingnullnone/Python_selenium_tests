from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Config.Filenames import *
from Utils import JSON_Utils
from Utils.Logger import Logger


class Driver:
    __driver = None

    def __init__(self):
        if not Driver.__driver:
            browser = JSON_Utils.get_json_field(Filenames.cfg_file.value, "browser")
            options = JSON_Utils.get_json_field(Filenames.cfg_file.value, "options")
            page_load_strategy = JSON_Utils.get_json_field(Filenames.cfg_file.value, "page_load_strategy")
            Logger.log_info(f"{browser} is initializing with options {options}")
            try:
                Driver.__driver = BrowserFactory.init_driver(browser=browser, options=options, page_load_strategy=page_load_strategy)
            except Exception:
                Logger.log_error("Driver initialization error!")
                raise RuntimeError

    @classmethod
    def get_instance(cls):
        if not cls.__driver:
            Driver()
        return cls.__driver

    @classmethod
    def destroy_driver(cls):
        if cls.__driver:
            Logger.log_info("Destroying driver!")
            cls.__driver.quit()
            cls.__driver = None


class BrowserFactory:

    @staticmethod
    def init_driver(browser, options, page_load_strategy):
        match browser.lower():
            case "chrome":
                chrome_opts = webdriver.ChromeOptions()
                for _ in options.split(", "):
                    chrome_opts.add_argument(options)
                    chrome_opts.page_load_strategy = page_load_strategy
                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                        chrome_options=chrome_opts)
            case "firefox":
                return webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
            case "edge":
                return webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
            case _:
                raise Exception("Error browser initialization!")
