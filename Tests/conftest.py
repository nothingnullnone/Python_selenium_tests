import pytest

from Utils.Logger import Logger
from Utils.Web_Driver_Utils import Driver


@pytest.fixture(scope="session")
def browser():
    driver = Driver.get_instance()
    Logger.log_info("Initializing driver")
    yield driver
    Driver.destroy_driver()
