from assertpy import assert_that
from selenium.webdriver.common.keys import Keys
from page_object_elements.web_ui.redmine_login_page_elements import RedmineLoginPageElements
from page_objects.web_ui.webui_base_page import WebuiBasePage
from page_objects.android.android_base_page import AndroidBasePage
from page_objects.web_ui.redmine_homepage_page import RedmineHomepagePage


class RedmineLoginPage(WebuiBasePage, AndroidBasePage, RedmineLoginPageElements):

    # Define constructor and methods.
    def __init__(self, driver, uri=None):
        super(RedmineLoginPage, self).__init__(driver)
        self.homepage_po = RedmineHomepagePage(self.driver)
        self.url = uri
        self.is_mobile = self.check_is_mobile_emulation()
        self.is_android = self.is_android_test()
        self.is_ios = self.is_ios_test()

    def login(self, username: str, password: str):
        if self.is_mobile:
            self.homepage_po.click_on_mobile_menu()

        self.homepage_po.click_on_link("sign in")

        self.wait_for_element_to_be_present(element_locator=self.btn_sign_in_loc, waiting_time=10)
        assert_that(self.driver.title).is_equal_to("Redmine").described_as("System login page cannot be reached.")

        self.wait_for_element_to_be_present(self.txt_user_name_loc, 10)
        assert_that(self.txt_user_name_loc).is_true().described_as("System login page cannot be reached.")
        self.fill_username(username)
        self.fill_password(password)
        self.btn_login.submit()
        self.wait_for_invisibility_of_element(element_locator=self.txt_user_name_loc, waiting_time=5)

    def fill_username(self, username: str):
        self.txt_user_name = username
        self.txt_user_name = Keys.TAB

    def fill_password(self, password):
        self.txt_password = password
        self.txt_password = Keys.TAB

    def get_login_text(self):
        return self.login_panel.text
