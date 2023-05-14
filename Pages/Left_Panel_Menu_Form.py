from Pages.Base_Page import Base_Page
from WebElements.Elements import Button, Label


class Left_Panel_Menu_Form(Base_Page):
    button_left_panel_elements = Button(locator="//div[@class='left-pannel']//div[text()='Elements']", name="button_left_panel_elements")
    button_alerts = Button(locator="//li[contains(@class, 'btn')]//span[contains(text(), 'Alerts')]", name="button_alerts")
    button_nested_frames = Button(locator="//li[contains(@class, 'btn')]//span[contains(text(), 'Nested')]", name="button_nested_frames")
    button_frames = Button(locator="//li[contains(@class, 'btn')]//span[(text() = 'Frames')]", name="button_frames")
    button_web_tables = Button(locator="//li[contains(@class, 'btn')]//span[(text() = 'Web Tables')]", name="button_web_tables")
    button_browser_windows = Button(locator="//li[contains(@class, 'btn')]//span[(text() = 'Browser Windows')]",
                                    name="button_browser_windows")
    button_links = Label(locator="//li[contains(@class, 'btn')]//span[(text() = 'Links')]", name="button_links")

    def __init__(self):
        super().__init__(locator="//div[@class='left-pannel']", name="elementsPage")

    def expand_accordion_elements(self):
        self.button_left_panel_elements.click()

    def click_button_alerts(self):
        self.button_alerts.click()

    def click_button_frames(self):
        self.button_frames.click()

    def click_button_nested_frames(self):
        self.button_nested_frames.click()

    def click_button_web_tables(self):
        self.button_web_tables.click()

    def click_button_browser_windows(self):
        self.button_browser_windows.click()

    def click_button_links(self):
        self.button_links.click()



