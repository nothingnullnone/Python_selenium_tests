from Pages.Base_Page import Base_Page
from WebElements.Elements import Button


class Main_Page(Base_Page):
    button_alerts_frame_windows = Button(locator="//div[@class='category-cards']//*[text() = 'Alerts, Frame & Windows']",
                                         name="button_alerts_frame_windows")
    button_elements = Button(locator="//div[@class='category-cards']//*[text() = 'Elements']", name="button_elements")

    def __init__(self):
        super().__init__(locator="//div[@class='category-cards']", name="main_page")

    def click_button_alerts_frame_windows(self):
        self.button_alerts_frame_windows.click()

    def click_button_elements(self):
        self.button_elements.click()
