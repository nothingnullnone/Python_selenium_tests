from Pages.Base_Page import Base_Page
from WebElements.Elements import Button


class Browser_Windows_Form(Base_Page):
    button_new_tab = Button(locator="//button[@id='tabButton']", name="button_new_tab")

    def __init__(self):
        super().__init__(locator="//div[@id='browserWindows']", name="browser_windows_form")

    def click_button_new_tab(self):
        self.button_new_tab.click()

