from Config.Filenames import Filenames
from Pages.Alerts_Form import Alerts_Form
from Pages.Left_Panel_Menu_Form import Left_Panel_Menu_Form
from Pages.Main_Page import Main_Page
from Tests.Base_Test import Base_Test
from Utils import JSON_Utils, String_Utils
from Utils.Web_Driver_Utils import Driver
from Utils.Browser_Utils import Alerts
from Utils.Logger import Logger


class Test_Alerts(Base_Test):

    def test_alerts(self):
        Logger.log_info("Starting Test Case 1 - Alerts")
        main_url = JSON_Utils.get_json_field(Filenames.cfg_file.value, "main_url")
        self.driver = Driver.get_instance()
        self.driver.get(main_url)
        self.main_page = Main_Page()
        assert self.main_page.is_form_present()
        Logger.log_info("Step 2: Clicking 'Alerts, Frame & Windows' button. In a menu clicking 'Alerts' button")
        self.main_page.click_button_alerts_frame_windows()
        self.left_panel_menu_form = Left_Panel_Menu_Form()
        self.left_panel_menu_form.click_button_alerts()
        self.alerts_form = Alerts_Form()
        assert self.alerts_form.is_form_present()
        Logger.log_info("Step 3: Clicking 'Click button to see alert' button");
        self.alerts_form.click_button_alert()
        text_alert_clicked = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_alert_clicked")
        alert_clicked = Alerts.get_alert()
        assert Alerts.get_alert_text(alert_clicked) == text_alert_clicked
        Logger.log_info("Step 4: Clicking 'OK' button")
        Alerts.accept_alert(alert_clicked)
        assert not Alerts.is_alert_present()
        Logger.log_info("Step 5: Clicking 'On button click, confirm box will appear' button")
        self.alerts_form.click_button_confirm()
        alert_confirm = Alerts.get_alert();
        text_alert_confirm = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_alert_confirm")
        assert Alerts.get_alert_text(alert_confirm) == text_alert_confirm
        Logger.log_info("Step 6: Clicking 'OK' button")
        Alerts.accept_alert(alert_confirm)
        assert not Alerts.is_alert_present()
        text_label_ok = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_label_ok")
        assert self.alerts_form.get_text_from_label_confirm_result() == text_label_ok
        Logger.log_info("Step 7: Clicking 'On button click, prompt box will appear' button")
        self.alerts_form.click_button_prompt()
        alert_prompt = Alerts.get_alert()
        text_alert_prompt = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_alert_prompt")
        assert Alerts.get_alert_text(alert_prompt) == text_alert_prompt
        randomText = String_Utils.get_random_string()
        Logger.log_info("Step 8: Entering randomly generated string, clicking 'OK' button")
        Alerts.set_alert_input_text(alert_prompt, randomText)
        Alerts.accept_alert(alert_prompt)
        assert not Alerts.is_alert_present()
        text_label_entered = JSON_Utils.get_json_field(Filenames.test_file_alerts.value, "text_label_entered")
        assert self.alerts_form.get_text_from_label_prompt_result() == text_label_entered + randomText


