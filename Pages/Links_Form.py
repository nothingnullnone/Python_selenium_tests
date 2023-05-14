from Pages.Base_Page import Base_Page
from WebElements.Elements import Link


class Links_Form(Base_Page):
    link_home = Link(locator="//a[@id='simpleLink']", name="link_home")

    def __init__(self):
        super().__init__(locator="//div[@id='linkWrapper']", name="links_form")

    def click_link_home(self):
        self.link_home.click()
