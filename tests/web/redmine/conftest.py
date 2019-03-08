import pytest
from lib import framework
from page_objects.web_ui.redmine_administration_page import RedmineAdministrationPage
from page_objects.web_ui.redmine_admin_projects_page import RedmineAdminProjectsPage
from tests.web.redmine import helper_redmine_project as helper


@pytest.fixture(scope='module')
def clean_project_list():
    yield
    driver = framework.setup_desktop_browser('chrome_mac_headless_config')
    helper.connect_to_redmine(driver, 'Redmine')
    helper.login_into_redmine(driver)
    helper.delete_all_projects(driver)

