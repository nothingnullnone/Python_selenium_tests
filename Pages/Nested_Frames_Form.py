from Pages.Base_Page import Base_Page
from WebElements.Elements import Button, Label


class Parent_Frame_Form(Base_Page):
    label_parent_frame = Label(locator="//body[contains(text(), 'Parent frame')]", name="label_parent_frame")

    def __init__(self):
        super().__init__(locator="//iframe[@id='frame1']", name="parent_frame_form")

    def get_text_from_label(self):
        return self.label_parent_frame.get_text()


class Child_Frame_Form(Base_Page):
    label_child_frame = Label(locator="//p[contains(text(), 'Child Iframe')]", name="labelChildIframe")

    def __init__(self):
        super().__init__(locator="//iframe[contains(@srcdoc, 'Child')]", name="child_frame_form")

    def get_text_from_label(self):
        return self.label_child_frame.get_text()


class Nested_Frames_Form(Base_Page):
    parent_frame_form = Parent_Frame_Form()
    child_frame_form = Child_Frame_Form()

    def __init__(self):
        super().__init__(locator="//iframe[@src='/sampleiframe' and @id='frame1']", name="nested_frames_form")

    def get_parent_frame_form(self):
        return self.parent_frame_form

    def get_child_frame_form(self):
        return self.child_frame_form



