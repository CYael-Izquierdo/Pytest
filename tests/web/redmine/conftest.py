import pytest
from lib import framework
from page_objects.web_ui.redmine_administration_page import RedmineAdministrationPage
from page_objects.web_ui.redmine_admin_projects_page import RedmineAdminProjectsPage


@pytest.fixture
def clean_project_list():
    yield
    driver = framework.setup_desktop_browser('chrome_mac_headless_config')
    admin_po = RedmineAdministrationPage(driver=driver)

    admin_po.homepage_po.click_on_link("administration")
    admin_po.navigate_to("projects")

    admin_projects_po = RedmineAdminProjectsPage(driver=driver)
    admin_projects_po.delete_all_projects()
