import pytest
from lib import framework
from page_objects.ios.ios_calendar_page import IosCalendarPage
from assertpy import soft_assertions, assert_that
from tests.mobile.ios.simulator import helper_ios_simulator_calendar as helper


# -------------------------------------------------------------------------------
devices_list = ['ios_simulator_iphone6s_cfg']


@pytest.fixture(params=devices_list)
def device_loop(request):
    return request.param
# -------------------------------------------------------------------------------


class TestCalendar:
    @pytest.mark.Working
    @pytest.mark.parametrize("direction, day", [
        # ('left', 'Tomorrow'),
        ('right', 'Yesterday')
        ])
    def test_calendar_slice_in_day_view(self, device_loop, direction, day):
        capabilities = {'bundleId': 'com.apple.mobilecal'}
        driver = framework.setup_appium_driver(device_loop, capabilities)
        helper.slice_in_day_view(direction, driver)
        calendar_po = IosCalendarPage(driver)
        date = calendar_po.get_formatted_date(day)

        with soft_assertions():
            assert_that(calendar_po.txt_date.text).is_equal_to(date)

