from assertpy import assert_that
from page_object_elements.web_ui.admin_user_page_elements import AdminUserPageElements
from page_objects.web_ui.webui_base_page import WebuiBasePage
from selenium.webdriver.common.keys import Keys
import time


class UsersPage(WebuiBasePage, AdminUserPageElements):
    # Define constructor and methods.
    def __init__(self, driver):
        super(UsersPage, self).__init__(driver)
        self.driver = driver
        self.wait_for_element_to_be_present(self.txt_username_loc, 5)
        assert_that(
            self.lbl_system_users.text).\
            is_equal_to("System Users").\
            described_as("System Users page cannot be reached.")

    def search_user(self, username, user_role, employee_name, status):
        if username is not None:
            self.txt_username = username
        if user_role is not None:
            self.sel_user_role = user_role
        if employee_name is not None:
            self.txt_employee_name = employee_name
            self.txt_employee_name.send_keys(Keys.TAB)
        if status is not None:
            self.sel_status = status

        self.click_on_search_button()
        # TODO: Remove Sleep
        time.sleep(1)

    def click_on_search_button(self):
        self.btn_search.click()

    def is_user_found(self, user_name):
        table = self.tbl_user_search_result
        tr_list = table.find_elements_by_xpath("//tr")
        ui_data = []

        for row in tr_list[1::]:
            td_list = row.find_elements_by_tag_name("td")
            temp = []
            for td in td_list[1::]:
                temp.append(td.text)
            ui_data.append(temp)

        return ui_data[0][0] == user_name
