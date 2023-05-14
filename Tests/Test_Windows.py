from Tests.Base_Test import Base_Test
from Utils import JSON_Utils
from Config.Filenames import Filenames
from Utils.Logger import Logger
from Utils.Web_Driver_Utils import Driver
from Utils.Browser_Utils import Browser
from Pages.Main_Page import Main_Page
from Pages.Left_Panel_Menu_Form import Left_Panel_Menu_Form
from Pages.Browser_Windows_Form import *
from Pages.Sample_Page import *
from Pages.Links_Form import *


class Test_Windows(Base_Test):

    def test_windows(self):
        Logger.log_info("Starting Test Case 4 - Handles")
        main_url = JSON_Utils.get_json_field(Filenames.cfg_file.value, "main_url")
        Logger.log_info("Step 1 - Navigating to the Main Page")
        self.driver = Driver.get_instance()
        self.driver.get(main_url)
        self.main_page = Main_Page()
        assert self.main_page.is_form_present()
        Logger.log_info("Step 2: Clicking 'Alerts, Frame & Windows' button. In a menu clicking 'Browser Windows' button")
        self.main_page.click_button_alerts_frame_windows()
        self.left_panel_menu_form = Left_Panel_Menu_Form()
        self.left_panel_menu_form.click_button_browser_windows()
        self.browser_windows_form = Browser_Windows_Form()
        assert self.browser_windows_form.is_form_present()
        init_tab_handle = Browser.get_tab_handle()
        Logger.log_info("Step 3 - Clicking 'New Tab' button")
        open_tabs_cnt = Browser.get_tabs_count()
        self.browser_windows_form.click_button_new_tab()
        Browser.switch_to_next_tab(open_tabs_cnt)
        self.sample_page = Sample_Page()
        sample_page_tab_handle = Browser.get_tab_handle()
        assert self.sample_page.is_form_present()
        assert not init_tab_handle == sample_page_tab_handle
        Logger.log_info("Step 4 - Closing current tab")
        Browser.close_tab()
        Browser.switch_to_tab(init_tab_handle)
        assert self.browser_windows_form.is_form_present()
        Logger.log_info("Step 5 - Clicking 'Elements'->'Links' button in the left menu")
        self.left_panel_menu_form.expand_accordion_elements()
        self.left_panel_menu_form.click_button_links()
        self.links_form = Links_Form()
        assert self.links_form.is_form_present()
        Logger.log_info("Step 6 - Clicking on 'Home' link")
        open_tabs_cnt = Browser.get_tabs_count()
        self.links_form.click_link_home()
        Browser.switch_to_next_tab(open_tabs_cnt)
        new_main_page_tab_handle = Browser.get_tab_handle()
        assert self.main_page.is_form_present()
        assert not init_tab_handle == new_main_page_tab_handle
        Logger.log_info("Step 7 - Resume to previous tab")
        Browser.switch_to_tab(init_tab_handle)
        assert self.links_form.is_form_present()



