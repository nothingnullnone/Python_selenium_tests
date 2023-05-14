from Tests.Base_Test import Base_Test
from Utils import JSON_Utils, String_Utils
from Config.Filenames import Filenames
from Utils.Logger import Logger
from Utils.Web_Driver_Utils import Driver
from Utils.Browser_Utils import Browser
from Pages.Main_Page import Main_Page
from Pages.Left_Panel_Menu_Form import Left_Panel_Menu_Form
from Pages.Nested_Frames_Form import *
from Pages.Frames_Form import *


class Test_IFrames(Base_Test):

    def test_iframes(self):
        Logger.log_info("Starting Test Case 2 - IFrames")
        main_url = JSON_Utils.get_json_field(Filenames.cfg_file.value, "main_url")
        Logger.log_info("Step 1 - Navigating to the Main Page")
        self.driver = Driver.get_instance()
        self.driver.get(main_url)
        self.main_page = Main_Page()
        assert self.main_page.is_form_present()
        Logger.log_info("Step 2 - Clicking 'Alerts, Frame & Windows' button. In a menu clicking 'Nested frames' button")
        self.main_page.click_button_alerts_frame_windows()
        self.left_panel_menu_form = Left_Panel_Menu_Form()
        self.left_panel_menu_form.click_button_nested_frames()
        self.nested_frames_form = Nested_Frames_Form()
        assert self.nested_frames_form.is_form_present()
        self.parent_frame_locator = self.nested_frames_form.get_parent_frame_form().get_locator()
        self.parent_frame_name = self.nested_frames_form.get_parent_frame_form().get_form_name()
        Browser.switch_to_frame(self.parent_frame_locator, self.parent_frame_name)
        text_parent_frame = JSON_Utils.get_json_field(Filenames.test_file_frames.value, "text_parent_frame")
        assert self.nested_frames_form.get_parent_frame_form().get_text_from_label() == text_parent_frame
        self.child_frame_locator = self.nested_frames_form.get_child_frame_form().get_locator()
        self.child_frame_name = self.nested_frames_form.get_child_frame_form().get_form_name()
        Browser.switch_to_frame(self.child_frame_locator, self.child_frame_name)
        text_child_frame = JSON_Utils.get_json_field(Filenames.test_file_frames.value, "text_child_frame")
        assert self.nested_frames_form.get_child_frame_form().get_text_from_label() == text_child_frame
        Browser.switch_to_default_content()
        Logger.log_info("Step 3 - Selecting 'Frames' option in a left menu")
        self.left_panel_menu_form.click_button_frames()
        self.frames_form = Frames_Form()
        assert self.frames_form.is_form_present()
        self.upper_frame_locator = self.frames_form.get_upper_frame_form().get_locator()
        self.upper_frame_name = self.frames_form.get_upper_frame_form().get_form_name()
        Browser.switch_to_frame(self.upper_frame_locator, self.upper_frame_name)
        text_upper_frame = self.frames_form.get_upper_frame_form().get_text_from_label()
        Browser.switch_to_default_content()
        self.lower_frame_locator = self.frames_form.get_lower_frame_form().get_locator()
        self.lower_frame_name = self.frames_form.get_lower_frame_form().get_form_name()
        Browser.switch_to_frame(self.lower_frame_locator, self.lower_frame_name)
        text_lower_frame = self.frames_form.get_lower_frame_form().get_text_from_label()
        Browser.switch_to_default_content()
        assert text_lower_frame == text_upper_frame


