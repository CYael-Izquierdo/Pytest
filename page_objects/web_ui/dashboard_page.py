from assertpy import assert_that
from page_object_elements.web_ui.dashboard_page_elements import DashboardPageElements
from page_objects.web_ui.common_page import *


class OrangeDashboardPage(WebuiBasePage, DashboardPageElements):
    title = 'OrangeHRM'

    # Define constructor and methods.
    def __init__(self, driver):
        super(OrangeDashboardPage, self).__init__(driver)
        self.driver = driver
        self.common_page = OrangeCommonPage(self.driver)
        self.wait_for_element_to_be_present(self.dashboard_title_loc, 30)
        assert_that(self.lbl_dashboard_title.__getattribute__("text")).\
            is_equal_to_ignoring_case("Dashboard").\
            described_as("Dashboard page cannot be reached.")

    def get_welcome_user(self):
        return self.common_page.get_welcome_user()

    def go_to_welcome_dropdown(self, value):
        self.common_page.select_value_in_welcome_dropdown(value)

    def go_to_menu(self, value):
        self.common_page.select_menu(value)
