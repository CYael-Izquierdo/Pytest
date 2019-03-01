from assertpy import assert_that
from selenium.webdriver.common.keys import Keys
from page_objects.web_ui.webui_base_page import WebuiBasePage
from page_object_elements.web_ui.orange_login_page_elements import OrangeLoginPageElements
from page_objects.web_ui.common_page import OrangeCommonPage
from page_objects.web_ui.dashboard_page import OrangeDashboardPage


class OrangeLoginPage(WebuiBasePage, OrangeLoginPageElements):
    tittle = "OrangeHRM"

    # Define constructor and methods.
    def __init__(self, driver, uri=None):
        super(OrangeLoginPage, self).__init__(driver=driver)
        self.common_page = OrangeCommonPage(self.driver)
        self.url = uri

        if uri is not None:
            self.driver.get(uri)

        self.wait_for_element_to_be_present(element_locator=self.txt_user_name_loc, waiting_time=20)

    def login(self, username, password):
        self.wait_for_element_to_be_present(element_locator=self.txt_user_name_loc, waiting_time=5)
        assert_that(self.driver.title).is_equal_to("OrangeHRM").described_as("System login page cannot be reached.")

        self.fill_username(username)
        self.fill_password(password)
        self.btn_login.click()
        return OrangeDashboardPage(self.driver)

    def fill_username(self, username):
        self.txt_user_name = username
        self.txt_user_name = Keys.TAB

    def fill_password(self, password):
        self.txt_password = password
        self.txt_password = Keys.TAB

    def get_login_text(self):
        return self.login_panel.text

    # TODO: Complete implementation
    def get_attribute(self, field, attribute):
        if field == "user_name":
            return self.txt_user_name.get_attribute(attribute)
        elif field == "password":
            return self.txt_password.get_attribute(attribute)
