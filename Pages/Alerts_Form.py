from Pages.Base_Page import Base_Page
from WebElements.Elements import Button, Label


class Alerts_Form(Base_Page):
    button_alert = Button(locator="//button[@id='alertButton']", name="button_alert")
    button_confirm = Button(locator="//button[@id='confirmButton']", name="button_confirm")
    button_prompt = Button(locator="//button[@id='promtButton']", name="button_prompt")
    label_confirm_result = Label(locator="//span[@id='confirmResult']", name="label_confirm_result")
    label_prompt_result = Label(locator="//span[@id='promptResult']", name="label_prompt_result")

    def __init__(self):
        super().__init__(locator="//div[@id='javascriptAlertsWrapper']", name="alerts_form")

    def click_button_alert(self):
        self.button_alert.click()

    def click_button_confirm(self):
        self.button_confirm.click()

    def click_button_prompt(self):
        self.button_prompt.click()

    def get_text_from_label_confirm_result(self):
        return self.label_confirm_result.get_text()

    def get_text_from_label_prompt_result(self):
        return self.label_prompt_result.get_text()
