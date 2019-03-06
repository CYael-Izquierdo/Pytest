import pytest
from tests.web.redmine import helper_redmine_project as helper
from lib import framework


@pytest.fixture(scope="class")
def clean_project_list():
    yield
    driver = framework.setup_desktop_browser('chrome_mac_headless_config')
    helper.connect_to_redmine(driver, 'Redmine')
    helper.login_into_redmine(driver)
    helper.delete_all_projects(driver)
