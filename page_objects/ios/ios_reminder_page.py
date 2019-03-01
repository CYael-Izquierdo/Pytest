from page_objects.ios.ios_base_page import IosBasePage
from page_object_elements.ios.ios_reminder_page_elements import IosReminderPageElements
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException


class IosReminderPage(IosBasePage, IosReminderPageElements):
    def __init__(self, driver):
        super(IosReminderPage, self).__init__(driver)

    def search_reminder_schedule(self):
        pass

    def add_reminder(self, reminder_type="reminder"):
        try:
            self.btn_back.click()
        except:
            pass
        self.wait_for_element_to_be_present(element_locator=self.btn_add_loc, waiting_time=10)
        self.btn_add.click()

        if reminder_type.lower() == "reminder":
            self.btn_add_reminder.click()
        elif reminder_type.lower() == "list":
            self.btn_add_list.click()

    def complete_reminder(self, context, test_data):

        self.wait_for_element_to_be_present(element_locator=self.txt_reminder_title_loc,
                                            waiting_time=10)
        self.driver.set_value(element=self.txt_reminder_title, value=test_data.get("reminder_title"))

        if test_data.get("reminder_day", "no").lower() == "yes":
            self.complete_reminder_day(test_data)
        self.set_priority(test_data.get("reminder_priority"))
        if test_data.get("reminder_notes", False):
            self.wait_for_element_to_be_present(element_locator=self.txt_reminder_notes_loc, waiting_time=5)
            self.driver.set_value(element=self.txt_reminder_notes, value=test_data.get("reminder_notes"))

        self.btn_done.click()

    def set_priority(self, priority):
        if priority.lower() == "none":
            self.btn_priority_none.click()
        elif priority.lower() == "low":
            self.btn_priority_low.click()
        elif priority.lower() == "medium":
            self.btn_priority_medium.click()
        elif priority.lower() == "high":
            self.btn_priority_high.click()
        else:
            raise Exception("Invalid priority: " + priority)

    def complete_reminder_day(self, test_data):
        self.btn_reminder_day.click()

        # TODO: Complete reminder day, hour, min and am/pm
        if test_data.get("reminder_day"):
            pass
        if test_data.get("reminder_hour"):
            pass
        if test_data.get("reminder_min"):
            pass
        if test_data.get("reminder_am_pm"):
            pass

    def search_reminder(self, reminder):
        # Search string
        try:
            self.driver.set_value(element=self.txt_search_reminder, value=reminder)
        except AttributeError:
            raise NoSuchElementException()

        # Element found
        reminder_found = self.wait_for_element_to_be_present(element_locator=self.first_search_result_loc, waiting_time=5)
        self.hide_keyboard()

        return reminder_found

    def delete_reminder(self, reminder):
        # Get element coordinate
        reminder_rect = reminder.rect
        x_coord = reminder_rect['x'] + reminder_rect['width']
        y_coord = reminder_rect['y'] + reminder_rect['height'] / 2

        self.slide_left_from(from_coord=(x_coord, y_coord))









