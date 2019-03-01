from page_objects.web_ui.webui_base_page import WebuiBasePage
from page_object_elements.web_ui.redmine_admin_projects_page_elements import RedmineAdminProjectsPageElements
from page_objects.web_ui.redmine_homepage_page import RedmineHomepagePage
from page_objects.android.android_base_page import AndroidBasePage


class RedmineAdminProjectsPage(WebuiBasePage, AndroidBasePage, RedmineAdminProjectsPageElements):
    def __init__(self, driver):
        super(RedmineAdminProjectsPage, self).__init__(driver=driver)
        self.homepage_po = RedmineHomepagePage(self.driver)

    def delete_all_projects(self):
        self.wait_for_element_to_be_present(element_locator=self.txt_project_name_loc, waiting_time=20)
        while True:
            if len(self.delete_projects_bnt_list) != 0:
                self.delete(self.delete_projects_bnt_list[0])
            else:
                break

    def delete(self, project):
        project.click()
        self.chk_confirm_delete_project.click()
        self.btn_delete_project.click()

