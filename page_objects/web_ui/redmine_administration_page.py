from page_objects.web_ui.webui_base_page import WebuiBasePage
from page_object_elements.web_ui.redmine_administration_page_elements import RedmineAdministrationPageElements
from page_objects.web_ui.redmine_homepage_page import RedmineHomepagePage
from page_objects.android.android_base_page import AndroidBasePage


class RedmineAdministrationPage(WebuiBasePage, AndroidBasePage, RedmineAdministrationPageElements):
    def __init__(self, driver):
        super(RedmineAdministrationPage, self).__init__(driver=driver)
        self.homepage_po = RedmineHomepagePage(self.driver)

    def navigate_to(self, section):
        if section.upper() == "PROJECTS":
            self.btn_project.click()

