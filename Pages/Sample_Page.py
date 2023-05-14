from Pages.Base_Page import Base_Page


class Sample_Page(Base_Page):

    def __init__(self):
        super().__init__(locator="//*[@id='sampleHeading']", name="sample_page")
