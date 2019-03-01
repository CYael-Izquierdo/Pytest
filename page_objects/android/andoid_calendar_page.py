from page_objects.android.android_base_page import AndroidBasePage
from page_object_elements.android.android_anydo_page_elements import AndroidAnydoPageElements
from page_object_elements.android.android_calendar_page_elements import AndroidCalendarPageElement
from page_objects.ios.ios_base_page import IosBasePage
from datetime import datetime


class AndroidCalendarPage(AndroidBasePage, AndroidCalendarPageElement):

    months = {'Jan': 1,
              'Feb': 2,
              'Mar': 3,
              'Apr': 4,
              'May': 5,
              'Jun': 6,
              'Jul': 7,
              'Aug': 8,
              'Sep': 9,
              'Oct': 10,
              'Nov': 11,
              'Dec': 12}

    def __init__(self, driver):
        super().__init__(driver=driver)

        if self.is_ios_test():
            self.scroll_down = IosBasePage().scroll_down
            self.scroll_down_to = IosBasePage().scroll_down_to

    def select_date(self, date: datetime):
        self.wait_for_element_to_be_clickable(self.txt_picker_day_loc, waiting_time=5)
        self.select_year(date.year)
        self.select_month(date.month)
        self.select_day(date.day)
        self.btn_ok.click()
        self.btn_ok.click()

    def select_year(self, year):
        self.btn_year.click()
        current_year = int(self.btn_year.text)
        i = 4
        while i > 0:
            for year_we in self.list_years:
                if int(year_we.text) == year:
                    year_we.click()
                    return
            if year > current_year:
                self.scroll_down_element(self.list_view_years)
            elif year < current_year:
                self.scroll_up_element(self.list_view_years)
            i += 1

    def select_month(self, month):
        current_month = self.months.get(self._get_calendar_month())

        aux = current_month - month
        for i in range(0, abs(aux)):
            if aux < 0:
                self.scroll_down_element(self.month_calendar)
            if aux > 0:
                self.scroll_up_element(self.month_calendar)

    def select_day(self, day):
        self.list_days_of_current_month[day-1].click()

    def _get_calendar_month(self):
        day: str = self.txt_picker_day.text
        month = day.split(' ')[1]
        return month
