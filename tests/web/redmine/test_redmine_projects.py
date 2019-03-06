import pytest
from lib import framework
from assertpy import soft_assertions, assert_that
from tests.web.redmine import helper_redmine_project as helper

# -------------------------------------------------------------------------------

browser_list = [
                'chrome_default_config',
                'chrome_mac_config_1',
                'chrome_mac_headless_config'
                ]


@pytest.fixture(params=browser_list)
def driver(request):
    driver = framework.setup_desktop_browser(request.param)
    yield driver
    driver.quit()

# -------------------------------------------------------------------------------



class TestRedmineProject:
    @pytest.mark.Working
    @pytest.mark.usefixtures('clean_project_list')
    @pytest.mark.parametrize("project_name, description, identifier, homepage", [
        ('Quantum', 'This project is about...', 'quantum', 'https://www.quantum.com'),
        ('Quantum123', 'This project is about...', 'quantum', 'https://www.quantum.com')
        ])
    def test_create_project(self, driver, project_name, description, identifier, homepage):
        helper.connect_to_redmine(driver, 'Redmine')
        helper.login_into_redmine(driver)
        project_info = helper.create_project_dict(project_name, description, identifier, homepage)
        helper.create_project(driver, project_info)
        helper.verify_project_successfully_created(driver)
        helper.verify_that_project_is_in_projects_list(driver, project_info)

