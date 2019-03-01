from appium.webdriver.common.mobileby import MobileBy as By
from lib.appium_page_objects import PageElement, MultiPageElement
from page_objects.ios.ios_base_page import IosBasePage
from page_object_elements.ios.ios_calendar_page_element import IosCalendarPageElement
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException


class IosCalendarPage(IosBasePage, IosCalendarPageElement):

    def scroll_to_year(self, year):
        current_year = self.get_date_dict()['year']
        year_loc = (By.ACCESSIBILITY_ID, year)
        if year < current_year:
            self.scroll_up_to(year_loc)
        elif year > current_year:
            self.scroll_down_to(year_loc)

    def go_to_year_view(self):
        try:
            if self.btn_higher_view.text == self.get_date_dict()['month']:
                self.btn_higher_view.click()
                self.wait_for_element_to_be_clickable(self.btn_higher_view_loc)
                self.btn_higher_view.click()
            elif self.btn_higher_view.text == self.get_date_dict()['year']:
                self.btn_higher_view.click()
        except NoSuchElementException:
            pass

    def go_to_day_view(self):
        if self.btn_higher_view.text == self.get_date_dict()['year']:
            self.btn_lower_view.click()
        elif self.btn_higher_view.text == 'Search':
            self.btn_lower_view.click()
            self.wait_for_element_to_be_clickable(self.btn_lower_view_loc)
            self.btn_lower_view.click()

    @staticmethod
    def get_formatted_date(day: str = 'Today') -> str:
        """

        :param day: Today, Yesterday or Tomorrow
        :return: formatted datetime, like "Thursday 7 February 2019"
        """
        if day == 'Today':
            date = datetime.now()
        elif day == 'Yesterday':
            date = datetime.now() - timedelta(days=1)
        elif day == 'Tomorrow':
            date = datetime.now() + timedelta(days=1)
        else:
            return None
        return date.strftime('%A, %B %-d, %Y')

    @staticmethod
    def get_date_dict() -> dict:
        date = datetime.today()
        date_dict = {
            'year': date.strftime('%Y'),
            'month': date.strftime('%B'),
            'day': date.strftime('%A')
        }
        return date_dict

    def get_year_element(self, year: str):
        try:
            year_we = self.driver.find_element(By.ACCESSIBILITY_ID, year)
        except NoSuchElementException:
            year_we = None
        return year_we
