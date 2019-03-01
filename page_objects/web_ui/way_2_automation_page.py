from assertpy import assert_that
from lib.mock_data import Generator
from page_object_elements.web_ui.way_2_automation_page_elements import Way2AutomationPageElements
from page_objects.web_ui.webui_base_page import WebuiBasePage


class Way2AutomationPage(WebuiBasePage, Way2AutomationPageElements):

    def __init__(self, context):
        super(Way2AutomationPage, self).__init__(context.driver)
        self.driver = context.driver
        self.driver.get(context.execution_data["sut_url"])
        self.wait_for_element_to_be_present(self.img_logo_loc)
        assert_that(self.lbl_title.text).is_equal_to_ignoring_case("Website For Testing Selenium / QTP Scripts")
        self.person = Generator.get_person()

    def go_to(self, section):
        if section == "frames and windows":
            self.menu_frames_and_windows.click()
        elif section == "interactions":
            self.menu_interaction.click()
        elif section == "widget":
            self.menu_widget.click()
        elif section == "alerts":
            self.menu_alert.click()

        # Switching to the new window
        self.switch_to_window("Welcome to the Test Site")

        self.wait_for_element_to_be_present(self.txt_username_loc, 10)
        # Wait for Registration form. If is present, fill it. If not, continue.
        if self.element_is_present(self.driver, self.block_registration_form_loc):
            self.fill_registration_form()

    def fill_registration_form(self):
        # self.wait_for_element_to_be_present(self.txt_name_loc, 10)
        self.wait_for_element_to_be_clickable(self.driver, self.txt_name_loc, 15)
        self.txt_name = self.person.name
        self.txt_phone = self.person.phone
        self.txt_email = self.person.email
        self.sel_country = "Argentina"
        self.txt_city = "Mendoza"
        self.txt_username = self.person.email
        self.txt_password = "123123123"
        self.btn_submit.click()

        # Wait for redirection
        self.wait_for_function_truth(self.element_has_gone_stale, self.btn_submit)

    def handle_js_alert(self):
        # Handle Javascript Alert
        self.menu_alert.click()
        self.tab_simple_alert.click()

        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[0])

        self.wait_for_element_to_be_clickable(self.driver, self.btn_display_alert_loc)
        self.btn_display_alert.click()
        self.accept_alert()
        self.driver.switch_to.default_content()

    # TODO: Check alert input
    def handle_js_input_alert(self):
        # Handle Input Alert
        self.tab_input_alert.click()

        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[1])

        self.btn_display_alert.click()
        self.accept_alert(self.p.name)
        self.driver.switch_to.default_content()

    def handle_submit_buttons(self):

        # Mouse Over menus
        self.do_mouseover(self.menu_dynamic_elements_loc)
        self.do_mouseover(self.menu_submit_button_clicked_loc)

        # Click Submenu
        self.menu_submit_button_clicked.click()

        # Selects "Starts With" Tab
        self.tab_starts_with.click()
        self.txt_form_input = "Form 1"
        self.btn_form_submit.click()

        # Selects "Ends With" Tab
        self.tab_ends_with.click()
        self.txt_form_input = "Form 2"
        self.btn_form_submit.click()

        # Selects "Complete ID Dynamic" Tab
        self.tab_completed_id_dynamic.click()
        self.txt_form_input = "Form 3"
        self.btn_form_submit.click()

    def verify_submitted_value(self, section):
        if section.lower() == "starts with":
            self.tab_starts_with.click()
            text = self.txt_form_input.text
        elif section.lower() == "ends with":
            self.tab_ends_with.click()
            text = self.txt_form_input.text
        elif section.lower() == "complete id dynamic":
            self.tab_complete_id_dynamic.click()
            text = self.txt_form_input.text
        else:
            text = "<Not Found>"

        return text
