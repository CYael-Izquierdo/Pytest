from page_object_elements.web_ui.common_page_elements import CommonPageElements
from page_objects.web_ui.admin_users_page import UsersPage
from page_objects.web_ui.webui_base_page import WebuiBasePage
from retry import retry


class OrangeCommonPage(WebuiBasePage, CommonPageElements):

    # Define constructor and methods.
    def __init__(self, driver):
        super(OrangeCommonPage, self).__init__(driver)
        self.driver = driver

    def select_value_in_welcome_dropdown(self, option):
        if not self.wait_for_element_to_be_present(self.section_user_options_loc):
            self.sel_welcome.click()
        self.select_option_from_list(self.sel_user_options, option)

    def get_welcome_user(self):
        return self.sel_welcome.text

    def navigate_to(self, section):
        if section.lower() == "create user":
            self.do_mouseover(*self.menu_admin_loc)
            self.do_mouseover(*self.menu_user_management_loc)
            self.do_mouseover(*self.menu_users_loc)
            self.wait_for_element_to_be_present(self.menu_users_loc)
            self.menu_users.click()
            return UsersPage(self.driver)

        elif section.lower() == "job titles":
            self.menu_job.click()
            self.menu_job_title.click()

    def click_on_button(self, button):
        if button.lower() in ["about", "logout", "change password", "close about pop up"]:
            self.click_on_welcome_menu_options(button)
            return True
        else:
            raise Exception("Button " + button + " NOT Found.")

    @retry(exceptions=[Exception], tries=10, delay=0.5)
    def click_on_welcome_menu(self):
        self.wait_for_element_to_be_present(element_locator=self.sel_welcome_loc, waiting_time=5)
        self.sel_welcome.click()
        self.wait_for_element_to_be_present(element_locator=self.section_user_options_loc,
                                            waiting_time=5)

    def click_on_welcome_menu_options(self, option):
        self.click_on_welcome_menu()
        if option.lower() == "about":
            self.wait_for_element_to_be_present(self.btn_about_loc)
            self.btn_about.click()
            return True
        elif option.lower() == "logout":
            self.wait_for_element_to_be_clickable(self.btn_logout_loc, waiting_time=5)
            self.scroll_to(self.btn_logout)
            self.btn_logout.click()
            # self.select_value_in_welcome_dropdown(button)
            return True
        elif option.lower() == "change password":
            self.wait_for_element_to_be_present(self.btn_change_password_loc)
            self.btn_change_password.click()
            return True
        elif option.lower() == "close about pop up":
            self.sel_welcome.click()
            self.wait_for_element_to_be_present(self.btn_close_pop_up_loc)
            self.btn_close_pop_up.click()
            return True

    def select_menu(self, value):
        if value == "Admin":
            self.menu_admin.click()
        elif value == "User Management":
            self.menu_user_management.click()
        elif value == "PIM":
            self.menu_pim.click()
        elif value == "Leave":
            self.menu_leave.click()
        elif value == "Time":
            self.menu_time.click()
        elif value == "Recruitment":
            self.menu_recruitment.click()
        elif value == "Performance":
            self.menu_performance.click()
        elif value == "Directory":
            self.menu_directory.click()
        elif value == "Job":
            self.menu_job.click()
        elif value == "Job Titles":
            self.menu_job_title.click()
