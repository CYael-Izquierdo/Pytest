import pytest
from lib import framework
from page_objects.ios.ios_calendar_page import IosCalendarPage
from assertpy import soft_assertions, assert_that
from tests.mobile.ios.simulator import helper_ios_simulator_calendar as helper


# -------------------------------------------------------------------------------
browser_list = ['chrome_default_config', 'chrome_mac_config_1', 'chrome_mac_headless_config']


@pytest.fixture(params=browser_list)
def browser(request):
    return request.param
# -------------------------------------------------------------------------------


class TestRedmineProject:
    @pytest.mark.Working
    @pytest.mark.parametrize("project_name, description, identifier, homepage", [
        # ('left', 'Tomorrow'),
        ('right', 'Yesterday')
        ])
    def test_create_project(self, browser, direction, day):


