from page_objects.android.android_base_page import AndroidBasePage
from page_object_elements.android.android_anydo_page_elements import AndroidAnydoPageElements
from page_objects.android.andoid_calendar_page import AndroidCalendarPage
from page_objects.ios.ios_base_page import IosBasePage


class AndroidAnydoPage(AndroidBasePage, AndroidAnydoPageElements):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.calendar = AndroidCalendarPage(driver)

        if self.is_ios_test():
            self.scroll_down = IosBasePage().scroll_down
            self.scroll_down_to = IosBasePage().scroll_down_to

    def add_task(self, task_title, task_day, date=None):
        self.btn_add_task.click()
        self.txt_task_title.set_value(task_title)
        self.set_task_day(task_day)
        if task_day == 'Custom':
            if date:
                self.calendar.select_date(date)
        self.btn_confirm_task.click()
        self.hide_keyboard()

    def set_task_day(self, task_day: str):
        if task_day != 'Today':
            i = 4
            while i >= 0:
                btn_task_day = self.get_task_day_we(task_day)
                if btn_task_day is not None and self.is_visible(btn_task_day, is_locator=False):
                    btn_task_day.click()
                    break
                self.slide_left_from(element=self.bar_day)

    ######## VER COMO MANDAR EL WE#####

    def get_task_day_we(self, task_day):

        task_day = task_day.capitalize()

        switcher = {
            "Later today": self.btn_later_today,
            "This evening": self.btn_this_evening,
            "Tomorrow morning": self.btn_tomorrow_morning,
            "Next week": self.btn_next_week,
            "Someday": self.btn_someday,
            "Custom": self.btn_custom
        }

        return switcher.get(task_day)

    def find_task(self, task_title):
        i = 0
        while i < 5:
            for task in self.list_tasks:
                if task.text == task_title and self.is_visible(task, is_locator=False):
                    return task
            i += 1
        return None

    def delete_task(self, task_title):
        task_we = self.find_task(task_title)
        task_we.click()
        self.wait_for_element_to_be_clickable(self.task_detail_loc, waiting_time=10)
        self.scroll_down_to(self.btn_delete_task_loc)
        self.btn_delete_task.click()
        self.wait_for_element_to_be_clickable(self.btn_true_delete_button_loc, waiting_time=5)
        self.btn_true_delete_button.click()
