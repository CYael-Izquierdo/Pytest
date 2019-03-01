from page_objects.image.image_desktop_page import ImageDesktopPage
from page_object_elements.image.macos.reminder.macos_reminders_page_elements import MacOsRemindersPagePageElements
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from retry.api import retry
from assertpy import assert_that


class MacOsReminderPage(ImageDesktopPage, MacOsRemindersPagePageElements):

    def __init__(self):
        super(MacOsReminderPage, self).__init__(class_name=MacOsReminderPage.__name__)
        self.keyboard = PyKeyboard()
        self.mouse = PyMouse()

        # self.wait(2)
        # # Comparing home screenshot against standard image
        # self.page_image.grab_screen(path=self.full_image_output_path)
        # self.page_image.set_threshold(0.98)
        # assert_that(self.page_image.find_img_on_screen(target_img_path=self.reminder_standard_image_path,
        #                                                full_img_path=self.full_image_output_path,
        #                                                draw_rectangle=True)).described_as(
        #     "Reminder screenshot does not match with the standard image: " + "\n" +
        #     "Standard image: " + self.reminder_standard_image_path + "\n" +
        #     "Screenshot image: " + self.full_image_output_path). \
        #     is_true()

    def add_reminder_by_menu(self, td):
        # ## Open Reminder by command shortcuts
        # self.keyboard.press_keys(['Command', "Space"])
        # self.keyboard.type_string("Reminders")
        # self.keyboard.press_keys(['Return'])
        ##

        self.add_reminder()
        self.complete_reminder(td)

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def add_reminder(self):
        self.menu_file.click()
        self.menu_file_new_reminder.click()

    # @retry(exceptions=Exception, tries=5, delay=0.1)
    def complete_reminder(self, td):
        self.txt_reminder_name_prompt = td["reminder_title"]

        # shortcut - Reminder info
        self.keyboard.press_keys(['Command', 'I'])

        if td.get("reminder_priority", False):
            self.set_priority(td)

        if td.get("reminder_notes", False):
            self.add_note(td["reminder_notes"])

        # Done
        self.btn_done.click()

        self.wait(1)

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def set_priority(self, td):
        self.sel_priority.click()

        if td["reminder_priority"].lower() == "low":
            self.sel_priority_low.click()
        elif td["reminder_priority"].lower() == "medium":
            self.sel_priority_medium.click()
        elif td["reminder_priority"].lower() == "high":
            self.sel_priority_high.click()

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def add_note(self, note):
        self.txt_note.click()
        self.txt_note = note

    def delete_reminder(self, reminder):
        self.get_reminder(name=reminder).click("right")
        self.wait(0.5)
        self.context_menu_delete.click()
        self.wait(0.5)

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def enter_full_screen_mode(self):
        self.menu_view.click()
        self.menu_view_enter_full_screen.click()

    def exit_full_screen_mode(self):
        self.keyboard.press_keys(['Escape'])
        self.keyboard.press_keys(['Escape'])

    @retry(exceptions=Exception, tries=5, delay=0.1)
    def get_reminder(self, name):
        if name.lower() == "lbl_send_the_weekly_report":
            return self.lbl_send_the_weekly_report
        else:
            raise Exception(
                4 * "<" + "[ERROR]" + 4 * "> " + "Reminder NOT found: " + name
            )

