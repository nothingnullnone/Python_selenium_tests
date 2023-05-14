from Pages.Base_Page import Base_Page
from WebElements.Elements import Button, Label


class Upper_Frame_Form(Base_Page):
    label_upper_frame = Label(locator="//*[@id='sampleHeading']", name="label_upper_frame")

    def __init__(self):
        super().__init__(locator="//iframe[@id='frame1']", name="upper_frame_form")

    def get_text_from_label(self):
        return self.label_upper_frame.get_text()


class Lower_Frame_Form(Base_Page):
    label_lower_frame = Label(locator="//*[@id='sampleHeading']", name="label_lower_frame")

    def __init__(self):
        super().__init__(locator="//iframe[@id='frame2']", name="lower_frame_form")

    def get_text_from_label(self):
        return self.label_lower_frame.get_text()


class Frames_Form(Base_Page):
    upper_frame_form = Upper_Frame_Form()
    lower_frame_form = Lower_Frame_Form()

    def __init__(self):
        super().__init__(locator="//iframe[@src='/sample' and @id='frame2']", name="frames_form")

    def get_upper_frame_form(self):
        return self.upper_frame_form

    def get_lower_frame_form(self):
        return self.lower_frame_form



