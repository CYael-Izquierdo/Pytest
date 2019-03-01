from assertpy import assert_that
from page_object_elements.web_ui.belax_page_elements import BelaxPageElements
from page_objects.web_ui.common_page import *
from page_objects.web_ui.webui_base_page import WebuiBasePage


class BelaxPage(WebuiBasePage, BelaxPageElements):
    title = 'Belatrix Software: Software Outsourcing South America'

    # Define constructor and methods.
    def __init__(self, driver):
        super(BelaxPage, self).__init__(driver)
        self.driver = driver
        self.common_page = OrangeCommonPage(self.driver)
        self.wait_for_element_to_be_present(self.lnk_contact_loc, 90)
        assert_that(self.driver.title).\
            is_equal_to_ignoring_case(self.title).\
            described_as("Main page cannot be reached.")

    def contact_us(self):
        self.lnk_contact.click()
        self.wait_for_element_to_be_present(element_locator=self.txt_first_name_loc, waiting_time=60)
        self.txt_first_name = "Fake name"
        self.txt_last_name = "Fake last name"
        self.txt_email = "fakeemail@fakehost.com"
        self.txt_phone = "2255442266"
        self.txt_company = "CoE"
        self.sel_service = "Looking for a job"
        self.btn_submit.click()

    def check_if_contact_message_is_sent(self):
        self.wait_for_element_to_be_present(element_locator=self.lbl_message_sent_loc, waiting_time=5)
        ui_msg = self.lbl_message_sent.text
        expected_msg = "Thanks for your request!"

        return ui_msg == expected_msg